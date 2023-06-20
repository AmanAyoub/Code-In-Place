import graphics

def main():
    # makes a canvas
    canvas = graphics.create_canvas(300, 300)
    
    # create 20 squares and repeat them
    for i in range(30):
        value = i * 10
        left_x = value
        top_y = value
        right_x = left_x + 10
        bottom_y = top_y + 10
    
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
        
    print(i)
        
if __name__ == '__main__':
    main()
