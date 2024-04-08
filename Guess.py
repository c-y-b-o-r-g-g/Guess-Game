import random



def isfloat(x):
    try:
        float_n = float(x)
    except ValueError:
        return False
    else:
        return True



number = random.randint(1,100)
success = False
print("The Number is From 1 to 100")
while success == False:
    user_choice = (input("Guess the number:"))
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if(user_choice == number):
            print("Correct !")
            success = True
        elif (user_choice < number):
            print("Too Low")
        elif (user_choice>number):
            print("Too High")
    elif isfloat(user_choice):
        print("Number is not a Floating Point")
    else:
        print("Enter a Valid Number")