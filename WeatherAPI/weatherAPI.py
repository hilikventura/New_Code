import requests, sys
from flask import Flask
from flask import request
from flask import render_template
import random

web = Flask(__name__)
token = "a69377a15953c8ba9671e9b62b065644"
data = "<h1>ERROR</h1>"
is_random = True


def get_weather_data(_lat, _lon, _token):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={_lat}&lon={_lon}&appid={_token}&units=metric"
    r = requests.get(url)
    data = r.json()
    country = data['sys']['country'] if 'country' in data['sys'].keys() else ""
    return data['name'], country, str(data['weather'][0]['description']).title(), data['main']['temp']


def get_air_pollution_data(_lat, _lon, _token):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={_lat}&lon={_lon}&appid={_token}"
    r = requests.get(url)
    data = r.json()
    return data['list'][0]['main']['aqi']


def get_cood_from_user():
    lat = int(input("Please enter latitude: \n"))
    lon = int(input("Please enter longitude: \n"))
    while not (-90 <= lat <= 90 and -180 <= lon <= 180):
        print("Please Try again something went wrong \n(latitude -90 to 90\tlongitude -180 to 180)")
        lat = int(input("Please enter latitude: \n"))
        lon = int(input("Please enter longitude: \n "))
    return lat, lon


@web.route("/")
def output():
    global data
    if is_random:
        main(str(random.randint(-90, 90)), str(random.randint(-180, 180)))
    return data

    # return  render_template("index.html")


def main(lan="", lon=""):
    global data
    if lan != "" and lan != "":
        lan, lon = int(lan), int(lon)
        if -90 <= lan <= 90 and -180 <= lon <= 180:
            # lan, lon = get_cood_from_user()
            name, country, desc, temp = get_weather_data(lan, lon, token)
            aqi = get_air_pollution_data(lan, lon, token)
            data = f"""<div>
            <h1>Weather Data about {country} {name} ({lan},{lon}):</h1>
            <p>{desc}</p> 
            <h3>Air pollution quality: {aqi} </h3>
            <h3>The current temp is {temp}°C</h3>
            </div>"""
    else:
        data = "<h1>Bad Input</h1>"


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(list(sys.argv)[1], list(sys.argv)[2])
    else:
        is_random = True

    web.run(host="0.0.0.0", port=8000)
