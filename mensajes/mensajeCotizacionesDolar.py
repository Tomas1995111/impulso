#scrapCotizaciones.py
import requests
from bs4 import BeautifulSoup

def generar_cotizacion_dolar():
    url = "https://www.cronista.com/MercadosOnline/dolar.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"[!] Error al obtener cotizaciones: {e}"

    soup = BeautifulSoup(response.text, "html.parser")
    tablas = soup.find_all("table", {"id": ["market-scrll-2", "market-scrll-4"]})
    datos = []

    for tabla in tablas:
        filas = tabla.find_all("tr")
        for fila in filas:
            nombre_tag = fila.find("td", class_="name")
            compra_tag = fila.find("td", class_="buy")
            venta_tag = fila.find("td", class_="sell")

            if nombre_tag and compra_tag and venta_tag:
                nombre = nombre_tag.get_text(strip=True).split('Ingres')[0].strip()
                compra = compra_tag.get_text(strip=True).replace("Compra", "").replace("$", "").replace(".", "").replace(",", ".").strip()
                venta = venta_tag.get_text(strip=True).replace("Venta", "").replace("$", "").replace(".", "").replace(",", ".").strip()

                try:
                    datos.append((nombre, float(compra), float(venta)))
                except ValueError:
                    print(f"Error convirtiendo valores para {nombre}")

    def formato_arg(num):
        return f"{num:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    emojis = {
        "Dólar BNA": "🇦🇷",
        "Dólar Blue": "💸",
        "Dólar MEP": "📈",
        "Dólar Mayorista": "🏦",
        "Dólar CCL": "🌐",
        "Dólar Turista": "✈️"
    }

    def buscar_emoji(nombre):
        nombre_limpio = nombre.lower().strip()
        for clave, emoji in emojis.items():
            if clave.lower() == nombre_limpio:
                return emoji
        return ""

    mensaje = "💵 *Cotizaciones del Dólar* 💵\n\n"

    for nombre, compra, venta in datos:
        emoji = buscar_emoji(nombre)
        compra_fmt = formato_arg(compra)
        venta_fmt = formato_arg(venta)
        mensaje += f"{emoji} *{nombre}*\nCompra: ${compra_fmt} | Venta: ${venta_fmt}\n\n"

    return mensaje

if __name__ == "__main__":
    print(generar_cotizacion_dolar())
