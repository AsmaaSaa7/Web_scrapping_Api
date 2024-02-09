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

- `docker-compose.yml`: Fichier de configuration Docker Compose pour lancer les 3 services (web scraping et CASSANDRA et API) simultanément.

# Utilisation

1. **Web Scraping (crawler)**:
   - Assurez-vous que Docker est installé sur votre système.
   - Exécutez `docker-compose up` pour construire l'image Docker et lancer le scraping des données météorologiques.
   - Le fichier `docker-compose.yml` contient la configuration Docker Compose pour lancer les 3 services (web scraping, Cassandra et API) simultanément.

2. **Cassandra**:
   - L'instance de Cassandra sera également lancée en utilisant Docker Compose lors de l'exécution de `docker-compose up`. Aucune action supplémentaire n'est requise pour la configuration.

3. **API OpenWeather**:
   - Une fois que les services Docker sont en cours d'exécution, l'API OpenWeather sera accessible.
   - Assurez-vous que l'adresse et le port de l'API sont corrects selon la configuration dans le fichier `main.py`.
     

## Exemple d'utilisation avec Docker Compose

1. Assurez-vous que Docker est installé sur votre système.
2. Naviguez jusqu'au répertoire contenant le fichier `docker-compose.yml`.
3. Exécutez la commande suivante dans votre terminal : docker-compose up
4. Attendez que les services se construisent et se lancent. Une fois terminé, vous devriez voir des messages indiquant que les services sont prêts à être utilisés.
5. Vous pouvez maintenant accéder à l'API OpenWeather via l'adresse spécifiée http://localhost:8080/weather?country=FR` et commencer à récupérer les données météorologiques.




## Captures d'écran

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
