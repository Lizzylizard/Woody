'''
Created on 14.04.2020

@author: Elisabeth
'''
import tkinter
import Bricks

class Game(tkinter.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 600
        self.height = 700
        self.canvas = tkinter.Canvas(self, width=self.width, height=self.height, bg='#AA6C39')
        
        self.showGrid()
        self.showScore(200, 15)
        
        self.canvas.pack()
        self.pack()
        
    def showGrid(self):
        #Position variables
        cwidth = self.width - 100
        cheight = self.height - 200
        posX_start = 50
        posY_start = 50
        posX_end = self.width-50
        posY_end = self.height-150
        #print("Canvas width = ", cwidth, "\nCanvas height = ", cheight, "\nPos X End = ", posX_end, "\nPos Y End = ", posY_end)
        
        #outline
        self.canvas.create_rectangle(posX_start, posY_start, posX_end, posY_end, width=4)
        
        #columns
        for i in range(posX_start, cwidth+posX_start):
            if (i % 50 == 0):
                self.canvas.create_line(i, 50, i, posY_end)
            if(i % 300 == 0):                
                self.canvas.create_line(i, 50, i, posY_end, width = 3)
                
        #rows
        for i in range(posY_start, cheight+posY_start):
            if(i % 50 == 0):
                self.canvas.create_line(posX_start, i, posX_end, i)
            if(i % 300 == 0):                
                self.canvas.create_line(posX_start, i, posX_end, i, width = 3)
                
    def showScore(self, score, size):
        #text = tkinter.Text(master, width = 70, height = 1)
        text = "Score = " + str(score)
        font = ("Helvetica", size)
        posX_middle = len(text)
        posY_middle = size / 2
        self.canvas.create_text(posX_middle, size, text=text, font=font)
        #text.pack()
        #text.insert(tkinter.END, "Just a text Widget")
        
        
        
        
        
        
        
        