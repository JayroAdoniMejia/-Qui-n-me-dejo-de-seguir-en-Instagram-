# 📊 Analizador de Seguidores de Instagram (Unfollowers Tool)

Una herramienta en **Python** que te permite analizar tu cuenta de Instagram y descubrir:

* ❌ Quién NO te sigue de vuelta
* 🤔 A quién NO sigues tú
* ✅ Seguidores mutuos

Todo esto de forma **segura**, sin necesidad de ingresar tu usuario o contraseña.

---

## 🚀 Características

* 🔒 **100% seguro** → No requiere login
* 🧠 Código simple y fácil de modificar y sin tener que instalar frameworks
* 📂 Funciona con datos oficiales exportados de Instagram
* 📊 Muestra estadísticas claras
* 📋 Listas ordenadas alfabéticamente
* 💾 Exporta resultados a archivos `.txt`


---

## 📁 Estructura del Proyecto

```
📦 proyecto/
 ┣ 📄 unfollowers_pro.py
 ┣ 📄 followers_1.json
 ┣ 📄 following.json
 ┗ 📄 README.md
```

---

## ⚙️ Requisitos

* Python 3.x

Puedes verificar tu versión con:

```bash
python --version
```

---

## 📥 Cómo obtener tus datos de Instagram

1. Ve a Configuración de Instagram
2. Entra en **Centro de cuentas**
3. Selecciona:

   * 👉 "Tu información y permisos"
   * 👉 "Descargar tu información(Solo selecciona la opcion Seguidores y seguidos)"
  
4. Elige:

   * Formato: **JSON**
   * Intervalo: **Cualquier fecha**
5. Descarga el archivo `.zip`
 * 👉 "Te caera un correo donde instagram te confirma la descarga"
6. Extrae los archivos
7. Veras una carpeta llamada "connections" y adentro otra carpeta llamada "followers_and_following"

---

## 📌 Archivos necesarios

Dentro del archivo descargado busca:

* `followers_1.json`
* `following.json`

Colócalos en la misma carpeta unfollowers_pro que debes crear para el script "unfollowers_pro.py".

---

## ▶️ Uso

Ejecuta el programa en la terminal con:

```bash
python unfollowers_pro.py
```

---

## 🖥️ Menú del programa

Al ejecutarlo verás:

```
1. Ver resumen
2. Ver quién NO te sigue
3. Ver a quién NO sigues
4. Ver seguidores mutuos
5. Guardar resultados en archivos .txt
6. Salir
```

---

## 📊 Ejemplo de salida

```
📊 RESUMEN
------------------------------
👥 Seguidores: 1185
➡️ Siguiendo: 650
❌ No te siguen: 320
🤔 No sigues: 855
✅ Mutuos: 330
```

---

## 💾 Exportación

El programa genera automáticamente:

* `no_te_siguen.txt`
* `no_sigues.txt`
* `mutuos.txt`

---

## 🧠 Cómo funciona

El script:

1. Lee los archivos JSON exportados
2. Extrae los nombres de usuario
3. Compara listas usando estructuras tipo `set`
4. Calcula diferencias e intersecciones

---

## ⚠️ Importante

* No uses aplicaciones externas que pidan tu contraseña
* Este método es seguro porque usa tus propios datos exportados
* Instagram cambia frecuentemente el formato de sus archivos, este script está adaptado para ello

---

## 🛠️ Posibles mejoras

* Interfaz gráfica (GUI)
* Filtros avanzados
* Integración con bases de datos
* Estadísticas más detalladas

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

Puedes hacer:

* Fork del proyecto
* Crear una rama
* Enviar un Pull Request

---

## 📜 Licencia

Este proyecto es de uso libre para fines educativos y personales.

---

## 👨‍💻 Autor

Desarrollado por **Jayro Adoni Mejía**

---

## ⭐ Apoya el proyecto

Si te fue útil, considera darle una ⭐ en GitHub 

---
