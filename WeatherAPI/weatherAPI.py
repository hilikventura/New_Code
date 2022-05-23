import requests,sys
from flask import Flask
from flask import request
from flask import render_template

web = Flask(__name__)
token = "a69377a15953c8ba9671e9b62b065644"
data="<h1>ERROR</h1>"

def get_weather_data(_lat, _lon, _token):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={_lat}&lon={_lon}&appid={_token}&units=metric"
    r = requests.get(url)
    data = r.json()
    return data['name'], str(data['weather'][0]['description']).title(), data['main']['temp']


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
    return data

    #return  render_template("index.html")



def main(lan="", lon=""):
    global data
    if lan!="" and lan!="":
        lan,lon=int(lan),int(lon)
        if -90 <= lan <= 90 and -180 <= lon <= 180:
            #lan, lon = get_cood_from_user()
            name, desc, temp = get_weather_data(lan, lon, token)
            aqi=get_air_pollution_data(lan, lon, token)
            data=f"\n<h1>Weather Data about {name}\n{desc}\nAir pollution quality: {aqi} \nThe current temp is {temp}°C</h1>"
    else:
        data="<h1>Bad Input</h1>"
    

if __name__ == "__main__":
    if len(sys.argv) == 3 :
        main(list(sys.argv)[1],list(sys.argv)[2])
        web.run(host="0.0.0.0", port=8000)

