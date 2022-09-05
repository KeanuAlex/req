import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']

rating_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    rating_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

print(max(rating_dict))
