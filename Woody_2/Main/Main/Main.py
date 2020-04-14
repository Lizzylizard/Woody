'''
Created on 14.04.2020

@author: Elisabeth
'''

import tkinter
import OpenWindow as ow

top = tkinter.Tk()
top.title("Woody")
top.resizable(True, True)
game = ow.Game(top)
top.mainloop()

