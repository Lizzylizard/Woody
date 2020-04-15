'''
Created on 14.04.2020

@author: Elisabeth
'''

import tkinter
import GameLogic as gl

top = tkinter.Tk()
top.title("Woody")
top.resizable(True, True)
game = gl.Game(top)
top.mainloop()

