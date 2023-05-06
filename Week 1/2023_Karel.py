from karel.stanfordkarel import *

# Put 20 beepers in (1,1) & put 23 beepers in (1,2).

def main():
    # Put 20 beepers in (1,1) and move 1 step forward
    for i in range(20):
        put_beeper()
    move()
    
    
    # Put 23 beepers in (1,2) and movee 1 step forward
    for i in range(23):
        put_beeper()
    move()
    

if __name__ == '__main__':
    main()
