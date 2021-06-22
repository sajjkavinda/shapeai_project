import apirequests
import requests
from datetime import datetime

# defining api
api_key = 'b44d8627b2fc5f110252253122f60ebc'
loc = input('Enter a location: ')

# calling api
api_link = "https://api.openweathermap.org/data/2.5/weather?q="+loc+"&appid="+api_key
api_get_link = requests.get(api_link)
api_data = api_get_link.json()

# storing data
temp = ((api_data['main']['temp']) - 273.15)
desc = api_data['weather'][0]['description']
humidt = api_data['main']['humidity']
w_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# output
print("-------------------------------------------------------------")
print("Weather stats for - {} || {}".format(loc.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature: {:.2f} C".format(temp))
print("Weather Description: ", desc.upper())
print("Current Humidity: ", humidt, "%")
print("Wind speed: ", w_speed, 'km/ph')






