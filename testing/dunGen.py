import os
import random
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter_shortcuts as tksh
from PIL import Image
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
        for i in range(roomNum):
            #add in the direction choice, hallway gen, and other features
            x_room_size = random.randint(5, int(self.x_max*0.5))
            y_room_size = random.randint(5, int(self.y_max*0.5))
            x_room_start = random.randint(5, int(self.y_max*0.5))
            y_room_start = random.randint(5, int(self.y_max*0.5))
            self.rooms.append(Room(x_room_size, y_room_size, x_room_start, y_room_start, self.image))
        self.image.save('donegeon.png', 'PNG')


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
        self.connected_rooms = []
        #gen some lore here? & fill room

test_dungeon = Dungeon(50, 50, '', '')
test_dungeon.add_rooms(2)


root.mainloop()