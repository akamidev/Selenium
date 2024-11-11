# 🕵️‍♂️ Projet Selenium : Test d'Automatisation avec Google Search

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.26.1-green?style=for-the-badge&logo=selenium)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-130.0.6723.116-brightgreen?style=for-the-badge&logo=google-chrome)
![Status](https://img.shields.io/badge/Status-Actif-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

Ce projet utilise **Selenium** pour automatiser une recherche Google en utilisant le navigateur **Chrome**. Il ouvre Google, tape "Test Selenium" dans la barre de recherche, et soumet la recherche automatiquement.

---

### **📋 Fonctionnalités**

- **Automatisation** d'une recherche Google avec Selenium.
- Utilise **ChromeDriver** pour contrôler le navigateur Chrome.
- Gère les erreurs courantes (élément non interactif, temps d'attente dépassé).
- Supporte le mode **headless** (sans interface graphique).

---

### **🛠️ Prérequis**

- **Python 3.12** installé sur votre machine.
- **ChromeDriver** compatible avec votre version de Chrome (dans ce projet, la version utilisée est `130.0.6723.116`).
- Navigateur **Google Chrome** installé (version `130.0.6723.117`).
- Compte GitHub pour partager le projet.

---

### **📦 Installation**

1. **Clonez ce dépôt GitHub** :

   ```bash
   git clone https://github.com/votre-nom-utilisateur/selenium-google-search.git
   cd selenium-google-search
   ```

2. **Créez et activez un environnement virtuel** :

    ```bash
    Copy code
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Installez les dépendances** :

    ```bash
    pip install selenium
    ```
3. **Téléchargez ChromeDriver** et placez-le dans un dossier accessible (par exemple, C:/chromedriver-win64/). Ajoutez ce chemin au PATH de votre système.
   
 ### ⚙️ Configuration

Assurez-vous que le chemin vers ChromeDriver est correct dans le fichier test_selenium.py :

    ```bash
    chrome_service = Service("C:/chromedriver-win64/chromedriver.exe")
    ```
### 🚀 Utilisation

Exécutez le script avec la commande suivante :

```bash

python test_selenium.py
```

***Exemple de sortie*** :

```bash
Ouverture de Google...
Recherche de la barre de recherche...
La barre de recherche est trouvée et interactive.
Texte entré et recherche soumise.
Fermeture du navigateur.
```
Le navigateur s'ouvrira, effectuera la recherche, puis se fermera automatiquement.

### 📚 Ressources

Documentation officielle de Selenium
Télécharger ChromeDriver
Guide d'installation de Python

### 🤝 Contribuer
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à créer une pull request.

### 📄 Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](https://github.com/akamidev/Selenium/blob/main/LICENSE) pour plus de détails.

### ✨ Auteur
AKAMI Mehdi - [Portfolio](https://akamimehdi.netlify.app/)