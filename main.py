import requests
import json
import os

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=cb449cc296994f849f493015230604&q={city}"

r = requests.get(url)

print(r.text) #todo it collects the raw text of the url

# print(type(r.text))

weatherDic = json.loads(r.text) #todo json.loads() converts r.text into a json dictionary

print(weatherDic["current"]["temp_c"])

temperature = weatherDic["current"]["temp_c"]

text = weatherDic["current"]["condition"]['text']

command1 = f"say 'The current temperature in {city} is {temperature}'" #todo using say command of macOS
os.system(command1)

command2 = f"say 'Weather condition is {text}'"
os.system(command2)

localtime = weatherDic["location"]["localtime"]
command3 = f"say 'local time in {city} is {localtime}'"
os.system(command3)

