'''
Created on 14.04.2020

@author: Elisabeth
'''

import tkinter

class Motion():
    
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0

    def moveBricks(self, master):
        master.bind("<Button-1>", callback)
        
    def getMousePos(self):
        print ("Mouse x = ", self.mouse_x, ", Mouse y = ", self.mouse_y)
        return self.mouse_x, self.mouse_y
    

motion = Motion()

def callback(event):
    motion.mouse_x = event.x
    motion.mouse_y = event.y
    #print ("Mouse x = ", motion.mouse_x, ", Mouse y = ", motion.mouse_y)
    
    if (motion.mouse_y >= 600 and motion.mouse_y <= 800):
        if(motion.mouse_x <= 200):
            print("Chose shape 1")
        if(motion.mouse_x >= 201 and motion.mouse_x <= 400):
            print("Chose shape 2")
        if(motion.mouse_x >= 401):
            print("Chose shape 3")