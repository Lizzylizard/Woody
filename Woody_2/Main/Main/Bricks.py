'''
Created on 14.04.2020

@author: Elisabeth
'''
import tkinter 
import random

class Brick():
    def __init__(self):
        three_x_three = Three_X_Three()
        l_big_down_right = L_Big_Down_Right()  
        l_big_up_right = L_Big_Up_Right()      
        l_big_down_left = L_Big_Down_Left()       
        l_big_up_left = L_Big_Up_Left()  
        one_x_five = One_X_Five()        
        l_small_down_right = L_Small_Down_Right()
        l_small_down_left = L_Small_Down_Left()
        l_small_up_right = L_Small_Up_Right()
        l_small_up_left = L_Small_Up_Left()
        five_x_one = Five_X_One()
        four_x_one = Four_X_One()
        one_x_four = One_X_Four()
        three_x_one = Three_X_One()
        one_x_three = One_X_Three()
        two_x_one = Two_X_One()
        one_x_two = One_X_Two()
        one_x_one = One_X_One()
        l_short_down_right = L_Short_Down_Right()
        l_short_down_left = L_Short_Down_Left()
        l_short_up_right = L_Short_Up_Right()
        l_short_up_left = L_Short_Up_Left()
        
        self.allBricks = {0: three_x_three, 1: l_big_down_right, 2: l_big_down_left, 3: l_big_up_left, 
                          4: one_x_five, 5: l_big_up_right, 6: l_small_down_right, 7: l_small_down_left,
                          8: l_small_up_right, 9: l_small_up_left, 10: five_x_one, 11: four_x_one,
                          12: one_x_four, 13: three_x_one, 14: one_x_three, 15: two_x_one,
                          16: one_x_two, 17: one_x_one, 18: l_short_down_right, 19: l_short_down_left,
                          20: l_short_up_right, 21: l_short_up_left}
        self.number_of_bricks = 21
        
    def __repr__(self):
        return "Shape"  
        
    
class Three_X_Three(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, True, True, False],
                      [False, True, True, True, False], 
                      [False, True, True, True, False],
                      [False, False, False, False, False]]
        #print(self.shape[0][0])
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " Three_X_Three"
        
#my_brick = Three_X_Three()

class L_Big_Down_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, False, False, False],
                      [False, True, False, False, False], 
                      [False, True, True, True, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Big_Down_Right"
    
class L_Big_Down_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, True, False],
                      [False, False, False, True, False], 
                      [False, True, True, True, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Big_Down_Left"
    
class L_Big_Up_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, True, True, False],
                      [False, False, False, True, False], 
                      [False, False, False, True, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Big_Up_Left"
    
class L_Big_Up_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, True, True, False],
                      [False, True, False, False, False], 
                      [False, True, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Big_Up_Right"
    
class L_Small_Down_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, False, False, False],
                      [False, True, True, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Small_Down_Right"
    
class L_Small_Down_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, False, False],
                      [False, True, True, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Small_Down_Left"
    
class L_Small_Up_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, True, False, False],
                      [False, True, False, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Small_Up_Right"
    
class L_Small_Up_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, True, False],
                      [False, False, False, True, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Small_Up_Left"
    
class One_X_Five(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, False, False],
                      [True, True, True, True, True], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " One_X_Five"
    
class Five_X_One(Brick):
    def __init__(self):
        self.shape = [[False, False, True, False, False],
                      [False, False, True, False, False],
                      [False, False, True, False, False], 
                      [False, False, True, False, False],
                      [False, False, True, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " Five_X_One"
    
class Four_X_One(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, False, False],
                      [False, False, True, False, False], 
                      [False, False, True, False, False],
                      [False, False, True, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " Four_X_One"
    
class One_X_Four(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, False, False],
                      [False, True, True, True, True], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " One_X_Four"
    
class Three_X_One(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, False, False],
                      [False, False, True, False, False], 
                      [False, False, True, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " Three_X_One"
    
class One_X_Three(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, False, False],
                      [False, True, True, True, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " One_X_Three"
    
class Two_X_One(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, False, False],
                      [False, False, True, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " Two_X_One"
    
class One_X_Two(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, False, False],
                      [False, True, True, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " One_X_Two"
    
class One_X_One(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, False, False],
                      [False, False, True, False, False], 
                      [False, False, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " One_X_One"
    
class L_Short_Down_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, False, False, False],
                      [False, True, False, False, False], 
                      [False, True, True, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Short_Down_Right"
    
class L_Short_Down_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, False, True, False],
                      [False, False, False, True, False], 
                      [False, False, True, True, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Short_Down_Left"
    
class L_Short_Up_Right(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, True, True, False, False],
                      [False, True, False, False, False], 
                      [False, True, False, False, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Short_Up_Right"
    
class L_Short_Up_Left(Brick):
    def __init__(self):
        self.shape = [[False, False, False, False, False],
                      [False, False, True, True, False],
                      [False, False, False, True, False], 
                      [False, False, False, True, False],
                      [False, False, False, False, False]]
        
    def __repr__(self):
        my_str = super().__repr__()
        return my_str + " L_Short_Up_Left"
    

#will later on choose brick randomly
def chooseBrick():
    master_brick = Brick()
    
    rand_int = random.randint(0, master_brick.number_of_bricks)
    #print("Rand int = ", rand_int)
        
    my_brick = master_brick.allBricks.get(rand_int)
    return my_brick

#another comment