from graphics import Canvas
CANVAS_WIDTH = 400
CANVAS_HIEGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HIEGHT)
    drow_Japan_flag(canvas)
    drow_bangladesh_flag(canvas)
    drow_pulau_flag(canvas)
    draw_georgia_flag(canvas)
    
    
    
def drow_Japan_flag(canvas):
    drow_circle(canvas, CANVAS_WIDTH/2, CANVAS_HIEGHT/2, 120, "red")
    
    
def drow_circle(canvas, center_x, center_y, size, color):
    size/2
    left_x = center_x - size/2
    top_y = center_y - size/2
    right_x = left_x + size
    bottom_y = top_y + size
    
    canvas.create_oval(left_x, top_y, right_x, bottom_y,color)
    
    
    
def drow_bangladesh_flag(canvas):
    canvas.create_rectangle(0,0, CANVAS_WIDTH,  CANVAS_HIEGHT, "darkgreen")
    drow_circle(canvas, CANVAS_WIDTH * 0.4, CANVAS_HIEGHT /2, 150, "red" )


def drow_pulau_flag(canvas):
    canvas.create_rectangle(0,0, CANVAS_WIDTH,  CANVAS_HIEGHT, "dodgerblue")
    drow_circle(canvas,CANVAS_WIDTH * 0.4, CANVAS_HIEGHT /2, 150, "yellow")
    
    



def draw_circle(canvas, center_x, center_y, size, color):
    """
    draw a circle on the given canvas. Centered at the given location, in
    the given color
    """
 
    left_x = center_x - size/2
    top_y = center_y - size/2
    right_x = left_x + size
    bottom_y = top_y + size
    canvas.create_oval(left_x, top_y, right_x, bottom_y, color)
    
    
    
    
    
def draw_georgia_flag(canvas):
    
    """
    Draw a flag that has 4 pluses , each corner has 1 plus with given color.
    One big plus should be in the middle of the flag with given color.
    """
    # some calculation for the location of the pluses
    canvas.clear()
    x_left = CANVAS_WIDTH * 1/4
    x_right = CANVAS_WIDTH * 3/4
    y_top = CANVAS_HIEGHT * 1/4
    y_bottom = CANVAS_HIEGHT * 3/4

    # Four call to drow the plus
    draw_plus(canvas,x_left - 20, y_top - 20, x_left + 20, y_top + 20,10, "red")
    draw_plus(canvas,x_right - 20, y_top - 20, x_right + 20, y_top + 20,10, "blue")
    draw_plus(canvas,x_left - 20, y_bottom - 20, x_left + 20, y_bottom + 20,10, "yellow")
    draw_plus(canvas,x_right - 20, y_bottom - 20, x_right + 20, y_bottom + 20,10, "magenta")
    
    # One big background plus
    draw_plus(canvas,0,0,CANVAS_WIDTH, CANVAS_HIEGHT,30,"black")
    
    
    
    
    
def draw_plus(canvas, x_1, y_1, x_2, y_2,width,color):
    """
    Draws a plus which is inscribed in the rectangle defined by the two 
    points (x_1, y_1) and (x_2, y_2). The thickness of each arm of the plus
    is also passed in as a parameter
    """
    mid_x = x_1 + (x_2 - x_1) /2
    mid_y = y_1 + (y_2 - y_1) /2
    
    # Half for pluss thikness
    half = width/2
    canvas.create_rectangle(x_1,mid_y - half,x_2, mid_y + half, color)
    canvas.create_rectangle(mid_x - half, y_1, mid_x + half, y_2, color)
    

    
if __name__ == '__main__':
    main()
