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
![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/b0578925-2438-4786-8afd-487aed9e1a38)
### Web Scraping

![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/06d3d702-a64f-4b58-a4e4-cf26e4240131)

*Figure 1: Capture d'écran du script sur VS CODE de  notre projet web scraping.*

### API OpenWeather
![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/36a483f7-ef14-4fe9-b9a1-4990087983f0)

*Figure 2: Capture d'écran de  résultatl'API OpenWeather en cours d'exécution.*

## Notes supplémentaires

- L'API OpenWeather nécessite une clé d'API valide, assurez-vous de configurer cette clé dans le fichier `main.py` avant de lancer l'API.
![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/50cf57b4-a303-44fc-b515-25ee437a782f)
![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/de998997-ad3f-4bd1-9b13-72dd7f31cff5)

![image](https://github.com/AsmaaSaa7/Web_scrapping_Api/assets/118186795/a1c6436c-cbdb-40fe-ad44-d0f80accc0a4)
