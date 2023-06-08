from turtle import Turtle, Screen
import turtle
import logging
import time

def write_board():
    '''
    Write 'Leaders' on screen
    Return None
    '''
    t = Turtle()
    t.hideturtle()
    t.up()
    t.color('blue')
    # the position set
    t.goto(165,265)
    t.down()
    t.write("Leaders:", font = ['Arial', 20, 'normal'])
    
def write_leaderboard():
    '''
    Write information from leadertext on canvas 
    Return None
    '''
    try:
        # try open leadertext file to get winner's information
        t = Turtle()
        t.hideturtle()
        t.color('blue')
        # setting original number equal 0
        ny = 0
        with open('leadertext.txt', mode = 'r', encoding = 'utf-8') as f:
            # using for loop to update the ori number
            # to change the positionon canvas every line go to
            for line in f:
                t.up()
                t.goto(165, 210 - ny * 30)
                t.down()
                t.write(f"{line}", font = ['Arial', 15, 'normal'])
                ny += 1
    # if can not open, record the error in 5001_puzzle.err.txt
    except Exception as Argument:
        t = turtle.Turtle()
        s = turtle.Screen()
        # also show hint image on screen
        s.addshape("Resources/leaderboard_error.gif")
        t.shape("Resources/leaderboard_error.gif")
        time.sleep(2)
        t.hideturtle()
        f = open("5001_puzzle.err.txt", "a")
        f.write(str(Argument))
        f.close()

    
def leaderboard(playername, move):
    '''
    Wirte down winner's information in leadertext file
    Return None
    '''
    # open winner's information txt file to append the update information
    with open('leadertext.txt', mode = 'a', encoding = 'utf-8') as f:
        element = f"{move}: {playername}"
        f.write(element + "\n")
