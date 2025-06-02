
# impulso_wsp_bot

Bot en Python para enviar mensajes programados a un grupo de WhatsApp, con información financiera y bursátil diaria.

---

## Estructura del proyecto

```
impulso_wsp_bot/
│
├── __pycache__/             # Cachés de Python (generados automáticamente)
├── PerfilesChrome/          # Perfiles de Chrome usados por Selenium
├── extras/                  # Scripts o utilidades auxiliares
├── mensajes/                # Scripts que generan los mensajes automáticos
│   ├── __init__.py
│   ├── mensajeCotizacionesDolar.py
│   ├── mensajeNoticias.py
│   └── mensajeAlertaCompra.py
├── envioWhatsapp.py         # Script principal que programa y envía los mensajes
├── chromedriver.exe         # Driver para Selenium
├── .gitignore               # Archivos a ignorar por Git
└── README.md                # Este archivo
```

---

## Descripción

El bot envía mensajes automáticos a un grupo de WhatsApp en horarios y días específicos, incluyendo:

- Noticias del mercado financiero (extraídas con Selenium y scraping)
- Cotización del dólar
- Alertas bursátiles aleatorias
- Mensajes especiales en fechas definidas

---

## Dependencias

- Python 3.8+
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- pyautogui
- pyperclip
- selenium
- googlesearch-python

Se recomienda instalar todo con:

```bash
pip install -r requirements.txt
```

---

## Uso

1. Configurar el nombre del grupo WhatsApp en `envioWhatsapp.py` en la variable `nombre_grupo`.
2. Ajustar los horarios y días en las listas `mensajes_semana` y `mensajes_fecha`.
3. Configurar los perfiles de Chrome para Selenium en `mensajes/mensajeNoticias.py`.
4. Ejecutar el script principal:

```bash
python envioWhatsapp.py
```

---

## Notas importantes

- Se usa **pywhatkit** para abrir WhatsApp Web y **pyautogui** para pegar y enviar los mensajes.
- Para el scraping de noticias se utiliza **Selenium** con perfiles de Chrome para obtener contenido traducido.
- Asegurate de tener `chromedriver.exe` compatible con tu versión de Chrome.
- El bot debe ejecutarse en un ambiente con acceso a la interfaz gráfica para que pyautogui funcione bien.

---

## Mejoras pendientes

- Manejo de errores y reconexión automática.
- Logs más detallados.
- Archivo de configuración externo para horarios y mensajes.
- Automatizar la actualización del driver de Chrome.

---

## Autor

Tomás Arriola
