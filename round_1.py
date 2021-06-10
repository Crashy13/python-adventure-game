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
        print("You walk towards the back of the building, seeing no one in sight. As you turn the corner, you see a door at the rear entrance. Maybe it's unlocked! As you head towards the door, you hear a growl to your left. You turn to the source of the noise and see a pack of 5 wolves glaring at you.\n What do you do now?\n 1. Fight! Wolves are no match for you!\n 2.Run! You didn't sign up for this!")

        choice = input()

        if '1' in choice:
            print("Seriously, you thought you could take on 5 wolves? You've severely overestimated your skills.")
            game_over()
        elif '2' in choice:
            print("Some may call you a coward, but you survived. Good thing they decided not to chase you for reasons you'll never know because it wasn't written in the script. As you come back around to the front, you notice that the doors are open. Maybe waiting would have been the better choice. As you walk into the building, the man at the front desk greets you with a warm smile. He leads you to the back and hands you a paper and pencil. You sit down and look at the test.\nQuestion 1:\n How many tires does a normal car have?\n 1. 2\n 2. 4\n 3. 3\n 4. 1")

            choice = input()
            if '2' in choice:
                 print("Great job! You passed! Please go outside to meet your instructor.")
            else:
                print("Come on, this is basic knowledge anyone should know.")
                game_over()



    elif '4' in choice:
        print("This must be a sign that you aren't ready. Better go back home and keep on practicing.")
        game_over()
    else:
        print("Choose one of the options provided")












start_game()
