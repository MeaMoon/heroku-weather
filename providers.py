import random
import requests

first_provider_url = "http://api.openweathermap.org/data/2.5/weather"
first_provider_api = "437b42c187bccd82ebfb061400bcc822"
full_first_provider = "http://api.openweathermap.org/data/2.5/weather?appid={437b42c187bccd82ebfb061400bcc822}&q={city},{country}"

second_provider_url = "http://api.weatherstack.com/current"
second_provider_api = "656cb2e892aa386b022104c13564ce8d"
full_second_provider = "https://api.weatherstack.com/current?access_key={656cb2e892aa386b022104c13564ce8d}&query={city},{country}"

third_provider_url = "http://api.weatherbit.io/v2.0/current"
third_provider_api = "fdfd1ebc45e94325a02e4675122f749f"
full_third_provider = "http://api.weatherbit.io/v2.0/current?&city={city}&key=fdfd1ebc45e94325a02e4675122f749f"

all_providers = [full_first_provider,full_second_provider]

city_provider_url = "https://countriesnow.space/api/v0.1/countries"

def get_cities_by_provider(chosen_country):
    url = "https://countriesnow.space/api/v0.1/countries"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    countries_data = response.json()
    searchable_country = countries_data['data']
    found_cities = None
    
    for countries in searchable_country:
        if countries['country'] == chosen_country:
            found_cities = countries
            break
    all_cities = found_cities['cities']
    return(all_cities)

bbb = get_cities_by_provider("Ukraine")

def get_country_by_city(chosen_city):
    url = "https://countriesnow.space/api/v0.1/countries"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    cities_data = response.json()
    searchable_city = cities_data['data']
    found_country = None
    
    for cities in searchable_city:
        if chosen_city in cities['cities']:
            found_country = cities
            break
    true_country = found_country['country']
    return(true_country)

ccc = get_country_by_city("Aleksandriya")


def get_provider_data(city, country):
    full_first_provider = (f"http://api.openweathermap.org/data/2.5/weather?appid=437b42c187bccd82ebfb061400bcc822&q={city},{country}")
    full_second_provider = (f"http://api.weatherstack.com/current?access_key=656cb2e892aa386b022104c13564ce8d&query={city},{country}")
    full_third_provider = (f"http://api.weatherbit.io/v2.0/current?city={city}&key=fdfd1ebc45e94325a02e4675122f749f")

    all_providers = [full_first_provider,full_second_provider,full_third_provider]
    
    chosen_one = random.choice(all_providers)
    return(chosen_one)

  
    
    