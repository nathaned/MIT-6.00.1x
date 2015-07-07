print "Please think of a number between 0 and 100!"

top = 100
bottom = 0
guess = (top + bottom) / 2

while (not top == bottom):
    print "Is your secret number " + str(guess) + "?"
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (str(ans) == 'h'):
        top = guess
        guess = (top + bottom) / 2
    elif (str(ans) == 'l'):
        bottom = guess
        guess = (top + bottom) / 2
        if (bottom == guess):
            guess = top
    elif (str(ans) == 'c'):
        break
    else:
        print "Sorry, I did not understand your input."

    #print "top: " + str(top) + "  bottom: " + str(bottom) + "  guess: " + str(guess)

print "Game over. Your secret number was: " + str(guess)
