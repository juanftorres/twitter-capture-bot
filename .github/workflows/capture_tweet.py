import time
from datetime import datetime
from playwright.sync_api import sync_playwright

# 👉 Sustituye este valor por el nombre de usuario de la cuenta que quieres vigilar (sin @)
TWITTER_USERNAME = "jjggrr89"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def capture_latest_tweet():
    url = f"https://twitter.com/{TWITTER_USERNAME}"
    timestamp = get_timestamp()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Cargar la cuenta de Twitter
        page.goto(url)

        # Esperar a que cargue al menos un tuit
        page.wait_for_selector("article", timeout=15000)

        # Seleccionar el primer tuit visible
        tweet = page.query_selector("article")

        # Hacer la captura de pantalla del tuit
        tweet.screenshot(path=f"tweet_{timestamp}.png")
        print(f"✅ Captura guardada como tweet_{timestamp}.png")

        browser.close()

if __name__ == "__main__":
    capture_latest_tweet()
