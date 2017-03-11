import random

def main():
    print("You enter a 4 digit number and if you guess the place and the number \ncorrectly you get a bull if you get the number correct but\nnot place the you get a cow")
    number = str(random.randint(1000,9999))
    guesses = 0
    while True:
        guesses+=1
        guess = input("Enter a 4 digit number ")
        if guess==number:
            print("Congratulations you guessed it correctly in",guesses, "tries")
            break
        bulls = cows = 0
        for i in range(len(number)):
            if number[i]==guess[i]:
                bulls+=1
            elif guess[i] in number:
                cows+=1
        print("Bulls "+str(bulls)+" Cows "+ str(cows))

main()