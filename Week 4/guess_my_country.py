from graphics import Canvas
    
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 500
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO: your code here!
    
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    rec = canvas.create_rectangle(40, 50,250,450,)
    rec1 = canvas.create_rectangle(250,50,460,450, 'red')
    rec3 = canvas.create_rectangle(460,50,670,450,  
    'green')
    image = canvas.create_image(200,170, "flag.png" )
    

    name = "Afghanistan"
    print('This is the flag of my country')
    guess = input("Guess my country's name: ")
    while guess != name:
       print("Incorrect!")
       guess = input("Guess my country's name: ") 
    print("Great work!\nMy country is Afghanistan. ")
    
if __name__ == '__main__':
    main()
