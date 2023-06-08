'''
     CS5001
     Spring 2022
     Final Project
 
     Chenxuan Xu
'''
import turtle
import random
import time
import os
from information import *
from leaderboard import *
import glob

global current_file
global allow_move
global playername
global a

# setting original information for the screen and turtle
screen = turtle.Screen()
screen.title("CS5001 Sliding Puzzle Game")
screen.setup(width = 700, height = 700)

# setting original default puzzle game
current_file = "mario.puz"
# show game start image at first
turtle.addshape("./Resources/splash_screen.gif")
turtle.shape("./Resources/splash_screen.gif")
# staying for 3 seconds then clear
time.sleep(3) 
screen.clear()

# ask for the player's name and allow max moves
playername = turtle.textinput("CS5001 Puzzle Slide", "Your Name:")
allow_move = turtle.numinput("CS 5001 Puzzle Game - Moves", "Enter the number of moves"
                                   "\n(chances) you want (5-200)?", minval = 5, maxval = 200)

a = information(current_file, allow_move, playername)

def draw_rec(my_turtle,x,y,l,w,color):
    '''
    Parameters:
        my_turtle -- turtle.Turtle
        x, y -- the coordinate of start point
        l -- length of rectangular
        w -- width of rectangular
        color -- color of turtle pen
        
    Drawing rectangular on cnavas
    Returns nothing
        
    '''
    # setting my turtle's specific color to draw the frame
    my_turtle.color(color)
    # hide turtle's path for more clearly screen
    my_turtle.up()
    # let turtle go to the position that need drawing the frame
    my_turtle.goto(x,y)
    # show turtle to start drawing
    my_turtle.down()
    # using a loop to draw rectangular frame
    for i in range(2):
        # l is the length of rectangular
        my_turtle.forward(l)
        # change the direction
        my_turtle.right(90)
        # w is the width of the rectangular
        my_turtle.forward(w)
        # change the direction again to finish rectangular
        my_turtle.right(90)

def load_button(my_turtle,x,y,name_gif):
    '''
    Parameters:
        my_turtle -- turtle.Turtle
        x, y -- the coordinate of start point
        name_gif -- path of gif file
        
    Loading button's image on canvas
    Returns nothing
    '''
    # hiding turtle first to make screen more clearly
    my_turtle.hideturtle()
    my_turtle.up()
    # let turtle go to the position that needed a button
    my_turtle.goto(x,y)
    # show the turtle
    my_turtle.showturtle()
    # all the butto's image in screen
    screen.addshape(name_gif)
    # using turtle to put down the button's image in screen
    my_turtle.shape(name_gif)    


def load_question():
    '''
    Loading question to ask for user's input
    Returns a string represent the name of puzzle need to be use
    
    '''
    # ask for user's input to choose which puzzle would be load next
    puz_list = []
    for file in glob.glob("*.puz"):
        puz_list.append(file)

    if len(puz_list) > 10:
        s = turtle.Screen()
        t = turtle.Turtle()
        error = "./Resources/file_warning.gif"
        t.penup()
        t.goto(0, 0)
        s.register_shape(error)
        t.shape(error)
        
    elif len(puz_list) <= 10:
        choice = turtle.textinput("CS5001 Sliding Puzzle Game", f"{puz_list}")
        return choice


def load(x, y):
    '''
    Parameters:
        x, y -- the coordinate of onclick point
        
    Use if click on load button, clear previous turtle object, load a new puzzle as user asked
    Returns nothing
    
    '''
    global a
    # clear turtle object list contains image and thumbnail to start storing new
    for each in a.object:
        each.hideturtle()
    for every in a.t_t:
        every.clear()
    for i in a.thumb:
        i.hideturtle()

    a.object.clear()
    a.blank.clear()
    a.t_t.clear()
    a.thumb.clear()
    
    # asign the asnwers of user's input to class filename
    a.filename = load_question()
    current_file = a.filename
    
    # check if path refer to filename exists
    if os.path.exists(a.filename) == True:
        # insert new puzzles' image
        a.insert_image()
        # reset the players move score to zero
        a.moves = 0
    else:
        # if path refer to filename does not exists
        a = turtle.Screen()
        # sending gif image to warn
        nofile = './Resources/file_error.gif'
        error = turtle.Turtle()
        error.penup()
        error.goto(0, 0)
        a.register_shape(nofile)
        error.shape(nofile)
        

def quit_puz(x, y):
    '''
    Parameters:
        x, y -- the coordinate of onclick point
        
    Use if click on quit button, load images then exit the program
    Returns nothing
    
    '''
    t = turtle.Turtle()
    screen = turtle.Screen()
    # show quit image on screen
    screen.addshape("./Resources/quitmsg.gif")
    t.shape("./Resources/quitmsg.gif")
    # stay for 4 seconds
    time.sleep(4)
    # quit the turtle game program
    screen.bye()

def reset_puz(x, y):
    '''
    Parameters:
        x, y -- the coordinate of onclick point
        
    Use if click on reset button, load same puzzle in right order, update object list
    Returns nothing
    
    '''
    global a
    # almost same procedure as insert image, clear all object before clicking reset
    for each in a.object:
        each.hideturtle()
    a.object.clear()
    a.blank.clear()
    tiles = a.get_tiles()
    # using index in orginal tiles to find the blank image object
    blank_ori = a.get_tiles()[-1]
    blank_i = tiles.index(blank_ori)
    
    for i in range(len(a.flat())):
        t = turtle.Turtle()
        # storing object for each turtle append in list
        a.object.append(t)
        t.hideturtle()
        s = turtle.Screen()
        t.penup()
        center = a.flat()[i]
        # let turtle go to position then add shape on screen
        t.goto(center)
        # getting the tile of each specific image
        name = tiles[i]
        screen.addshape(name)
        t.shape(name)
        t.showturtle()
    # setting list to blank to store the position (x, y) of each object
    turtle_pos = []
    for each in a.object:
        q = each.xcor()
        w = each.ycor()
        pos = (q, w)
        # append each position to blank list
        turtle_pos.append(pos)
    # getting a dictionary key as turtle_pos, value as tiles
    a.random_dict = dict(zip(turtle_pos, tiles))
    blank_location = a.object[blank_i]
    a.blank.append(blank_location)
        
        
def click_button(x, y):
    '''
    Parameters:
        x, y -- the coordinate of click point
        
    Determine whether the user clicks on the designed button
    If not, start trying the swap puzzle play game
    Returns nothing
    
    '''
    # asign variable of coordinate x and y for each button
    x_reset = 80
    y_reset = -260
    x_load = 170
    y_load = -260
    x_quit = 260
    y_quit = -260
    t = turtle.Turtle()
    # if click point inside any button coordinae's range, then do next thing
    if x_reset - 40 < x < x_reset + 40 and y_reset - 40 < y < y_reset + 40:
        # reset button clicked, reset same puzzles on screen
        reset_puz(x, y)
    if x_load - 40 < x < x_load + 40 and y_load - 38 < y < y_load + 38:
        # load button clicked, load another puzzles on screen
        load(x, y)
    if x_quit - 40 < x < x_quit + 40 and y_quit - 26.5 < y < y_quit + 26.5:
        # quit button clicked, quit the game
        quit_puz(x, y)
    # if did not click inside any button's range, then check if the puzzle can be swap
    # then check the win or loose of the game
    else:
        a.win(x, y)


def driver():
    '''
    Auxiliary main function work
    Returns nothing
    
    '''
    # opening animations
    t = turtle.Turtle()
    t.width(4)
    t.speed(10)

    # drawing the area frame of game
    draw_rec(t,-310,300,450,450,"black")
    draw_rec(t,160,300,150,450,"blue")
    draw_rec(t,-310,-200,620,120,"black")
    
    # setting different turtle to word seperately
    t_1 = turtle.Turtle()
    t_2 = turtle.Turtle()
    t_3 = turtle.Turtle()
    
    # loading three button
    load_button(t_1,80,-260,"./Resources/resetbutton.gif")
    load_button(t_2,170,-260,"./Resources/loadbutton.gif")
    load_button(t_3,260,-260,"./Resources/quitbutton.gif")
    
    # write the board title on screen
    write_board()
    
    # if input playername is not equal the string
    if playername != 'no leaderboard Er':
        # show the leaderbord's content on screen
        write_leaderboard()
    
    # insert default puzzle image to start a new game
    a.insert_image()

    # screen click open
    screen.onclick(click_button)
    screen.mainloop()

def main():
    driver()

main()
