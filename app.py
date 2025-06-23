from flask import Flask, render_template, request
from weather import get_weather
from storage import save_to_csv

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        try:
            weather = get_weather(city)
            save_to_csv(weather)
        except ValueError as e:
            error = str(e)

    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)