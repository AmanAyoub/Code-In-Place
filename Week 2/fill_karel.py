from karel.stanfordkarel import *
    # Karel should fill the world with beeprs.
def main():
    
    """
    Fill 4 rows with using 3 functions named fill_low, turn_back, and step_up in while loop.
    """
    while left_is_clear():
        fill_row()
        turn_back()
        step_up()
    
    fill_row()
    
        
    # Difine a function to fill the rows
def fill_row():   
   while front_is_clear():
       put_beeper()
       move()
   put_beeper() 
    

    # Difine a function to step up and move to the other rows
def step_up():
  # turn right
    for i in range(3):
        turn_left()
    move()
  # turn right
    for i in range(3):
        turn_left()
   
   
    # Difine a function to come back to the left side after filiing the row
def turn_back():
    for i in range(2):
        turn_left()
        while front_is_clear():
            move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
