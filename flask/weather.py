import requests
from datetime import datetime

appid = "fe110878ac5b12fcb687053a9d1e927a"


def request_current_weather(city_id = "Minsk"):
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
            params={'q': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    return "Weather forecast today:<br> city:{}<br> conditions:{}<br> temp:{}".format(data['name'], data['weather'][0]['main'],data['main']['temp'] )

def request_forecast_weather(city_id = "Minsk"):
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
            params={'q': city_id,'units': 'metric', 'lang': 'ru', 'cnt':40, 'APPID': appid})
    data = res.json()
    forecast = "Weather forecast for next 5 days:<br> "
    forecast +=  "city: {}<br> ".format(data['city']["name"])
    past_date = str()
    for i in data['list']:
        if datetime.fromtimestamp(i['dt']).strftime("%d %B, %Y") == past_date:
            pass
        else:
            forecast += "-_-_-"*5+"<br>"
            forecast += "  date: {} <br>".format(datetime.fromtimestamp(i['dt']).strftime("%d %B, %Y"))
            forecast += "  temp: {} <br>".format(i['main']['temp'])
            forecast += "  condition{} <br>".format(i['weather'][0]["main"])
        past_date = datetime.fromtimestamp(i['dt']).strftime("%d %B, %Y")
    return (forecast)

print(request_forecast_weather())
