import os
from flask import Flask, render_template, request
from weather import get_weather
from storage import save_to_csv
from plot import save_plot_to_file

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    weather = None
    error = None
    plot_path = None

    if request.method == 'POST':
        city = request.form.get('city')
        try:
            weather = get_weather(city)
            save_to_csv(weather)

            # Ścieżka do pliku wykresu
            filename = f'static/plot.png'
            if save_plot_to_file(city, filename):
                plot_path = filename
        except ValueError as e:
            error = str(e)

    return render_template('index.html', weather=weather, error=error, plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)