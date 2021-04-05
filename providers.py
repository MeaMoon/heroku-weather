import random

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

def get_provider_data(city, country):
    full_first_provider = (f"http://api.openweathermap.org/data/2.5/weather?appid=437b42c187bccd82ebfb061400bcc822&q={city},{country}")
    
    full_second_provider = (f"http://api.weatherstack.com/current?access_key=656cb2e892aa386b022104c13564ce8d&query={city},{country}")

    #third_provider_url = "http://api.weatherbit.io/v2.0/current"
    #third_provider_api = "fdfd1ebc45e94325a02e4675122f749f"
    full_third_provider = (f"http://api.weatherbit.io/v2.0/current?&city={city}&key=fdfd1ebc45e94325a02e4675122f749f")

    all_providers = [full_first_provider,full_second_provider,full_third_provider]
    
    chosen_one = random.choice(all_providers)
    return(chosen_one)

  
    
    