from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    
    # Face nort, fill the 1st column
    build_column()
    
    
    # Turn east, move 4 steps forward
    another_column()
    
    
    # Turn down, fill the 5th column
    step_down()
    
    
    # Turn east, move 4 steps forward
    other_column()
    
    
    # Face north, fill the 9th column
    build_column()
    
    
    # Turn east, move 4 steps forward
    another_column()
    
    
    # Face south, fill the 13th column
    step_down()
    
    
    # Turn east to finish the puzzel
    turn_left()
    

def build_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
    
def another_column():
    turn_right()
    for i in range(4):
        move()
    
    
def step_down():
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
    
def other_column():
    turn_left()
    for i in range(4):
        move()
    
    
def turn_right():
    for i in range(3):
        turn_left()
        
if __name__ == '__main__':
    main()
