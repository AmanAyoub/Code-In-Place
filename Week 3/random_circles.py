from graphics import Canvas
import random

# Draw some circles with random colors
# Set canstants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CIRCLE_SIZE = 100
CIRCLE_NUM = 20

def main():
    # Setup
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    for i in range(CIRCLE_NUM):
        draw_1_circle(canvas)
def draw_1_circle(canvas):
    start_x = random.randint(0,CANVAS_WIDTH)
    start_y = random.randint(0,CANVAS_HEIGHT)
    end_x = start_x + CIRCLE_SIZE
    end_y = start_y + CIRCLE_SIZE
    circle = canvas.create_oval(start_x, start_y, end_x, end_y,random_color(canvas))
    print(start_x, start_y)
   
def random_color(canvas):
    colors = ['red','blue','yellow','green','orange','teal',
                'cyan','maroon','darkblue','salmon','purple',
                'brown','coral','lemon',]
    return random.choice(colors)
    
if __name__ == '__main__':
    main()
