from flask import Flask, render_template, request
import requests
#import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "437b42c187bccd82ebfb061400bcc822"

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}')

        weather_data = weather_url.json()

        temp = int((weather_data['main']['temp'] - 273.15))
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        true_wind = round(wind_speed * 3.6, 2)

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=true_wind, city=city)

    return render_template("index.html")