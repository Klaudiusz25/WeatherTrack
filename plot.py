import csv
import matplotlib.pyplot as plt
from datetime import datetime

def plot_temperature_history(city):
    timestamps = []
    temperatures = []

    try:
        with open("data/history.csv", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['miasto'].lower() == city.lower():
                    dt = datetime.strptime(row['data'], "%Y-%m-%d %H:%M")
                    temp = float(row['temperatura'])
                    timestamps.append(dt)
                    temperatures.append(temp)
    except FileNotFoundError:
        print("Plik history.csv nie istnieje.")
        return
    if not timestamps:
        print(f"Brak danych dla miasta: {city}")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='dodgerblue')
    plt.title(f"Zmiany temperatury w {city.capitalize()}")
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

def save_plot_to_file(city, filename):

    timestamps = []
    temperatures = []

    try:
        with open("data/history.csv", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row = {k.lower(): v for k, v in row.items()}
                if row['miasto'].lower() == city.lower():
                    dt = datetime.strptime(row['data'], "%Y-%m-%d %H:%M")
                    temp = float(row['temperatura'])
                    timestamps.append(dt)
                    temperatures.append(temp)
    except FileNotFoundError:
        return False

    if not timestamps:
        return False

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='dodgerblue')
    plt.title(f"Temperatura w {city.capitalize()} (historia)")
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return True