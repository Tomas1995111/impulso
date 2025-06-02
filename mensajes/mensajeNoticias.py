# mensajeNoticias.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from googlesearch import search
import time

def extraer_con_perfil(url, perfil_path):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
    options.add_argument(f"user-data-dir={perfil_path}")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10)

    paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.group p")
    resultados = []

    for p in paragraphs[1:-1]:
        texto = p.text.strip()
        lineas = texto.split("\n", 1)
        titulo = lineas[0].strip()
        contenido = lineas[1].strip() if len(lineas) > 1 else "(sin contenido)"
        resultados.append((titulo, contenido))

    driver.quit()
    return resultados

def generar_noticia_mercado():
    fecha = time.strftime("%Y/%m/%d/")
    query = f"site:cnbc.com {fecha} stocks making the biggest moves premarket"

    from googlesearch import search
    url_encontrada = None
    for url in search(query, num_results=5):
        if f"cnbc.com/{fecha}stocks-making-the-biggest-moves-premarket" in url:
            url_encontrada = url
            break

    if not url_encontrada:
        return "No se encontró el artículo de CNBC de hoy."

    perfil1 = r"C:\Users\Tomas\OneDrive\Escritorio\impulso_wsp_bot\PerfilesChrome\ChromeProfile_Normal"
    perfil2 = r"C:\Users\Tomas\OneDrive\Escritorio\impulso_wsp_bot\PerfilesChrome\ChromeProfile_Traductor"

    resultados_ingles = extraer_con_perfil(url_encontrada, perfil1)
    resultados_traducido = extraer_con_perfil(url_encontrada, perfil2)

    mensaje = "📊 *Muy buenos días Impuslores, les dejamos los mayores movimientos de acciones del día de hoy:* 📊\n\n"
    for i, (titulo, _) in enumerate(resultados_ingles):
        contenido = resultados_traducido[i][1] if i < len(resultados_traducido) else "(sin contenido)"
        mensaje += f"🔹 {titulo}:\n{contenido}\n\n"

    return mensaje.strip()
