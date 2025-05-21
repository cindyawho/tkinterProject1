import requests # type: ignore # pip install requests.
import json
def get_weather(one,two, three):
    response = requests.get(f'https://api.weather.gov/gridpoints/{three}/{one},{two}/forecast')
    data = response.json()
    return data["properties"]['periods'][0]['temperature'], data["properties"]['periods'][0]['detailedForecast'], data["properties"]['periods'][0]['probabilityOfPrecipitation']['value']