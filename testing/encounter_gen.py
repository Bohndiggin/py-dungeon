import encounter_cal_utils as enc_utils
import json
import random

with open('monsters.json', 'r') as monster_array:
    monsters_dict = json.load(monster_array)

selection = random.choice(list(monsters_dict.values())) #### this is where the ai will choose the monsters.

print(selection)

monster = enc_utils.Monster(selection["name"], selection["cr"], selection["url"])

print(monster)

char_1 = enc_utils.Character('jeff')
char_2 = enc_utils.Character('james')
char_3 = enc_utils.Character('jerry')
char_4 = enc_utils.Character('jimothy')
char_list = [char_1, char_2, char_3, char_4]

print(enc_utils.calculate_thresholds(char_list))