from flask import Flask, render_template, request
import requests
from providers import get_provider_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        random_provider = get_provider_data(city, country)

        weather_url = requests.get(random_provider)
        
        if "openweathermap" in random_provider:
            weather_data = weather_url.json()
            temp = int((weather_data['main']['temp'] - 273.15))
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            true_wind = round(wind_speed * 3.6, 2)
            
        else:
            weather_data = weather_url.json()
            temp = int(weather_data['current']['temperature'])
            humidity = weather_data['current']['humidity']
            true_wind = weather_data['current']['wind_speed']
            
#        else:
#            weather_data = weather_url.json()
#            temp = int(weather_data['data']['temp'])
#            humidity = weather_data['data']['rh']
#            wind_speed = weather_data['data']['wind_spd']
#            true_wind = round(wind_speed * 3.6, 2)

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=true_wind, city=city)

    return render_template("index.html")