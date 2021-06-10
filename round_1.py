def start_game():

    def game_over():
        print("Game over!")
        play_again()

    
    def play_again():
        print("Would you like to try again, y/n?")
        answer = input()
        if "y" in answer:
            start_game()
        elif "n" in answer:
            exit()
        else:
            print("Please enter y for yes or n for no")
            play_again()

    print("It's finally the big day! Time to get your driver's license! You were so excited last night you hardly slept, but you've been preparing for this day all your life. As your older brother drives you up to the DMV, you notice that it says it opens at 8 am, but it's now 8:05 and the doors are still locked!\n You can choose to\n 1. Attempt to break in...\n 2. Wait patiently\n 3. Check the back door\n 4. Curse your luck and go home\n What do you do?")

    choice = input()

    if '1' in choice:
        print('You win')
    elif '2' in choice:
        print('You win')
    elif '3' in choice:
        print('You win')
    elif '4' in choice:
        print("This must be a sign that you aren't ready. Better go back home and keep on practicing.")
        game_over()








start_game()
