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

def find_pay_phone()
    print("")

def round3():
    print("""You're pulled over at the bus stop...
            Your hear starts to race! Did you fail the test? Why did he tell you to pull over?
            'Get out of the car,' he says to you. Uh oh... (insert crickets emoji)

            'FIRE DRILL!!!' he shouts.

            'Wait, whaaa...?' you start to question.

            'Car is on fire! Gimmee your phone! You have 10 minutes to find a payphone, call the number on this card, and get your tail back here...
            or else... BOOM! The car explodes!
            ...oh and if that happens, you FAIL the test! Hope you like having your momma drive you around!'

            You quickly glance at the card he slapped in your hand:
                Bob Brown
                Driver's License Examiner
                U.S. Marines Veteran
                555-555-5555

            'What are you waiting for?!' he shouts, sounding like a drill sargeant.

            """)
    answer = input("""
                        What are you going to do?
                        Op 1:
                        Op: 2
                        Op3:..
                        """)
    if "1" in answer:
        gameover()
    elif "2" in answer:
        find_pay_phone()
    elif "3" in answer:
        find_cell_phone()
    else:
        gameover()

round3()
