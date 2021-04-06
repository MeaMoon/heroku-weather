from flask import Flask, render_template, request
import requests
from providers import get_provider_data
from providers import get_cities_by_provider
from providers import get_country_by_city

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/acquire_city', methods=['GET', 'POST'])
def acquire_city():
        if request.method == "POST":
            country = request.form['country']
            cities = get_cities_by_provider(country)
        return render_template("index.html", cities=cities)
    
@app.route('/acquire_city/show_weather', methods=['GET', 'POST'])
def show_weather():
    if request.method == "POST":
        city = request.form['city']
        country = get_country_by_city(city)
        
        random_provider = get_provider_data(city, country)
        weather_url = requests.get(random_provider)
        
        if "openweathermap" in random_provider:
            weather_data = weather_url.json()
            temp = int((weather_data['main']['temp'] - 273.15))
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            true_wind = round(wind_speed * 3.6, 2)
            
        elif "weatherstack" in random_provider:
            weather_data = weather_url.json()
            temp = int(weather_data['current']['temperature'])
            humidity = weather_data['current']['humidity']
            true_wind = weather_data['current']['wind_speed']
            
        else:
            weather_data = weather_url.json()
            temp = int(weather_data['data'][0]['temp'])
            humidity = weather_data['data'][0]['rh']
            wind_speed = weather_data['data'][0]['wind_spd']
            true_wind = round(wind_speed * 3.6, 2)

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=true_wind, city=city)
    
    return render_template("index.html")










