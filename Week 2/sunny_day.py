# Make a spring veiw with the blue sky, sun , and trees on earth's surface in graphics.

from graphics import Canvas
 # Make constant variables   
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 400
SIZE = 50
def main():
    # Call the functions made for every shape
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    make_2_background_rects(canvas)
    make_circle(canvas,CANVAS_WIDTH/2 - SIZE/2,SIZE,SIZE,"yellow")
    make_tree(canvas,50,CANVAS_HEIGHT-140)
    make_tree(canvas,149,CANVAS_HEIGHT-140)
    make_tree(canvas,299,CANVAS_HEIGHT-140)
    make_tree(canvas,399,CANVAS_HEIGHT-140)
    
    # Draw 2 rectangles for blue sky and gruss
def make_2_background_rects(canvas):
    left_x = 0
    top_y = 0
    right_x = left_x + CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT - 100
    canvas.create_rectangle(left_x,top_y,right_x,bottom_y,'darkblue')
    canvas.create_rectangle(left_x, CANVAS_HEIGHT-100, right_x, bottom_y + CANVAS_WIDTH,"green")
   # Draw a tree trunk and call the function four times which was made for small circles 
def make_tree(canvas,left_x,top_y):
    right_x = left_x + 23
    bottom_y = top_y + 40
    canvas.create_rectangle(left_x,top_y,right_x,bottom_y,"coral")
    circly(canvas,42,240)
    circly(canvas,140,240)
    circly(canvas,290,240)
    circly(canvas,390,240)
    # Draw a circle in size of 40 pixels
def circly(canvas,start_x,start_y):
    size = 40
    right_x = start_x + size
    bottom_y = start_y + size
    canvas.create_oval(start_x,start_y,right_x,bottom_y,"yellow")
    print(start_x, start_y)
    # Draw a circle for the sun's shape
def make_circle(canvas,start_x,start_y,size,color):
    left_x = start_x
    top_y = start_y
    right_x = left_x + size
    bottom_y = start_y + size
    return canvas.create_oval(left_x,top_y, right_x, bottom_y,color)
    


    
    
if __name__ == '__main__': 
    main()
