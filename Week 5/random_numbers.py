from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 110

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_circle(canvas,50, 50,"blue",SIZE)
    draw_circle(canvas,60,90, "pink", SIZE)
    draw_circle(canvas,100, 30, "gray",SIZE)
    draw_circle(canvas,130,200,"red",SIZE)
    draw_circle(canvas, 130,100, "dodgerblue", SIZE)
    draw_circle(canvas,70, 160, "cyan", SIZE)
    draw_circle(canvas, 60, 230,"purple", SIZE)
    draw_circle(canvas,360,290, "green", SIZE)
    draw_circle(canvas,300,330, "teal", SIZE)
    draw_circle(canvas,370,350, "coral", SIZE)
    draw_circle(canvas,230,345, "gold", SIZE)
    draw_circle(canvas,280,260, "olive", SIZE)
    draw_circle(canvas,220,290, "thistle", SIZE)
    draw_circle(canvas,160,345, "palegreen", SIZE)
    draw_circle(canvas,150,270, "tomato", SIZE)
    
def draw_circle(canvas,center_x, center_y,color,size):
    """
    Draw a circle with a givin location,size, and color.It should be drawn every place.
    """
   
    left_x = center_x - SIZE/2
