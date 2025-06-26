import requests

API_KEY = #'Podaj swój klucz API'
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
        raise ValueError(f"Błąd: {data.get('message', 'Nieznany błąd')}")
    
    result = {
        'miasto': city.capitalize(),
        'temperatura': data['main']['temp'],
        'opis': data['weather'][0]['description'],
        'wilgotność': data['main']['humidity'],
        'wiatr': data['wind']['speed']
    }

    return result
