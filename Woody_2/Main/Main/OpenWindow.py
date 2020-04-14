'''
Created on 14.04.2020

@author: Elisabeth
'''
import tkinter
import Bricks
import Move

class Game(tkinter.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 600
        self.height = 850
        self.canvas = tkinter.Canvas(self, width=self.width, height=self.height, bg='#AA6C39')
        
        self.showGrid()
        #testscore
        self.showScore(200)
        self.showBricks()
        motion = Move.Motion()
        motion.moveBricks(master)
        motion.getMousePos()
        
        self.canvas.pack()
        self.pack()
        
    def showGrid(self):
        #Position variables
        cwidth = self.width - 100
        cheight = self.height - 350
        posX_start = 50
        posY_start = 50
        posX_end = self.width-50
        posY_end = self.height-300
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
                
    def showScore(self, score):
        text = "Score = " + str(score)
        font = ("Helvetica", "15")
        
        self.canvas.create_text(self.width-50, 45, text=text, font=font, anchor="se")
        
    def showBricks(self):
        text = "Choose from: "
        font = ("Helvetica", "15")
        size = len(text)
        print(size)
        self.canvas.create_text(50, 560, text=text, font=font, anchor="nw")
        
        self.canvas.create_line(200, 600, 200, 800, width = 2)
        self.canvas.create_line(400, 600, 400, 800, width = 2)
        
        
        square_size = 20 
        
        #first brick
        my_brick = Bricks.chooseBrick()
        print("1 = ", my_brick)   
    
        for i in range(len(my_brick.shape)):
            for j in range(len(my_brick.shape[i])):
                #print("i = ", i, " j = ", j)
                if my_brick.shape[i][j] == True:
                    x_left = j*square_size + 75
                    x_right = j*square_size + 75 + square_size
                    y_up = i*square_size + 640
                    y_down = i*square_size + 640 + square_size
                    self.canvas.create_rectangle(x_left, y_up, x_right, y_down)
                    #print("Up Left: (" + str(x_left) + ", " + str(y_up) + ")")
                
        #second brick
        my_brick_2 = Bricks.chooseBrick() 
        print("2 = ", my_brick_2)    
    
        for i in range(len(my_brick_2.shape)):
            for j in range(len(my_brick_2.shape[i])):
                #print("i = ", i, " j = ", j)
                if my_brick_2.shape[i][j] == True:
                    x_left = j*square_size + 250
                    x_right = j*square_size + 250 + square_size
                    y_up = i*square_size + 640
                    y_down = i*square_size + 640 + square_size
                    self.canvas.create_rectangle(x_left, y_up, x_right, y_down)
                    #print("Up Left: (" + str(x_left) + ", " + str(y_up) + ")")
        
        #third brick
        my_brick_3 = Bricks.chooseBrick()
        print("3 = ", my_brick_3)     
    
        for i in range(len(my_brick_3.shape)):
            for j in range(len(my_brick_3.shape[i])):
                #print("i = ", i, " j = ", j)
                if my_brick_3.shape[i][j] == True:
                    x_left = j*square_size + 425
                    x_right = j*square_size + 425 + square_size
                    y_up = i*square_size + 640
                    y_down = i*square_size + 640 + square_size
                    self.canvas.create_rectangle(x_left, y_up, x_right, y_down)
                    #print("Up Left: (" + str(x_left) + ", " + str(y_up) + ")") 
        
        
        
        
        