low = 1
high = 10000
print("Please think a number between {} and {}".format(low,high))
input("Press ENTER to start")

guesses = 1

while low != high:
    guess = low + (high - low) // 2
    user_input = input("My guess is {}. Please enter h to guess a higher number , l to guess a lower number , c if my guess is right ".format(guess))
    if user_input == "h":
        low = guess + 1
    elif user_input == "l":
        high = guess - 1
    elif user_input == "c":
        print("I got it right in {} guesses and the number is {}".format(guesses,guess))
        break
    else:
        print("Please select either h , l ,c")

    guesses +=  1

else:
    print("You thought of the number {} . I got it in {} guesses ".format(guess,guesses))