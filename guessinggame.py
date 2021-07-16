import random
number = random.randint(1, 9)
chances= 0



while chances < 5 :
    guess= int (input("guess a number between 1 and 9"))
    print(guess)

    if guess== number:
        print("congratulations you won")
        break

    elif guess < number:
        print(" your guess was too low, guess a higher number", guess)

    else:
        print(" your guess was too high, guess a lower number", guess)

    chances= chances + 1

if chances >= 5:
    print( " you lose, the number was", number)



    

    
