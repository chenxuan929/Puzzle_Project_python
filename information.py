import turtle
import math
import random
global pos
import time
import logging

from leaderboard import *
class information:
    def __init__(self, filename, allow_move, playername):
        self.filename = filename
        self.allow_move = allow_move
        self.playername = playername
        
        self.object = []
        self.blank = []
        self.move_object = []
        self.object1 = []
        self.t_t = []
        self.t_t1 = []
        self.thumb = []
        self.thumb1 = []
        self.random_dict = {}
        self.moves = 0
             
    def get_dict(self):
        '''
        Get a dictionary of all the images' tiles in puz.file
        Return the dictionary create
        '''
        try:
            # open file as reading, asign number as key, asign tiles as value
            with open(self.filename, "r") as file:
                # create a blank dict to start store
                my_dict = {}
                for line in file:
                    (key, value) = line.replace(' ', '').strip().split(":")
                    my_dict[key] = value
            return my_dict
        # if can not find the file, record the error in txt file
        except Exception as Argument:
            # open file for appending
            f = open("5001_puzzle.err.txt", "a")
            f.write(str(Argument))
            f.close()

    def get_filename(self):
        '''
        Get current filename
        Return current filename
        
        '''
        name = self.get_dict()['name']
        return name

    def get_number(self):
        '''
        Get number of tile in dictionary
        Return number
        
        '''
        number = self.get_dict()['number']
        return number

    def get_size(self):
        '''
        Get size of image in dictionary
        Return size
        
        '''
        size = self.get_dict()['size']
        return size

    def get_thumbnail(self):
        '''
        Get thumbnail's path in dictionary
        Return path
        
        '''
        thumbnail = self.get_dict()['thumbnail']
        thumbnail_path = thumbnail
        # replace extra blank before path
        thumbnail_path = thumbnail_path.replace(" ","")
        return thumbnail_path

    def get_tiles(self):
        '''
        Get original tiles list of each image for each puz
        Return original tiles
        
        '''
        # crating blank list key, tile to store the number and path of images
        key = []
        for i in range(int(self.get_number())):
            key.append(str(i + 1))
        tile = []
        for j in range(len(key)):
            tile.append(self.get_dict().get(key[j]))
        
        return tile
             
        
    def get_image_location(self):
        '''
        Get original location nested list of each image for each puz
        Return list
        
        '''
        # creating blank lists to store coordinate for x, y and (x, y)
        xpos = []
        ypos = []
        coor = []
        # sqrt.number to get how many imags each row
        n = int(math.sqrt(int(self.get_number())))
        for i in range(n):
            # determine specific location of each 
            xpos.append(-250 + i * 100)
            ypos.append(330 - (i + 1) * 100)

        for j in ypos:
            for k in xpos:
                position = k, j
                # setting x position and y position as one coordinate then save
                coor.append(position)
        # creating a nested list to store all the coordinate for better determine the position
        nested_lst = [coor[i: i + n] for i in range(0, len(coor), n)]

        return nested_lst


    def flat(self):
        '''
        Get original coordinate common list of each image for each puz
        Return list
        
        '''
        n = int(math.sqrt(int(self.get_number())))
        coor = []
        # open the nested list to save as a easy common list for easier insert each puzzle one by one
        for i in range(n):
            for j in range(int(n)):
                item = self.get_image_location()[i][j]
                coor.append(item)
        return coor
    

    def shuffle(self):
        '''
        Get the images' tile list after shuffling 
        Return list
        
        '''
        # original path can get from get_tiles function
        path = self.get_tiles()
        # using random to shuffle tiles get a new tile list
        new_path = path.copy()
        random.shuffle(new_path)
        return new_path
    
    def flat_dict(self):
        '''
        Builfing a right order coordinate dictionary of puzzles
        Returns dictionary

        '''
        # getting original tiles
        tile = self.get_tiles()
        # getting original coordinate
        cor = self.flat()
        flat_dict = {}
        key = []
        value = []
        # key is cooridinate
        # value is tiles
        for i in range(len(tile)):
            key.append(cor[i])
            value.append(tile[i])
            flat_dict = dict(zip(key, value))
        return flat_dict
            

    def insert_image(self):
        '''
        Insert different puzzles image in one puz.file and draw the frame
        Return None
        
        '''
        tiles_lst = self.shuffle() 
        # find the index of blank gif in the suffled list
        blank_ori = self.get_tiles()[-1]
        blank_i = tiles_lst.index(blank_ori)
    
        for i in range(len(self.flat())):
            t = turtle.Turtle()
            self.t_t.append(t)
            t.hideturtle()
            t.speed(12)
            t.penup()
            # draw frames around each puzzle
            t.goto(self.flat()[i])
            t.forward(int(self.get_size())/2)
            t.left(90)
            t.forward(int(self.get_size())/2)
            t.left(90)
            t.forward(1)
            t.pendown()
            for j in range(4):                
                t.forward(int(self.get_size()))
                t.left(90)
            tg = turtle.Turtle()
            # create a list of Turtle object
            self.object.append(tg)
            tg.hideturtle()
            screen = turtle.Screen()
            tg.penup()
            # insert random puzzle image on canvas
            center = self.flat()[i]
            tg.goto(center)
            name = tiles_lst[i]
            screen.addshape(name)
            tg.shape(name)
            tg.showturtle()

        # create a shuffle puzzle's dictionary 
        turtle_pos = []
        for each in self.object:
            a = each.xcor()
            b = each.ycor()
            pos = (a, b)
            turtle_pos.append(pos)
        # position of each turtle as key
        # tiles as value
        self.random_dict = dict(zip(turtle_pos, tiles_lst))
        
        # find the blank Turtle object
        blank_location = self.object[blank_i]
        self.blank.append(blank_location)
            
        # draw thumbnail refer to the puzzle file is playing
        thumbnail = turtle.Turtle()
        self.thumb.append(thumbnail)
        thumbnail.hideturtle()
        thumbnail.penup()
        thumbnail.goto(290, 250)
        screen = turtle.Screen()
        # get the path of thumbnail
        screen.addshape(self.get_thumbnail())
        thumbnail.shape(self.get_thumbnail())
        thumbnail.showturtle()


    def get_blank(self):
        '''
        Get the blank object
        Return list

        '''
        return self.blank

    def get_turtle_object(self):
        '''
        Get the turtle object
        Return list

        '''
        return self.t_t

    def get_object_location(self):
        '''
        Get the object position
        Return list

        '''
        return self.object

    def object_check(self, x, y):
        '''
        Check if click on any object
        Return object

        '''
        for each in self.object:
            a = each.xcor()
            b = each.ycor()
            # if click inside the size of puzzle image
            if a - 50 <= x <= a + 50 and b - 50 <= y <= b + 50:
                return each
    
    def is_adjacency(self, x, y):
        '''
        Determain if blank and click object have relationship
        Return Bool
        '''
        blank = self.blank[0]
        # if click outside the blank with distance 50 to 100
        if 50 <= blank.distance(self.object_check(x, y)) <= 100:
            return True

    def swap(self, x, y):
        '''
        Determain if blank and click object have relationship then swap puzzles
        Return Bool
        '''
        
        judge = self.is_adjacency(x, y)
        # get the blank object
        blank = self.blank[0]
        # get the coordinate of blank object
        blank_cor = (blank.xcor(), blank.ycor())
        click_turtle = self.object_check(x, y)
        # get click coorfinate
        click_cor = (click_turtle.xcor(), click_turtle.ycor())

        # if function adjacency return True, start swap the puzzles
        if judge is True:
            blank.hideturtle()
            click_turtle.penup()
            click_turtle.goto(blank_cor)
            # change the coorfinate of blank object and clicked puzzle object
            change_value = self.random_dict[blank_cor]
            # replace each other to achieve one swap
            self.random_dict[blank_cor] = self.random_dict[click_cor]
            blank.penup()
            blank.goto(click_cor)
            self.random_dict[click_cor] = change_value
            blank.showturtle()
            return True

    def get_moves(self, x, y):
        '''
        keep score of how many times play swap
        return move times
        
        '''
        # if swap successfully, add 1 to players moves times to keep score
        if self.swap(x, y) == True:
            self.moves +=  1
            # for previous score object, hide and clear
            for each in self.move_object:
                each.clear()
                each.hideturtle()
            # wirte the update score on same position every time and keep updating
            t = turtle.Turtle()
            t.hideturtle()
            t.up()
            # select score position
            t.goto(-300, -260)
            t.down()
            t.write(f"Player Moves: {self.moves}", font = ['Arial', 20, 'normal'])
            # update the score object in list
            self.move_object.append(t)
        return self.moves


    
    def win(self, x, y):
        '''
        Adjust player win or lose in one game
        Return None
        '''
    
        a = self.get_moves(x, y)
        t = turtle.Turtle()
        # get player's moves until now as a
        # get allowed moves, then compare to each other
        # if players moves less then allowed moves and puzzles position now is same as right order position, win
        if a <= self.allow_move and self.flat_dict() == self.random_dict:
            s = turtle.Screen()
            s.addshape("./Resources/winner.gif")
            t.shape("./Resources/winner.gif")
            time.sleep(2)
            # add playersname and score on leaderboard
            leaderboard(self.playername, self.moves)
            exit()
        # if players moves has achieve allowed moves and puzzles position now not same as right order position, lose  
        elif a > self.allow_move and self.flat_dict() != self.random_dict:
            s2 = turtle.Screen()
            s2.addshape("./Resources/Lose.gif")
            t.shape("./Resources/Lose.gif")
            time.sleep(2)
            s2.addshape("./Resources/credits.gif")
            t.shape("./Resources/credits.gif")
            exit()

