import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

def column_label_gen(columns, parent_name, row_num=0, sticky_var=(N, E, W)): #makes colums of labels input list with [NONE, x=StringVar()] for text variables
     label_start = 0
     for i in columns:
        if type(i) == list:
            i[0] = ttk.Label(parent_name, textvariable=i[1])
            i[0].grid(column=label_start, row=row_num, sticky=sticky_var)
            i[1].set(0)
        else:
            ttk.Label(parent_name, text=i).grid(column=label_start, row=row_num, sticky=sticky_var)
        label_start += 1

def row_label_gen(rows, parent_name, column_num=0, sticky_var=(N, E, W)): #makes rows of labels
     label_start = 0
     for i in rows:
          ttk.Label(parent_name, text=i).grid(row=label_start, column=column_num, sticky=sticky_var)
          label_start += 1

def column_entry_gen(entrys, parent_name, row_num=0, sticky_var=(N, E, W)): #this makes columns of entry boxes
     entry_start = 0
     for i in entrys:
          i[0] = ttk.Entry(parent_name, textvariable=i[1])
          i[0].grid(column=entry_start, row=row_num, sticky=sticky_var)
          i[0].insert(0, "DEFAULT")
          entry_start += 1

def row_entry_gen(entrys, parent_name, column_num=0, sticky_var=(N, E, W)): #this makes rows of entry boxes
     entry_start = 0
     for i in entrys:
          i[0] = ttk.Entry(parent_name, textvariable=i[1])
          i[0].grid(row=entry_start, column=column_num, sticky=sticky_var)
          i[0].insert(0, "DEFAULT")
          entry_start += 1

def weight_assign(object, x=1, y=1):
     size = object.grid_size()
     for i in range(size[0]):
          object.columnconfigure(i, weight=x)
     for j in range(size[1]):
          object.rowconfigure(j, weight=y)

def padding(object, x=6, y=6):
     for child in object.winfo_children(): 
          child.grid_configure(padx=x, pady=y)
