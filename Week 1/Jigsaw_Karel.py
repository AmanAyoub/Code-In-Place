from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():

  # Move 2 steps forward, pick the beeper and move ahead
  take_beeper()
  
  
  # Turn to north, move 2 steps up and put the beeper in (3,4)
  step_up()
  
  
  # Turn around and move 2 steps down
  step_down()
  
  
  # Face to west, move 3 steps forward and turn to east 
  move_to_wall()
  

  
def take_beeper(): 
    while no_beepers_present():
       move()
    pick_beeper()
    move()
    
   
def step_up():
    turn_left()
    for i in range(2):
        move()
    put_beeper()
   
   
def step_down():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


def move_to_wall():
    turn_right()
    for i in range(3):
        move()
    turn_back()
    
    
    
def turn_back():
    for i in range(2):
        turn_left()
    
    
def turn_right():
    for i in range(3):
        turn_left()
 

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
