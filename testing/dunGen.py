import os
import random
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter_shortcuts as tksh
from PIL import Image, ImageDraw
import dungen_Pillow as dP

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

root = Tk()
root.title("Dungeon Gen 0.0")
root.minsize(900, 500)

# blank_slate = Image.new('RGB', (50, 50), color='#32a852')

class Dungeon():
    def __init__(self, x_max, y_max, history, location):
        self.x_max = x_max
        self.y_max = y_max
        self.history = history
        self.location = location
        self.rooms = []
        self.image = Image.new('RGB', (x_max, y_max), color='#32a852')
    def add_rooms(self, roomNum):
        x_room_size = random.randint(5, int(self.x_max*0.5))
        y_room_size = random.randint(5, int(self.y_max*0.5))
        x_room_start = 1
        y_room_start = 1
        self.rooms.append(Room(x_room_size, y_room_size, x_room_start, y_room_start, self.image))
        for i in range(roomNum-1):
            #add in the direction choice, hallway gen, and other features
            #look in each direction, choose out of viable options
            #randomly choose number 0-3.
            #or randomly choose dict direction tuple of positives and negatives
            x_room_size = random.randint(5, int(self.x_max*0.5))
            y_room_size = random.randint(5, int(self.y_max*0.5))
            x_room_start = random.randint(5, int(self.y_max*0.5))
            y_room_start = random.randint(5, int(self.y_max*0.5))
            self.rooms.append(Room(x_room_size, y_room_size, x_room_start, y_room_start, self.image))
        self.image.save('donegeon.png', 'PNG')

"""
so we want each room to have a list of the connecting rooms. OR!? does the Dungeon's list of Rooms include that?

could it be added after the fact?

create base room - give it null connections
create next room - connect it to base room (then connect base room to it??)

room connector will take in 2 rooms.
room connector appends the rooms to each room's connected_rooms list

So. On the initial generation this will be easy. Then after initial room gen?

another function to decide which rooms to connect


"""

class Room():
    def __init__(self, x_size, y_size, x_axis_start, y_axis_start, image):
        self.x_size = x_size
        self.y_size = y_size
        self.contents = []
        self.x_axis_start = x_axis_start
        self.y_axis_start = y_axis_start
        self.x_axis_end = self.x_axis_start + self.x_size
        self.y_axis_end = self.y_axis_start + self.y_size
        dP.draw_room(self.x_axis_start, self.y_axis_start, self.x_axis_end, self.y_axis_end, image=image)
        self.connected_rooms = [] # make it like a linked list
        #gen some lore here? & fill room

test_dungeon = Dungeon(50, 50, '', '')
test_dungeon.add_rooms(2)


root.mainloop()