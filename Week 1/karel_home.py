from karel.stanfordkarel import *

# Karel should pick the beeper and resturn to her starting point.

def main():
    
    # Turn down and move to the 3th street
    step_down()
    
    
    # To face east
    turn_left()
    
    
    # Move 3 steps forward, pick the beeper
    move_to_wall()
    
    
    # Face west, move 3 steps forward
    return_back()
    
    
    # Turn right, move 1 step up and face east
    step_up()
    
def step_up():
    turn_right()
    move()
    turn_right()
    
    
def return_back():
    pick_beeper()
    turn_left()
    turn_left()
    move_to_wall()


def step_down():
    turn_right()
    move()
def move_to_wall():
    for i in range(3):
        move()


def turn_right():
    for i in range(3):
        turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
