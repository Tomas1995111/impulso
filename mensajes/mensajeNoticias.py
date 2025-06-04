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

def buscar_url_noticia():
    fecha = time.strftime("%Y/%m/%d")
    fecha = "2025/05/30"
    query = f"site:cnbc.com {fecha} stocks making the biggest premarket"
    
    for url in search(query, num_results=15):
        if (
            f"cnbc.com/{fecha}" in url and
            "stocks-making-the-biggest" in url and
            "premarket" in url and
            "midday" not in url and
            "after-hours" not in url
        ):
            print(f"URL encontrada: {url}")
            return url

    print("No se encontró el artículo")
    return None

def generar_noticia_mercado():
    url = buscar_url_noticia()
    if not url:
        return ""

    perfil1 = r"C:\Users\Tomas\OneDrive\Escritorio\impulso_wsp_bot\PerfilesChrome\ChromeProfile_Normal"
    perfil2 = r"C:\Users\Tomas\OneDrive\Escritorio\impulso_wsp_bot\PerfilesChrome\ChromeProfile_Traductor"

    resultados_ingles = extraer_con_perfil(url, perfil1)
    resultados_traducido = extraer_con_perfil(url, perfil2)

    mensaje = "📊 *Muy buenos días Impuslores, les dejamos los mayores movimientos de acciones del día de hoy:* 📊\n\n"
    for i, (titulo, _) in enumerate(resultados_ingles):
        contenido = resultados_traducido[i][1] if i < len(resultados_traducido) else "(sin contenido)"
        mensaje += f"🔹 {titulo}:\n{contenido}\n\n"

    return mensaje.strip()
