import csv
import os
from datetime import datetime

DATA_PATH = 'data/history.csv'

def save_to_csv(weather_data):
    os.makedirs('data', exist_ok=True)
    file_exists = os.path.isfile(DATA_PATH)

    with open(DATA_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['data', 'miasto', 'temperatura', 'opis', 'wilgotność', 'wiatr'])

        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M'),
            weather_data['miasto'],
            weather_data['temperatura'],
            weather_data['opis'],
            weather_data['wilgotność'],
            weather_data['wiatr']
        ])