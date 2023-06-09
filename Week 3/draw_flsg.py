from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_indonesian_flag(canvas)
    
    
    # Create Indonesian flag
def draw_indonesian_flag(canvas):
        canvas.create_rectangle(0, 0, 450, 150, "red")

if __name__ == '__main__':
    main()
