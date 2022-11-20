import requests
import json

base_api_url = 'https://www.dnd5eapi.co'

response_monsters = requests.get(base_api_url + '/api/monsters')
response_monsters.json()
response_monsters_json = response_monsters.json()
# print(response_monsters_json)

monsters_and_cr = {}

for i in response_monsters_json["results"]:
    curr_mon = {
        'index': i['index'],
        'name': i['name'],
        'url': i['url'],
        'cr': ''
    }
    curr_mon_json = requests.get(base_api_url + i["url"]).json()
    curr_mon['cr'] = curr_mon_json['challenge_rating']
    monsters_and_cr[f'{curr_mon["index"]}'] = curr_mon

# print(monsters_and_cr)

json_obj = json.dumps(monsters_and_cr, indent=4)

with open('monsters.json', 'w') as monster_json:
    monster_json.write(json_obj)