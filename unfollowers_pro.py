import json
import os
from datetime import datetime

# ========= CONFIGURACIÓN DE COLORES (ANSI - SIN LIBRERÍAS) =========
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ========= FUNCIONES =========

def extraer_datos(data, es_following=False):
    """
    Extrae un diccionario {usuario: enlace_limpio} de los JSON de Instagram.
    Soluciona el error de redirección de los enlaces /_u/.
    """
    usuarios_dict = {}
    fuente = data.get("relationships_following", []) if es_following else data
    
    for user in fuente:
        username_fallback = user.get("title")
        for item in user.get("string_list_data", []):
            username = item.get("value") or username_fallback
            link_original = item.get("href", "")
            
            if "/_u/" in link_original:
                user_clean = link_original.split("/_u/")[-1]
                link_final = f"https://www.instagram.com/{user_clean}/"
            elif link_original:
                link_final = link_original if link_original.endswith("/") else f"{link_original}/"
            else:
                link_final = "Enlace no disponible"

            if username:
                usuarios_dict[username] = link_final
    return usuarios_dict

def generar_reporte_html(nombre_archivo, lista_claves, diccionario_fuente, titulo_reporte, color_base):
    """Genera una página web atractiva con estándares modernos de seguridad y viewport"""
    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    filas_html = ""
    for u in sorted(lista_claves):
        link = diccionario_fuente.get(u, "#")
        filas_html += f'<a href="{link}" target="_blank" rel="noopener" class="user-link">@{u}</a>'

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo_reporte}</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; padding: 20px; }}
            .container {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 100%; max-width: 500px; }}
            h1 {{ color: {color_base}; border-bottom: 2px solid #eee; padding-bottom: 15px; margin-top: 0; }}
            .stats {{ color: #65676b; font-size: 0.9em; margin-bottom: 15px; }}
            .instruction {{ color: {color_base}; font-weight: bold; font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; display: block; }}
            .user-link {{ display: block; padding: 12px; margin: 8px 0; text-decoration: none; color: #1c1e21; background: #f8f9fa; border-radius: 8px; transition: all 0.2s; font-weight: 500; overflow-wrap: break-word; }}
            .user-link:hover {{ background: {color_base}; color: white; transform: translateX(10px); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{titulo_reporte}</h1>
            <p class="stats">📅 {fecha_actual} | 👥 Total: {len(lista_claves)}</p>
            <span class="instruction">👇 Click para ir a su perfil:</span>
            {filas_html}
        </div>
    </body>
    </html>
    """
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(html_content)

# ========= CARGA DE DATOS =========

os.system('cls' if os.name == 'nt' else 'clear')
logo = f"""{MAGENTA}{BOLD}
  ___ _  _ ___ _____ _    ___ ___   _   __  __ 
 |_ _| \| / __|_   _/_\  / __| _ \ /_\ |  \/  |
  | || .` \__ \ | |/ _ \ \__ \   // _ \| |\/| |
 |___|_|\_|___/ |_/_/ \_\|___/_|_/_/ \_\_|  |_|
{RESET}"""
print(logo)

try:
    with open("followers_1.json", "r", encoding="utf-8") as f:
        followers_data = json.load(f)
    with open("following.json", "r", encoding="utf-8") as f:
        following_data = json.load(f)
except FileNotFoundError:
    print(f"{RED}❌ Error: No se encontraron los archivos JSON en la carpeta.{RESET}")
    input("Presiona ENTER para salir...")
    exit()

dict_followers = extraer_datos(followers_data)
dict_following = extraer_datos(following_data, es_following=True)
diccionario_maestro = {**dict_followers, **dict_following}

set_followers = set(dict_followers.keys())
set_following = set(dict_following.keys())

# ========= CÁLCULOS =========
no_te_siguen = set_following - set_followers
no_sigues = set_followers - set_following
mutuos = set_followers & set_following

# ========= MENÚ =========

while True:
    print(f"\n{CYAN}{BOLD}📊 --- ANALIZADOR DE INSTAGRAM PRO ---{RESET}")
    print(f"1. {BOLD}Ver resumen{RESET}")
    print(f"2. {RED}Ver quién NO te sigue{RESET}")
    print(f"3. {YELLOW}Ver a quién NO sigues{RESET}")
    print(f"4. {GREEN}Ver seguidores mutuos{RESET}")
    print(f"5. {BOLD}Exportar Reportes HTML(Sugerido){RESET}")
    print(f"6. Salir")

    opcion = input(f"\n{BOLD}Elige una opción: {RESET}")

    if opcion == "1":
        print(f"\n{BOLD}📈 RESUMEN DE CUENTA{RESET}")
        print("-" * 25)
        print(f"👥 Seguidores: {len(set_followers)}")
        print(f"➡️ Siguiendo:  {len(set_following)}")
        print(f"❌ {RED}No te siguen: {len(no_te_siguen)}{RESET}")
        print(f"🤔 {YELLOW}No sigues:    {len(no_sigues)}{RESET}")
        print(f"✅ {GREEN}Mutuos:       {len(mutuos)}{RESET}")

    elif opcion == "2":
        print(f"\n{RED}{BOLD}❌ USUARIOS QUE NO TE SIGUEN ({len(no_te_siguen)}):{RESET}")
        for u in sorted(no_te_siguen): print(f"  • @{u}")

    elif opcion == "5":
        print(f"\n{CYAN}Generando reportes HTML profesionales...{RESET}")
        generar_reporte_html("no_te_siguen.html", no_te_siguen, diccionario_maestro, "No te siguen", "#e4405f")
        generar_reporte_html("mutuos.html", mutuos, diccionario_maestro, "Seguidores Mutuos", "#3897f0")
        print(f"{GREEN}✅ ¡Éxito! Reportes HTML listos. (TXT desactivado){RESET}")

    elif opcion == "6":
        print(f"\n{MAGENTA}👋 ¡Hasta luego!{RESET}")
        break
    else:
        print(f"{RED}❌ Opción inválida{RESET}")