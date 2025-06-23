import argparse
from weather import get_weather
from storage import save_to_csv


def main():
    parser = argparse.ArgumentParser(description="Pogodowy tracker")
    parser.add_argument('--city', '-c', required=True, help='Nazwa miasta')
    args = parser.parse_args()

    try:
        weather = get_weather(args.city)
        print(f"Pogoda w {weather['miasto']}: {weather['temperatura']}°C, {weather['opis']}")
        print(f"Wilgotność: {weather['wilgotność']}%, Wiatr: {weather['wiatr']} m/s")
        save_to_csv(weather)
        print("Dane zapisane do historii.")
    except ValueError as e:
        print(f"{e}")

if __name__ == "__main__":
    main()