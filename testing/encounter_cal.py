import os
import sys
from tkinter import *
from tkinter import ttk
import tkinter_shortcuts as tksh
import json

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

root = Tk()
root.title("Encounter XP Thingy 1.0")

easy_xp_disp = StringVar()
medium_xp_disp = StringVar()
hard_xp_disp = StringVar()
deadly_xp_disp = StringVar()
character_name = StringVar()
encounter_xp = StringVar()
monster_name = StringVar()

character_list = []
monster_list = []

xp_list = [
    [0, 10],
    [0.125, 25],
    [0.25, 50],
    [0.5, 100],
    [1, 200],
    [2, 450],
    [3, 700],
    [4, 1100],
    [5, 1800],
    [6, 2300],
    [7, 2900],
    [8, 3900],
    [9, 5000],
    [10, 5900],
    [11, 7200],
    [12, 8400],
    [13, 10000],
    [14, 11500],
    [15, 13000],
    [16, 15000],
    [17, 18000],
    [18, 20000],
    [19, 22000],
    [20, 25000],
    [21, 33000],
    [22, 41000],
    [23, 50000],
    [24, 62000],
    [30, 155000]
]

xp_list_monsters = []
for i in xp_list:
    xp_list_monsters.append(i[0])
#xp_list_monsters.append("Other")

#xp thresholds for characters. Easy - Medium - Hard - Deadly
thresholds = [
    [25, 50, 75, 100],
    [50, 100, 150, 200],
    [75, 150, 225, 400],
    [125, 250, 375, 500],
    [250, 500, 750, 1100],
    [300, 600, 900, 1400],
    [350, 750, 1100, 1700],
    [450, 900, 1400, 2100],
    [550, 1100, 1600, 2400],
    [600, 1200, 1900, 2800],
    [800, 1600, 2400, 3600],
    [1000, 2000, 3000, 4500],
    [1100, 2200, 3400, 5100],
    [1250, 2500, 3800, 5700],
    [1400, 2800, 4300, 6400],
    [1600, 3200, 4800, 7200],
    [2000, 3900, 5900, 8800],
    [2100, 4200, 6300, 9500],
    [2400, 4900, 7300, 10900],
    [2800, 5700, 8500, 12700]
]

lv_list = []
for i in range(len(thresholds)):
    lv_list.append(i + 1)


#encounter multiplier is based on monster count

enc_multiplier = [1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4]

mainframe = ttk.Frame(root, padding="3 3 30 30")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sub_threshold = ttk.Frame(mainframe, padding="3 3 30 30")
sub_threshold.grid(column=0, row=0, sticky=(N, W))

encounter_xp_disp_box = ttk.Frame(mainframe, padding="3 3 30 30")
encounter_xp_disp_box.grid(column=0, row=2, sticky=(N, W))

characters = ttk.Frame(mainframe, padding="3 3 30 30")
characters.grid(column=1, row=0, sticky=N)
ttk.Label(characters, text="Character:").grid(column=0, row=0, sticky=(N, W))
ttk.Label(characters, text="Level:").grid(column=1, row=0, sticky=(N, E))
characters_controls = ttk.Frame(mainframe, padding="3 3 30 30")
characters_controls.grid(column=1, row=1, sticky=N)

monsters = ttk.Frame(mainframe, padding="3 3 30 30")
monsters.grid(column=2, row=0, sticky=N)
ttk.Label(monsters, text="Monster:").grid(column=0, row=0, sticky=N)
ttk.Label(monsters, text="Level:").grid(column=1, row=0, sticky=N)
monsters_controls = ttk.Frame(mainframe, padding="3 3 30 30")
monsters_controls.grid(column=2, row=1, sticky=N)

class Character:
    def __init__(self, name, level=0):
        self.name = name
        self.level = int(level)
        self.level_disp = StringVar()
        global character_list
        character_list.append(self)
        self.level_disp.set(self.level)
        name_display = ttk.Label(characters, text=self.name)
        name_display.grid(column=0, row=(len(character_list) + 1))
        level_display = ttk.Label(characters, textvariable=self.level_disp)
        level_display.grid(column=1, row=(len(character_list) + 1))
    def level_up(self):
        if self.level < 19:
            self.level += 1
            self.level_disp.set(self.level + 1)
            calculate_thresholds()
        else:
            pass

class Monster:
    def __init__(self, name, level=0, xp=0):
        self.name = name
        self.level = level
        self.level_disp = StringVar()
        if self.level == "Other":
            self.xp = int(xp)
            self.level += ": ({} XP)"
            self.level_disp.set(self.level.format(self.xp))
        else:
            self.xp = xp_get(int(self.level))
            self.level_disp.set(str(self.level))
        monster_list.append(self)
        mon_name_display = ttk.Label(monsters, text=self.name)
        mon_name_display.grid(column=0, row=(len(monster_list) + 1))
        mon_level_display = ttk.Label(monsters, textvariable=self.level_disp)
        mon_level_display.grid(column=1, row=(len(monster_list) +1))
    def __str__(self):
        return(f"{str(self.name)}. CR: {str(self.level)}")

def calculate_thresholds():
    current_xp = [0, 0, 0, 0]
    for j in range(len(thresholds[0])):
        for character in character_list:
            current_xp[j] += thresholds[character.level][j]
    display_update(current_xp)

def display_update(current_xp):
    global easy_xp_disp, medium_xp_disp, hard_xp_disp, deadly_xp_disp
    try:
        easy_xp_disp.set(current_xp[0])
        medium_xp_disp.set(current_xp[1])
        hard_xp_disp.set(current_xp[2])
        deadly_xp_disp.set(current_xp[3])
    except:
        easy_xp_disp.set(0)
        medium_xp_disp.set(0)
        hard_xp_disp.set(0)
        deadly_xp_disp.set(0)

def level():
    for i in character_list:
        i.level_up()

def xp_get(level):
    xp = 0
    for i in xp_list:
        if i[0] == level:
            xp = i[1]
        else:
            continue
    return xp

def add_character_dialogue():
    t = Toplevel(mainframe)
    character_level = StringVar()
    def add_character():
        Character(character_name.get(), character_level.get())
    ttk.Label(t, text="Add Character: ").grid(column=0, row=0, sticky=N)
    box = ttk.Entry(t, textvariable=character_name)
    box.grid(column=1, row=0, sticky=N)
    character_level_entry = ttk.Combobox(t, textvariable=character_level)
    character_level_entry["values"] = lv_list
    character_level_entry.grid(column=2, row=0, sticky=N)
    ttk.Button(t, text="Add", command=add_character).grid(column=3, row=0, sticky=N)

def add_monster_dialogue():
    md = Toplevel(mainframe) # Monster Dialogue
    other_level = StringVar()
    monster_name = StringVar()
    def add_monster():
        Monster(monster_name.get(), monster_level.get())
    def other_monster_level():
        oml = Toplevel(md)
        def add_other_monster():
            Monster(monster_name.get(), "Other", other_level.get())
        ttk.Label(oml, text="XP:").grid(column=0, row=0, sticky=N)
        oml_box = ttk.Entry(oml, textvariable=other_level)
        oml_box.grid(column=1, row=0, sticky=N)
        ttk.Button(oml, text="Add", command=add_other_monster).grid(column=2, row=0, sticky=N)
    ttk.Label(md, text="Add Monster: ").grid(column=0, row=0, sticky=N)
    monster_box = ttk.Entry(md, textvariable=monster_name)
    monster_box.grid(column=1, row=0, sticky=N)
    monster_level = StringVar()
    monster_select = ttk.Combobox(md, textvariable=monster_level)
    monster_select["values"] = xp_list_monsters
    monster_select.grid(column=2, row=0, sticky=N)
    ttk.Button(md, text="Other", command=other_monster_level).grid(column=3, row=0, sticky=N)
    ttk.Button(md, text="Add", command=add_monster).grid(column=4, row=0, sticky=N)

def calculate_encounter():
    exp = 0
    for i in monster_list:
        exp += i.xp
    if len(monster_list) <= 15:
        exp *= enc_multiplier[len(monster_list)-1]
    else:
        exp *= 4
    encounter_xp.set(exp)

tksh.column_label_gen(["Easy", "Medium", "Hard", "Deadly"], sub_threshold)
tksh.column_label_gen([[NONE, easy_xp_disp], [NONE, medium_xp_disp], [NONE, hard_xp_disp], [NONE,deadly_xp_disp]], sub_threshold, row_num=1)

ttk.Label(encounter_xp_disp_box, text="Encounter XP:").grid(column=0, row=0, sticky=(N, W))
encounter_xp_disp = ttk.Label(encounter_xp_disp_box, textvariable=encounter_xp)
encounter_xp_disp.grid(column=1, row=0, sticky=N)
ttk.Button(encounter_xp_disp_box, text="Calculate Encounter", command=calculate_encounter).grid(column=1, row=1, sticky=(N, W))

ttk.Button(mainframe, text="Calculate", command=calculate_thresholds).grid(column=0, row=1, sticky=N)
ttk.Button(characters_controls, text="Level Up", command=level).grid(column=1, row=0, sticky=N)
ttk.Button(characters_controls, text="Add Character", command=add_character_dialogue).grid(column=0, row=0, sticky=N)
ttk.Button(monsters_controls, text="Add Monster", command=add_monster_dialogue).grid(column=0, row=0, sticky=(N, W))

tksh.padding(mainframe, x=6, y=6)

tksh.padding(sub_threshold, x=12, y=12)
tksh.padding(characters, x=6, y=0)
for i in [mainframe, characters, monsters]:
    tksh.weight_assign(i)

# root.mainloop()