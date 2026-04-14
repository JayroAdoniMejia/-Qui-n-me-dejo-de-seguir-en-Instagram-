# 📊 Analizador de Seguidores de Instagram (Unfollowers Tool)

Una herramienta profesional en **Python** que te permite analizar tu cuenta de Instagram y descubrir:

- ❌ **Quién NO te sigue de vuelta**
- 🤔 **A quién NO sigues tú**
- ✅ **Seguidores mutuos**

Todo esto de forma **100% segura**, procesando tus datos localmente sin necesidad de ingresar tu usuario o contraseña, el programa unicamente analiza los archivos JSON de tus seguidores y seguidos(por lo que es totalmente seguro).

---

## 🚀 Características

- 🔒 **Privacidad Total** → No requiere login ni inicio de sesion ni acceso a APIs externas.
- ⚡ **Sin Frameworks** → Código puro de Python; no necesitas instalar librerías externas.
- 🎨 **Interfaz Colorida** → Menú visual en terminal con códigos de color ANSI.
- 🌐 **Reportes HTML Pro** → Genera páginas web locales con diseño moderno y enlaces directos a perfiles.
- 📱 **Diseño Responsivo** → Reportes compatibles con dispositivos móviles (Meta Viewport).

---

## 📁 Estructura del Proyecto

```text
📦 proyecto/
 ┣ 📄 unfollowers_pro.py
 ┣ 📄 followers_1.json
 ┣ 📄 following.json
 ┣ 📄 no_te_siguen.html  <-- Generado por el script
 ┣ 📄 mutuos.html        <-- Generado por el script
 ┗ 📄 README.md
```

---

## ⚙️ Requisitos

- Python 3.x

Puedes verificar tu versión con:

```bash
python --version
```

---

## 📥 Cómo obtener tus datos de Instagram

1. Ve a la **Configuración** de tu Instagram.
2. Entra en **Centro de cuentas → Tu información y permisos**.
3. Selecciona **Descargar tu información**.
4. Elige **Descarga parcial** y marca únicamente la opción **Seguidores y seguidos**.
5. Configuración del archivo:
   - Formato: **JSON** *(Obligatorio)*
   - Calidad: Media/Alta
   - Intervalo: Desde el principio *(cualquier fecha)*
6. Descarga y extrae el archivo `.zip` que Instagram te enviará por correo.

### 📌 Archivos necesarios

Dentro de la carpeta extraída, busca en `connections/followers_and_following/`:

- `followers_1.json`
- `following.json`

Cópialos a la misma carpeta donde tengas tu script `unfollowers_pro.py`.

---

## ▶️ Uso

Ejecuta el programa en la terminal con:

```bash
python unfollowers_pro.py
```

### 🖥️ Menú del programa

Al ejecutarlo verás una interfaz interactiva:

```
1. Ver resumen
2. Ver quién NO te sigue
3. Ver a quién NO sigues
4. Ver seguidores mutuos
5. Exportar Reportes HTML(recomendado)
6. Salir
```

---

## 📊 Reportes Visuales

Al seleccionar la opción **5**, el programa genera archivos `.html` con:


- **Instrucciones:** Guía visual *"👇 Click para ir a su perfil"*.
- **Instrucciones:** Guía visual *"👇 Lista de seguidores que no te siguen"*.
- **Instrucciones:** Guía visual *"te permite ir al perfil de quien no te sigue si dejarlo de seguir"*.


---

## 🧠 Cómo funciona

1. **Limpieza Dinámica:** El script procesa el JSON y reconstruye las URLs de Instagram eliminando las trabas de redirección del formato original.
2. **Lógica de Conjuntos:** Utiliza estructuras de `set()` para calcular diferencias simétricas en milisegundos.
3. **Generación de Plantillas:** Crea un documento HTML desde cero inyectando los datos procesados y estilos CSS embebidos para asegurar la portabilidad y cumplimiento de estándares web (Viewport).

---

## ⚠️ Importante

- **Seguridad:** Nunca uses aplicaciones que te pidan tu contraseña de Instagram. Este script es seguro porque tú controlas tus datos.
- **Privacidad:** Los reportes generados son archivos locales en tu PC; nadie más tiene acceso a ellos.

---

## 👨‍💻 Autor

Desarrollado por **Jayro Adoni Mejía**

---

## ⭐ Apoya el proyecto

Si te fue útil esta herramienta para gestionar tu comunidad, considera darle una ⭐ en GitHub.