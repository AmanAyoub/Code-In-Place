import random

def main():
    print("Khansole Academy")
    print("Let's start with addition!")
    NUM1 = 10;
    NUM2 = 99;
    CORRECT = 3;
    streak = 0;
    while (streak < CORRECT):
        first_number = random.randint(10,99);
        second_number = random.randint(10,99);
        user_response = int(input("What is " + str(first_number) + " + " + str(second_number) + "? "));
        summary = first_number + second_number;
        
        if (user_response == summary):
            streak += 1;
            print("Correct! You've gotten " + str(streak) + " correct  in a row")
            
        while (user_response != summary):
            print("Incorrect! The expected answer is " + str(summary))
            user_response = int(input("What is " + str(first_number)
            + " + " + str(second_number) + "? "));
    print("Congratulations! You mastered addition.")
    print("==============================")
    
    Correct = 3
    streak = 0
    print("It's time to learn subtruction!")
    while (streak < CORRECT):
        num = random.randint(NUM1,NUM2);
        num2 = random.randint(NUM1,NUM2);
        user_response = int(input("What is " + str(num) + " - " + str(num2) + "? "));
        answer = num - num2        
   
        if (user_response == answer):
            streak += 1;
            print("Correct! You've gotten " + str(streak) + " correct  in a row")
    
        while (user_response != answer):
            print("Incorrect! The expected answer is " + str(answer))
            user_response = int(input("What is " + str(num)
            + " - " + str(num2) + "? "));
    print("Congratulations! You mastered subtruction.")
    print('============================= ')
    
    
    yes = input("Do you want to continue? ")
    yes = True
    if yes == True:
        Correct = 3
        streak = 0
        print("It's time to learn multiplication!")
        while (streak < CORRECT):
            mal = random.randint(NUM1,NUM2);
            mal2 = random.randint(NUM1,NUM2);
            user_response = int(input("What is " + str(mal) + " * " + str(mal2) + "? "));
            ans = mal * mal2        
       
            if (user_response == ans):
                streak += 1;
                print("Correct! You've gotten " + str(streak) + " correct  in a row")
        
            while (user_response != ans):
                print("Incorrect! The expected answer is " + str(ans))
                user_response = int(input("What is " + str(mal)
                + " * " + str(mal2) + "? "));
        print("Congratulations! You mastered multiplication.")
        print("==========================")
    else:
        print("  ")
        
        
    yes = input("Wohoo,you're rocking!!!" + "Do you want to master division? ")
    yes = True
    if yes == True:
        Correct = 3
        streak = 0
        while (streak < CORRECT):
            div = random.randint(NUM1,NUM2);
            div2 = random.randint(NUM1,NUM2);
            user_response = int(input("What is " + str(div) + " / " + str(div2) + "? "));
            response = div // div2
       
            if (user_response == response):
                streak += 1;
                print("Correct! You've gotten " + str(streak) + " correct  in a row")
        
            while (user_response != response):
                print("Incorrect! The expected answer is " + str(response))
                user_response = int(input("What is " + str(div)
                + " / " + str(div2) + "? "));
        print("Congratulations! You mastered division.")
        print("==============================")
    else:
        print(" ")

if __name__ == '__main__':
    main()
