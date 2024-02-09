# Projet de Web Scraping & API OpenWeather

Ce projet est une application de web scraping et d'API OpenWeather développée avec VS Code réalisé par Mohamed REDA TARAOUI , Illana TARTOUR, Asmaa SAADAOUI. Il est conçu pour récupérer des données météorologiques à partir du site web et fournir une API pour accéder à ces données.

## Structure du dossier

- `crawler/`: Contient les scripts de web scraping.
  - `crawler.py`: Script principal pour le scraping des données météorologiques.
  - `requirements.txt`: Fichier des dépendances Python.
  - `Dockerfile`: Configuration pour Docker.
  - `init_db`: Script d'initialisation de la base de données.
  - `current.city.list.json`: Fichier JSON des données sur les villes actuelles.

- `Api/`: Contient les fichiers pour l'API OpenWeather.
  - `main.py`: Script principal pour l'API OpenWeather.
  - `requirements.txt`: Fichier des dépendances Python.
  - `Dockerfile`: Configuration pour Docker.

- `docker-compose.yml`: Fichier de configuration Docker Compose pour lancer les deux services (web scraping et API) simultanément.

## Utilisation

1. **Web Scraping (crawler)**:
   - Assurez-vous que Docker est installé sur votre système.
   - Exécutez `docker build -t web_scraper crawler/` pour construire l'image Docker.
   - Exécutez `docker run -v $(pwd)/crawler:/app -it web_scraper` pour lancer le scraping des données météorologiques.

2. **API OpenWeather**:
   - Assurez-vous que Docker est installé sur votre système.
   - Exécutez `docker build -t openweather_api Api/` pour construire l'image Docker.
   - Exécutez `docker run -p 5000:5000 openweather_api` pour lancer l'API OpenWeather.

## Captures d'écran

### Web Scraping
![Capture d'écran du script de scraping](screenshots/crawler_script.png)
*Figure 1: Capture d'écran du script de web scraping.*

### API OpenWeather
![Capture d'écran de l'API OpenWeather en cours d'exécution](screenshots/api_running.png)
*Figure 2: Capture d'écran de l'API OpenWeather en cours d'exécution.*

## Notes supplémentaires

- Assurez-vous d'avoir une connexion Internet active pour le scraping des données météorologiques.
- L'API OpenWeather nécessite une clé d'API valide, assurez-vous de configurer cette clé dans le fichier `main.py` avant de lancer l'API.

![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/a1c6436c-cbdb-40fe-ad44-d0f80accc0a4)
