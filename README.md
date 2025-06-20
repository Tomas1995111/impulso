# impulso_wsp_bot

Bot en Python para enviar mensajes automáticos a un grupo de WhatsApp con contenido financiero personalizado. Incluye alertas, cotizaciones, noticias del mercado y reportes diarios o por fecha.

---

## ⚙️ Funcionalidad

El bot envía automáticamente mensajes a WhatsApp en horarios programados. Algunas de sus funciones principales:

- 📈 **Alertas bursátiles** aleatorias (acciones locales y del exterior)
- 💵 **Cotización del dólar** scrapeada desde sitios web financieros
- 🗞️ **Resumen de noticias** traducidas usando Selenium y Google
- 📊 **Reporte automatizado** cargado en Google Sheets
- 📆 **Mensajes especiales** por fechas predefinidas

Todo se configura desde el archivo `envioWhatsapp.py`.

---


## Estructura del proyecto

```
impulso_wsp_bot/
├── envioWhatsapp.py # Script principal del bot
├── chromedriver.exe # Driver Chrome para Selenium
├── requirements.txt # Dependencias del proyecto
├── README.md # Documentación
├── log_envioWhatsapp.log # Log de actividad del bot
├── PyWhatKit_DB.txt # Registro interno de pywhatkit (puede eliminarse si no se usa más)
│
├── mensajes/ # Lógica para generar cada tipo de mensaje
│ ├── mensajeAlertaCompra.py
│ ├── mensajeAlertaCompraArg.py
│ ├── mensajeCotizacionesDolar.py
│ ├── mensajeResumen.py
│ ├── reporteAlertas.py
│ └── credenciales.json # Acceso a Google Sheets (no compartir)
│
├── extras/ # Scripts secundarios o utilitarios
│ ├── enviardocumento.py
│ └── index.html

├── PerfilesChrome/ # Perfiles Chrome usados para automatizar
├── pycache/ # Caché de compilación de Python
```

---


## 🧰 Requisitos

- Python 3.8 o superior
- Navegador Google Chrome
- Tener escaneado el QR de WhatsApp Web en el perfil de Chrome usado por Selenium
- Tener `chromedriver.exe` compatible con la versión de Chrome

---

## ▶️ Uso

1. Cloná el proyecto o descargalo en tu máquina.
2. Instalá las dependencias con:

```bash
pip install -r requirements.txt
```

3. Configurá el grupo de destino y los horarios en `envioWhatsapp.py`.
4. Ejecutá el bot:

```bash
python envioWhatsapp.py
```

El bot quedará corriendo en segundo plano y enviará los mensajes según el cronograma.

---

## 📦 Dependencias

El proyecto requiere las siguientes librerías de Python:

- `yfinance`
- `gspread`
- `oauth2client`
- `requests`
- `beautifulsoup4`
- `selenium`
- `googlesearch-python`

Instalalas ejecutando:

```bash
pip install -r requirements.txt
```

---

## 🚀 Mejoras futuras

- Ejecutar el bot 100% headless (requiere cambiar la forma de envío de mensajes)
- Integrar archivo `.env` para mover configuraciones sensibles
- Cargar los horarios y tipos de mensajes desde Google Sheets
- Implementar logs detallados con más control de errores

---

## 👨‍💻 Autor

**Tomás Arriola**  
Proyecto orientado a automatizar el envío de información bursátil y ayudar a democratizar el acceso a contenido financiero en Argentina.
