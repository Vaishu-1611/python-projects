import random
print("""Welcome to the Number Guessing Game.
You will have 10 chances.
You have 1 number to be guessed.
The secret number is between 1 - 50""")
attempts = 10
secret_num = random.randint(1, 50)
is_guess_correct:False
num = 1
while num <=10 :
    print(f"You have {attempts} attempts left!")
    user_number = int(input("enter a number between 1 - 50: "))
    if user_number == secret_num:
        print("Congratulations! You guessed the number correctly")
        is_correct_guess = True
        break
    else:
        if user_number < secret_num:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"You guess is wrong ,try {higher_or_lower} number")
    num +=1
    attempts -= 1