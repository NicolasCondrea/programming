"""
Title: Gibberish Game
Author: Nicolas Condrea
Date: 07/10/2019
"""

# Variables
answer_1 = True
answer_2 = True
vowels = "aeiouAEIOU"
restart = True
quit = True

# Program explanation
print("Purpose of the program is to translate words from English to Gibberish!")

# Program loop
while restart == True:
    # Loop for error checking
    while answer_1 == True:
        user_input = input("Enter your first gibberish syllable: ")

        # This for loop checks
        for i in range(len(user_input)):
            '''
                This segment of code uses the ord function which converts the letters into ascii
                numbers which checks to see if the user entered a legitimate character
            '''
            if ord(user_input[i])>=97 and ord(user_input[i])<=122 or ord(user_input[i])>=65 and ord(user_input[i])<=90:
                answer_1 = False
                break
            else:
                print("Input must be a character! Please reenter: ")

    # This loop translates the syllable and word into gibberish
    while answer_2 == True:
        user_word = input("Please enter a word to be translated: ")
        Translated_word = []
        for i in range(len(user_word)):
            if user_word[i] in vowels:
                Translated_word.append(user_input)
                Translated_word.append(user_word[i])
            else:
                Translated_word.append(user_word[i])
                answer_2 = False

    # The following code prints the gibberish word
    gibberish_word = "".join(Translated_word)
    print(("Your final word is: ") + gibberish_word)

    # This segment of code asks the user if they want to play again and provides error checking
    while quit == True:
        user_input1 = input("Would you like to play again? Enter yes or no:\n ")
        if user_input1 == "no":
            restart = False
            quit = False
            print("Thanks for playing")
        elif user_input1 == "yes":
            restart = True
            quit = False
        else:
            print("You have not selected a valid option. Please re-enter (yes/no)")
            quit = True
