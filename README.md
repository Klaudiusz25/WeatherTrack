# WeatherTrack
Aplikacja do śledzenia pogody w wybranych miastach. Dane są pobierane z API OpenWeatherMap i zapisywane lokalnie w pliku CSV, a następnie wizualizowane na wykresie temperatur.

# Funkcje
- Pobieranie aktualnej pogody dla wybranego miasta
- Tworzenie wykresu historii temperatur
- Zapisywanie danych do pliku CSV
- Możliwość automatycznego odświeżania danych (np. co godzinę)

# Użycie
Pobieranie pogody:
python main.py --city "Warszawa"

Wyświetlenie wykresu historii:
python main.py --city "Warszawa" --plot

Działa z polskimi znakami i spacjami, np.:
python main.py --city "Środa Wielkopolska" --plot

# Automatyzacja (Windows)
Aby dane były zbierane regularnie (np. co godzinę), możesz użyć Harmonogramu zadań w Windows:
1. Otwórz Harmonogram zadań
2. Wybierz „Utwórz zadanie podstawowe”
3. Wybierz „Codziennie” i ustaw godzinę startu
4. W sekcji „Akcja”:
   Program/skrypt: ścieżka do python.exe
   Argumenty: ścieżka do fetch_cron.py
5. Ustaw „Powtarzaj co 1 godzinę”
