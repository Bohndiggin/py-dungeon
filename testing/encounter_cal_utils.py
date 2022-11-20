import numpy as np

xp_list = [
    np.array([0, 10]),
    np.array([0.125, 25]),
    np.array([0.25, 50]),
    np.array([0.5, 100]),
    np.array([1, 200]),
    np.array([2, 450]),
    np.array([3, 700]),
    np.array([4, 1100]),
    np.array([5, 1800]),
    np.array([6, 2300]),
    np.array([7, 2900]),
    np.array([8, 3900]),
    np.array([9, 5000]),
    np.array([10, 5900]),
    np.array([11, 7200]),
    np.array([12, 8400]),
    np.array([13, 10000]),
    np.array([14, 11500]),
    np.array([15, 13000]),
    np.array([16, 15000]),
    np.array([17, 18000]),
    np.array([18, 20000]),
    np.array([19, 22000]),
    np.array([20, 25000]),
    np.array([21, 33000]),
    np.array([22, 41000]),
    np.array([23, 50000]),
    np.array([24, 62000]),
    np.array([30, 155000])
]

thresholds = [
    np.array([25, 50, 75, 100]),
    np.array([50, 100, 150, 200]),
    np.array([75, 150, 225, 400]),
    np.array([125, 250, 375, 500]),
    np.array([250, 500, 750, 1100]),
    np.array([300, 600, 900, 1400]),
    np.array([350, 750, 1100, 1700]),
    np.array([450, 900, 1400, 2100]),
    np.array([550, 1100, 1600, 2400]),
    np.array([600, 1200, 1900, 2800]),
    np.array([800, 1600, 2400, 3600]),
    np.array([1000, 2000, 3000, 4500]),
    np.array([1100, 2200, 3400, 5100]),
    np.array([1250, 2500, 3800, 5700]),
    np.array([1400, 2800, 4300, 6400]),
    np.array([1600, 3200, 4800, 7200]),
    np.array([2000, 3900, 5900, 8800]),
    np.array([2100, 4200, 6300, 9500]),
    np.array([2400, 4900, 7300, 10900]),
    np.array([2800, 5700, 8500, 12700])
]

enc_multiplier = np.array([1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4])

class Character:
    def __init__(self, name, level=0):
        self.name = name
        self.level = int(level)
    def level_up(self):
        if self.level < 19:
            self.level += 1
            # calculate_thresholds()
        else:
            pass
    def __str__(self):
        return f'{self.name}. Level: {self.level}'

class Monster:
    def __init__(self, name, level=0, URL=''):
        self.name = name
        self.level = level
        self.URL = URL
        self.xp = xp_get(int(self.level))
    def __str__(self):
        return(f"{str(self.name)}. CR: {str(self.level)}")

def calculate_thresholds(character_list):
    current_xp = np.array([0, 0, 0, 0])
    for character in character_list:
        current_xp += thresholds[character.level]
    return current_xp

def level(character_list):
    for i in character_list:
        i.level_up()

def xp_get(level): # FIX IT
    xp = 0
    for i in xp_list:
        if i[0] == level:
            xp = i[1]
        else:
            continue
    return xp

def calculate_encounter(monster_list):
    exp = 0
    for i in monster_list:
        exp += i.xp
    if len(monster_list) <= 15:
        exp *= enc_multiplier[len(monster_list)-1]
    else:
        exp *= 4
    return exp