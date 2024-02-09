from time import sleep
from init_db import init_db
import requests
import json
from cassandra.cluster import Cluster
import uuid
 

 
WEATHER_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = 'dd21a638583cc4d8d17e6e7b24b70348'
CITIES_DATA_FILE = 'city.list.json'
 
def fetch_weather_for_city(city_identifier: int):
    api_response = requests.get(WEATHER_API_ENDPOINT, params={'id': city_identifier, 'appid': API_KEY})
    return api_response.json()
 
def retrieve_city_ids():
    with open(CITIES_DATA_FILE, 'r') as file_handle:
        cities_data = json.load(file_handle)
        french_city_ids = [city['id'] for city in cities_data if city['country'] == "FR"]
        return french_city_ids
 
def persist_weather_data(session, weather_data):
    insert_query = """
    INSERT INTO weather_table (id, name, weather, description, temperature, feels_like, humidity, pressure, country)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    session.execute(insert_query, (
        weather_data['id'],
        weather_data['name'],
        weather_data['weather'],
        weather_data['description'],
        weather_data['temperature'],
        weather_data['feels_like'],
        weather_data['humidity'],
        weather_data['pressure'],
        weather_data['country']
    ))
 
french_cities_ids = retrieve_city_ids()
collected_weather_info = []
for city_id in french_cities_ids[0:100]:
    city_weather = fetch_weather_for_city(city_id)
    collected_weather_info.append({
        'id': city_weather['id'],
        'name': city_weather['name'],
        'weather': city_weather['weather'][0]['main'],
        'description': city_weather['weather'][0]['description'],  # Correction pour correspondre à la description plutôt que 'main'
        'temperature': city_weather['main']['temp'],
        'feels_like': city_weather['main']['feels_like'],
        'humidity': city_weather['main']['humidity'],
        'pressure': city_weather['main']['pressure'],
        'country': city_weather['sys']['country']
    })
 
# Connexion à Cassandra
cluster = Cluster(['cassandra'])  # Remplacez 'adresse_ip_cassandra' par l'adresse IP de votre cluster Cassandra
session = cluster.connect()
keyspace_name = "weather_db"  # Assurez-vous que le keyspace existe ou est créé par setup_database
init_db(session, keyspace_name)  # Cette ligne peut être commentée une fois que le keyspace et la table sont déjà configurés
session.set_keyspace(keyspace_name)
 
for weather_data in collected_weather_info:
    print('Insertion dans la base de données : ', weather_data['id'])
    persist_weather_data(session, weather_data)
 
session.shutdown()
cluster.shutdown()