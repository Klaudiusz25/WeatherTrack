import requests

API_KEY = '0589da42efecdaa571ee6e516ec179f3'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pl'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200 or data.get("cod") != 200:
        print(f"Błąd: {data.get('message', 'Nieznany błąd')}")
        return
    
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"Pogoda w {city.capitalize()}:")
    print(f"Temperatura: {temp}°C")
    print(f"Opis: {description}")
    print(f"Wilgotność: {humidity}%")
    print(f"Wiatr: {wind_speed} m/s")

if __name__ == "__main__":
    city_name = input("Podaj miasto: ")
    get_weather(city_name)