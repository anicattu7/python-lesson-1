# enter the secret number
secret = 7

# enter the guess number
while(True):
    guess = int(input("Enter your guess here: "))

    # if both numbers are same-congrats, else print wrong number
    if secret == guess:
        print("You got it right!!! You won!!!")
    else:
        ans = input("Wrong guess.. Wanna try again? y/n ")
        if ans == "y":
            continue
        else:
            break
    break


