name = input("What is your name?")

print("Hello, " + name + ". Time to play Hangman!")

print("Hangman is guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.")

#here we place our secret word that the other player will try to guess
word = "WRONG"

#we need to create an empty string variable, where we will store guesses
guesses = ''
#and set number of wrong turns, otherwise it can never ends
turns = 10

#create a while loop to check if the turns are more than zero
while turns > 0:
    #set counter that starts at zero
    count = 0
    #now we check every letter in our word, we set our word to all lower characters
    for letter in word.lower():
    #check if the letter is in players guesses
        if letter in guesses:
            print (letter)
        else:
        #if not found
            print ("_")
        #increase the wrong counter with one
            count +=1
    if count == 0:
        print ("You win")
        break

    #ask the user go guess a letter, we also convert a guessing letter into lowercase
    guess = input("Guess a letter:").lower() 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
        print ("Wrong guess")  
 
    # how many turns are left
        print ("You have, " + str(turns) + " more guesses")
 
    # if the turns are equal to zero
        if turns == 0:           
            print ("You Lose")