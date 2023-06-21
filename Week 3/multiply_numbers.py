"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    user = int(input("Enter first number: "))
    user2 = int(input("Enter second number: "))
    sam = user * user2
    print(sam)

   
   
   
#This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
