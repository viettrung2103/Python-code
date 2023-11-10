# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api
# . Your task is to write a program that asks the user for the name of a municipality and
# then prints out the corresponding weather condition description text and temperature
# in Celsius degrees. Take a good look at the API documentation. You must register for
# the service to receive the API key required for making API requests. Furthermore,
# find out how you can convert Kelvin degrees into Celsius.

# https: // openweathermap.org / api
import requests.exceptions
import json
import datetime as dt


private_key = "28e489100830be62a52cd6f528c12b6c"

#geo_request
# query_string = "London"

# geo_request =f"http://api.openweathermap.org/geo/1.0/direct?q={query_string}&limit=5&appid={private_key}"
# print(geo_request)

example_request = "http://api.openweathermap.org/geo/1.0/direct?limit=5&appid=28e489100830be62a52cd6f528c12b6c&q=London"
#weather request
# weather_request = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={private_key}"
# # https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}

def get_location(location_name):
    geo_request = (f"http://api.openweathermap.org/geo/1.0/"
                   f"direct?q={location_name}&limit=5&appid={private_key}")
    try:
    # response = requests.get(request)
        response = requests.get(geo_request).json()  #recommend way
        location =response[0]
        location_lon = location["lon"]
        location_lat = location["lat"]

        # print(json.dumps(response[0], indent=2))

        return [location_lon,location_lat]
    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")

def get_forecast_at_location(location_name):
    location_lon, location_lat = get_location(location_name)
    unit = "metric"
    # print(f"longitute: {location_lon} - latitute: {location_lat}")

    weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&appid={private_key}&units={unit}"
    try:
        # response = requests.get(request)
        response = requests.get(weather_request).json()  # recommend way
        # print(json.dumps(response,indent=2))

        weather = response["weather"][0]
        main_weather = weather["main"]
        description = weather["description"]

        main_temperature= response["main"]
        temp =  main_temperature["temp"]
        feels_like = main_temperature['feels_like']

        sys = response["sys"]
        sunrise = sys['sunrise']
        converted_sunrise = dt.datetime.fromtimestamp(sunrise).strftime('%A %d-%b-%Y, at: %H:%M:%S')

        sunset = sys['sunset']
        converted_sunset = dt.datetime.fromtimestamp(sunset).strftime('%A %d-%b-%Y, at: %H:%M:%S')



        # print(f"Weather: {weather}")
        print(f"Main Weather: {main_weather}")
        print(f"DescriptionL: {description}")

        # print(f"Main: {main_temperature}")
        print(f"Temperature: {temp}")
        print(f"Feel like: {feels_like}")

        # print(f"Sys: {sys}")
        # print(f"Sunrise: {sunrise}")
        #%A %d - %b - %Y, %H:%M:%S - Friday 01-Jan-1994, 06:30:30
        # converted_sunrice = dt.datetime.fromtimestamp(sunrise).strftime('%A %d-%b-%Y, at: %H:%M:%S')
        print(f"Sunrise: {converted_sunrise}")
        print(f"Sunset: {converted_sunset}")



        # print(json.dumps(response[0], indent=2))

        # return [location_lon, location_lat]
    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")


query_string = "London"


# location_lon, location_lat = get_location(query_string)
# print(f"longitute: {location_lon} - latitute: {location_lat}")
get_forecast_at_location(query_string)