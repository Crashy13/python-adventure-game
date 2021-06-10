car = ""

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

def select_car():
    result = input('''
    Okay, then! Now you have to do something really cool.
    You can choose your car!
    Choose your car:
    1.Porshe, 2.URAL, 3.Tandem bicycle
    ''')

    if result == "1":
        print("What can I say. You have an expensive taste. Good work")
    elif result == "2":
        print("Wow! You have a little Russian in you.Good luck driving it")
    elif result == "3":
        print("What did you come to get again? Bicycle lessons? Get out of here.It is GAME OVER for you")
        game_over()
    introduce_yourself()


def introduce_yourself():
    result = input('''This is really important part.
     You should make a first impression.
     You instructor is really interesting man.
      1.Hi, I am an octopus man,
      2.Hi, my name is Rick and I have only one testicle. Do I need two to drive,
      3.Hi, I am Rick. How are you doing today''')

    if result == "1":
        print("Ha... Who would known. Your examiner loves Rick and Morty show. You made him laugh and know you have some good bond. Good Job!")
    elif result == "2":
        print("Hmmm... You made a really interesting impression on your examiner. He laught but you can see that he got a little bit confused, and maybe even concerned")
    elif result == "3":
           print("REALLY BORING! But it how it goes. You made FINE impression. NICE(boring)")

    make_a_joke()

def make_a_joke():
    result = input('''You finally got inside the car.
     You strapped in and starded the car.
      Suddenly you felt a very unpleasant smell.Oh, your examiner farted.
      Ops. Now, what are you going to do about it?
      1.You can make a stupid joke as "oh, geez... isn't to early for P.F Chang's,
      2. You can roll down your window,
      3.Just ignor it''')

     # if result == "1":
     #        print("")
     # elif result == "2":
     #        print("")
     # elif result == "3":
     #        print("")



select_car()
