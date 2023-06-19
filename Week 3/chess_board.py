from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HIEGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH/N_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HIEGHT)
    for r in range(N_ROWS):
        for c in range(N_COLS):
            draw_square(canvas, r, c)
    

def draw_square(canvas, r, c): # draw some squares to make a grid
    print(r, c)
    
    color = get_color(r,c)
    x = c * SIZE
    y = r * SIZE
    end_x = x + SIZE
    end_y = y + SIZE
    canvas.create_rectangle(x, y, end_x, end_y,color,'black')

def get_color(r, c): # Get color 
    if is_even(r, c):
        return "black"
    else:
        return "white"
        
def is_even(r, c): # Check if r,c is even or not
    remainder = (r+c) % 2 
    if remainder == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
