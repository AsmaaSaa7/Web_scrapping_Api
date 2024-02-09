from fastapi import FastAPI, HTTPException
from cassandra.cluster import Cluster
from typing import List
from pydantic import BaseModel
import uvicorn
 
app = FastAPI()
cluster = Cluster(['cassandra'])
session = cluster.connect()
keyspace_name = "weather_db"
session.set_keyspace(keyspace_name)
 
class WeatherResponse(BaseModel):
    City_name: str
    weather: str
    description: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
 
@app.get("/weather", response_model=List[WeatherResponse])
async def response_weather(country: str):
    search_query = """
    SELECT * FROM weather_table WHERE country=%s ALLOW FILTERING;
    """
    try:
        response = session.execute(search_query, [country])
        result = []
        for row in response:
            result.append({
                'City_name': row.name,
                'weather': row.weather,
                'description': row.description,
                'temperature': row.temperature,
                'feels_like': row.feels_like,
                'humidity': row.humidity,
                'pressure': row.pressure
            })
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)