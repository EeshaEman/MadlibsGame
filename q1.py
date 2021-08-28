import random
# i= int(input("enter your choice between 1 and 2 :"))
# def choice(i):
#     if i == 1:
#      print("{guess(20)}")
#     elif i == 2:
#        print(computer_guess(20))



def guess(range):
    random_number = random.randint(1, range)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input("enter a number between 1 and " + str(range) + ":"))
        count = count + 1
        if guess > random_number:
            print("your number is too high enter again")

        elif guess < random_number:
            print("your number is too low enter again")



    print("YESS! congrats finally you guessed the number And you enter guess number by " + str(count) + " times ")

# guess(10)

def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback = ""
    count = 0
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input("if  the  number  " + str(guess) + " is too high then enter (h) and is too low then enter (l) ")
        count = count + 1
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print("thankGod ! computer bot guess number correctly And computer bot guess number by " + str(count) + " times ")

computer_guess(100)