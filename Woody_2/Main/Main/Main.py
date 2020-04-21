'''
Created on 14.04.2020 

@author: Elisabeth
'''

import tkinter
import GameLogic as gl
import time

def main():
    top = tkinter.Tk()
    top.title("Woody")
    top.resizable(True, True)
    
    game = gl.Game(top)    
    
    top.mainloop()


if __name__ == '__main__':
    main()
    