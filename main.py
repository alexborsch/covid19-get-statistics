import requests
import json
import time
import os

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

c = input("Enter country: ")

querystring = {"country":c}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "YOUR-TOKEN-KEY"
    }

while True:
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    country = str(json_data['data']['covid19Stats'][0]['country'])
    lastUpdate = str(json_data['data']['covid19Stats'][0]['lastUpdate'])
    deaths = str(json_data['data']['covid19Stats'][0]['deaths'])
    confirmed = str(json_data['data']['covid19Stats'][0]['confirmed'])
    recovered = str(json_data['data']['covid19Stats'][0]['recovered'])
    print('Country: '+country+'\nDate: '+lastUpdate+'\nConfirmed: '+confirmed+'\nRecovered: '+recovered+'\nDeaths: '+deaths)
    time.sleep(10)
    os.system('cls')