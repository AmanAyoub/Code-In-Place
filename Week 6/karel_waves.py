from karel.stanfordkarel import *

def main():
    #put_beeper()
    for i in range(3):
        fill_two()
    put_beeper()
    move()
    put_beeper()
    
    second_row()
    for i in range(3):
        fill_second_row()
    put_beeper()
    move()
    turn_left()
    move()
    turn_left()
    for i in range(10):
        move()
        
    
    
    
    # Put the beeper, move 1 step forward, put beeper and move 2 steps ahead  
def fill_two():
    put_beeper()
    move()
    put_beeper()
    move()
    move()
    
    
def second_row():
    turn_left()
    move()
    turn_left()
    
def fill_second_row():
    put_beeper()
    for i in range(3):
        move()

    
   
def turn_right():
    for i in range(3):
        turn_left()
        
        

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
