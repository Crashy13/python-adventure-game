import sys
import time

def slowprint(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 200)

def game_over():
    print("Game over!")
    play_again()

def play_again():
    print("Would you like to try again from your save point?, y/n?")
    answer = input().lower()
    if "y" in answer:
        select_car()
    elif "n" in answer:
        exit()
    else:
        print("Please enter y for yes or n for no")
        play_again()


def select_car():
    slowprint('''
    Okay, then! Now you have to do something really cool.
    You can choose your car!
    Choose your car:
    1.Porshe
    2.BW1918
    3.Tandem bicycle
    ''')
    result = input()

    if result == "1":
        print("What can I say. You have an expensive taste. Good work")
    elif result == "2":
        print("Wow! I don't know what to say. Good luck with it")
    elif result == "3":
        print("What did you come to get again? Bicycle lessons? Get out of here.It is GAME OVER for you")
        game_over()
    introduce_yourself()


def introduce_yourself():
    slowprint('''
     This is really important part.
     You should make a first impression.
     You instructor is really interesting man.
      1.Hi, I am an octopus man
      2.Hi, my name is Rick.
      3.Hi, I am Rick. How are you doing today''')
    result = input()

    if result == "1":
        print("Ha... Who would known. Your examiner loves Rick and Morty show. You made him laugh and know you have some good bond. Good Job!")
    elif result == "2":
        print("Hmmm... You made a really interesting impression on your examiner. He laught but you can see that he got a little bit confused, and maybe even concerned")
    elif result == "3":
        print("REALLY BORING! But it how it goes. You made FINE impression. NICE(boring)")

    make_a_joke()

def make_a_joke():
    slowprint('''You finally got inside the car.
     You strapped in and started the car.
      Suddenly you felt a very unpleasant smell.Oh, your examiner farted.
      Ops. Now, what are you going to do about it?
      1.You can make a stupid joke as "oh, geez... isn't to early for P.F Chang's,
      2. You can roll down your window,
      3.Just ignore it''')
    result = input()

    if result == "1":
        print("That was BAD! You just made the situation worse...Examiner blocked the windows and now you have to drive in this smelly car")
    elif result == "2":
        print("Passive aggressive action. Nice! Now we know what kind of person you are")
    elif result == "3":
            print("Best thing you could possibly do. GOOD JOB. You got some more \"I like you\" points from examiner")

    first_light()

def first_light():
    slowprint('''
     Good.
     Now you are finally driving.
     Your first task is red light.
     What can possibly go wrong, right?
     Well...Surprise! You can see the red light, and you are about to stop.
     BUT! Right across the street you can see Leonardo Dicaprio.
     OH! That is just crazy! What you do?
     1.You don't who he is and just stop at the red light
     2.You hit gas and you skip the red light to say hi to Leonardo Dicaprio because you a BIG fan
     3.You open a door of your car and just run to him with open arms
     4.You are being patient. You just wait until green light and then you drive to Leonardo''')
    result = input()

    if result == "1":
         print("WHAT? How? WHAT? Okay, this is just ridiculous! GAME OVER just from me")
         game_over()
    elif result == "2":
        print("Okay, it wasn't the best choice because you ran over a grandma who was crossing the road. Too much... Sorry. GAME OVER")
        game_over()
    elif result == "3":
        print("interesting. You left your instructor alone in the car. BUT! Do you remember that your examiner is an interesting man? Because something crazy happened. He ran to hug Leo with you. After hugging Leo, you just went back to the car with big smiles. Good work")
    elif result == "4":
        print("Well. That is a good decision but you miss Leo and now you are sad. Anyway, you pass")

    stop_at_the_bus_station()

def stop_at_the_bus_station():
    slowprint('''
    You are driving by a bus station and your examiner asks you to stop there.
    Your action?
    1. You do stop
    2. You don't stop
    ''')
    result = input()

    if result == "1":
       print("Good job! You pass!")
    elif result == "2":
        print("I guess you should listen to your examiner. GAME OVER")
        game_over()


select_car()
