import json
import os

# ========= FUNCIONES MODIFICADAS =========

def extraer_datos(data, es_following=False):
    """
    Extrae un diccionario {usuario: enlace_limpio} de los JSON de Instagram.
    Soluciona el error de redirección de los enlaces /_u/.
    """
    usuarios_dict = {}
    
    # Navegar por la estructura dependiendo de si es followers o following
    fuente = data.get("relationships_following", []) if es_following else data
    
    for user in fuente:
        # En following, a veces el nombre está en 'title'
        username_fallback = user.get("title")
        
        for item in user.get("string_list_data", []):
            username = item.get("value") or username_fallback
            link_original = item.get("href", "")
            
            # --- LIMPIEZA DE ENLACE (SOLUCIÓN AL ERROR DE INSTAGRAM) ---
            if "/_u/" in link_original:
                # Extraer el nombre de usuario después del /_u/ para crear link limpio
                user_clean = link_original.split("/_u/")[-1]
                link_final = f"https://www.instagram.com/{user_clean}/"
            elif link_original:
                # Asegurar que los links normales terminen en /
                link_final = link_original if link_original.endswith("/") else f"{link_original}/"
            else:
                link_final = "Enlace no disponible"
            
            # Si aún no tenemos username, intentamos sacarlo del link final
            if not username and link_final != "Enlace no disponible":
                username = link_final.split("/")[-2]
            
            if username:
                usuarios_dict[username] = link_final
                
    return usuarios_dict

def guardar_txt(nombre, lista_claves, diccionario_fuente):
    """
    Guarda en el TXT el formato: usuario - enlace
    """
    with open(nombre, "w", encoding="utf-8") as f:
        for user in sorted(lista_claves):
            enlace = diccionario_fuente.get(user, "No disponible")
            f.write(f"{user} - {enlace}\n")

def mostrar_lista(titulo, lista):
    print(f"\n{titulo} ({len(lista)}):\n" + "-"*40)
    for user in sorted(lista):
        print(user)

# ========= CARGA DE DATOS =========

try:
    with open("followers_1.json", "r", encoding="utf-8") as f:
        followers_data = json.load(f)
    with open("following.json", "r", encoding="utf-8") as f:
        following_data = json.load(f)
except FileNotFoundError:
    print("❌ No se encontraron los archivos JSON")
    print("Asegúrate de que 'followers_1.json' y 'following.json' estén en la misma carpeta.")
    input("Presiona ENTER para salir...")
    exit()

# Obtenemos diccionarios completos {usuario: link_limpio}
dict_followers = extraer_datos(followers_data)
dict_following = extraer_datos(following_data, es_following=True)

# Creamos sets para las operaciones matemáticas
set_followers = set(dict_followers.keys())
set_following = set(dict_following.keys())

# ========= CÁLCULOS =========

no_te_siguen = set_following - set_followers
no_sigues = set_followers - set_following
mutuos = set_followers & set_following

# ========= MENÚ =========

while True:
    print("\n📊 --- ANALIZADOR DE INSTAGRAM (LINKS LIMPIOS) ---")
    print("1. Ver resumen")
    print("2. Ver quién NO te sigue")
    print("3. Ver a quién NO sigues")
    print("4. Ver seguidores mutuos")
    print("5. Guardar resultados con LINKS CORREGIDOS en .txt")
    print("6. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        print(f"\n👥 Seguidores: {len(set_followers)}")
        print(f"➡️ Siguiendo: {len(set_following)}")
        print(f"❌ No te siguen: {len(no_te_siguen)}")
        print(f"🤔 No sigues: {len(no_sigues)}")
        print(f"✅ Mutuos: {len(mutuos)}")

    elif opcion == "2":
        mostrar_lista("❌ No te siguen", no_te_siguen)

    elif opcion == "3":
        mostrar_lista("🤔 Tú no sigues", no_sigues)

    elif opcion == "4":
        mostrar_lista("✅ Seguidores mutuos", mutuos)

    elif opcion == "5":
        # Usamos dict_following para los que no te siguen
        guardar_txt("no_te_siguen.txt", no_te_siguen, dict_following)
        # Usamos dict_followers para los que tú no sigues
        guardar_txt("no_sigues.txt", no_sigues, dict_followers)
        guardar_txt("mutuos.txt", mutuos, dict_following)
        print("\n💾 Archivos guardados. Los links ahora deberían funcionar correctamente.")

    elif opcion == "6":
        print("\n👋 ¡Hasta luego!")
        break
    else:
        print("\n❌ Opción inválida")