from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import time

# Configuration du service ChromeDriver
chrome_service = Service("C:/chromedriver-win64/chromedriver.exe")

# Options du navigateur Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Évite la détection par Google
# chrome_options.add_argument("--headless")  # Décommenter pour activer le mode headless

# Initialiser le navigateur
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # Ouvrir une page web pour tester
    driver.get("https://www.google.com")

    # Solution 1 : Attendre que l'élément soit cliquable
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
    except TimeoutException:
        print("L'élément n'a pas pu être localisé dans le temps imparti.")
        driver.quit()
        exit()

    # Solution 2 : Attendre un peu plus longtemps
    time.sleep(2)  # Attendre 2 secondes supplémentaires

    # Solution 3 : Scroll vers l'élément avant d'interagir
    driver.execute_script("arguments[0].scrollIntoView();", search_box)

    # Solution 4 : Vérifier si l'élément est visible et interactif
    if search_box.is_displayed() and search_box.is_enabled():
        # Solution 5 : Envoyer le texte avec JavaScript
        driver.execute_script("arguments[0].value = 'Test Selenium';", search_box)
        search_box.submit()
    else:
        print("L'élément n'est pas interactif.")

except ElementNotInteractableException:
    print("Erreur : L'élément n'est pas interactif.")
except TimeoutException:
    print("Erreur : Temps d'attente dépassé.")
finally:
    # Fermer le navigateur après quelques secondes
    time.sleep(2)  # Attendre avant de fermer le navigateur
    driver.quit()
