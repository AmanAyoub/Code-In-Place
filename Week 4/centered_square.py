from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUARE_SIZE = 100

def main():
    # create canvas
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    
    # find the middle of canvas
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    
    # calculate the left and to top left corner of the square
    left_x = middle_x - SQUARE_SIZE/2
    left_y = middle_y - SQUARE_SIZE/2
    
    # calculate the right and bottom of the square
    right_x = middle_x + SQUARE_SIZE/2
    right_y = middle_y + SQUARE_SIZE/2
    
    
    # create square in the middle of canvas
    canvas.create_rectangle(right_x,left_y , left_x,right_y , 'blue')
    
    
if __name__ == '__main__':
    main()
