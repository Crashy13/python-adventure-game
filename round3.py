import sys
import time

def round3():
    def slowprint(s):
        for c in s + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1.0 / 60)

    def game_over():
        print("Game over!")
        play_again()

    def play_again():
        print("Would you like to try again from your last save point?, y/n?")
        answer = input().lower()
        if "y" in answer:
            round3()
        elif "n" in answer:
            exit()
        else:
            print("Please enter y for yes or n for no")
            play_again()


    sections = {
        'bus_stop': {'text': """You're pulled over at the bus stop... \U0001F68C \U0001F6D1\n Your \U0001F49B starts to race! Did you fail the test? Why did he tell you to pull over? \U0001F633\n 'Get out of the car,' he says to you. Uh oh... \U0001F648\n 'FIRE DRILL!!!' he shouts. \U0001F525 \U0001F525 \U0001F525  Wait, whaaa...?' you start to question.\n 'Car is on fire! Gimmee your phone! You have 10 minutes to find a payphone, call the number on this card, and get your tail back here... or else... BOOM! The car explodes! \U000023F0 \U0001F4A5\n ...oh and if that happens, you FAIL the test! Hope you like having your momma drive you around!'\n You quickly glance at the card he slapped in your hand:\n Bob Brown\n Driver's License Examiner\n 555-555-5555\n 'What are you waiting for?!' he shouts!\n '9 minutes 27 seconds' he says again. You now notice he's holding a stop watch! This guy's not messing around...\n What do you do???\n\n 1. You're in your best suit (always gotta be lookin' fly!), you're not gonna get it sweaty! Take the bus back to the DMV.\n\n 2. Run like the wind!!! \U0001F3C3 \U0001F32C \n A driver's license = freedom! Challenge accepted!\n\n 3. Do payphones even exist any more?? There's gotta be someone nearby with a cell phone you can borrow and pretend it's a pay phone."""},

        'find_pay_phone' : {'text': """You take off running! Your belly starts to rumble... uh oh... Maybe the Cheetos you had for breakfast weren't a good idea... \U0001F922 More rumbles... your mind starts to scatter from the mission. You need a bathroom ASAP!\n What do you do???\n 1. Driver's License or Bust! You keep running & risk an "accident"!\n 2. Find a bathroom first!"""},

        'keep_running': {'text': """...\U0001F3C3 ...\U0001F3C3 ...\U0001F3C3 ...Like an oasis in the dessert, you see in the distance what appears to be a payphone! You run to the phone, pick up the receiver, and start to punch in the number on the card... Nothing happens.\n \U0001F997 \U0001F997 \U0001F997 \n You were born in 2005! You've never used one of these antiquated things before...\n P-A-Y Phone...\n You reach for your wallet to take out your mom's credit card, and then notice the empty slot with 25¢ written next to it.'Does anyone even carry coins anymore?!'\n What do you do???\n 1. You see an old lady a block away. Old people love coins. She's gotta have 25¢ on her, right???\n 2. You start searching on the ground for dropped coins"""},

        'techy_old_lady': {'text': """You run up to the old lady, and ask her if she has a quarter she can spare!\n She starts laughing!\n "Does anyone even carry coins anymore?" she says.\n "I only use Apple Pay! \U0001F4F1 Sorry kid..." """},

        'collect_call': {'text': """You start searching the ground for dropped coins\n ...then out of the corner of your eye you notice a worn sticker on the payphone:\n "1-800-COLLECT" \U0001F4DE\n You punch in the number.\n The examiner accepts the collect call!"""},

        'portapotty' : {'text': """You find a port-a-potty nearby! SCORE!\n Content with your decision to make a quick bathroom trip, you go to unlock the door to exit, and find that the lock is stuck and you can't open the door! By the time you finally are able to bust the door open, you find that the sun has set, and your test examiner is no where to be found! Talk about a crappy situation, better luck next time!!""" },

        'find_cell_phone': {'text': """You start running away from the car, once it's out of sight,\n you start looking for signs of life! \U0001F9D0\n Where are all the people when you need them?!\n Suddenly, you spy two people!\n To your left: An old lady who must be close to 100 years old!\n To your right: A baby boomer hippie, wearing a tie-die 'Save the Trees' shirt and Birkenstocks.\n What are the odds that EITHER of these interesting characters have a cell phone on them?\n Time is running out!\n Who are you going to pick???\n\n 1. The Old Lady\n\n 2. The Hippie\n """ },

        'grandmas_phone': {'text': """You approach the old lady, and ask her if she has a cell phone that you could use.\n "Aren't you precious!" she says. "Of course I have a cell phone, it's the 21st century! How else am I going to stream Netflix on the go?" \U0001F4F1\n She hands you her cell phone, and you punch in the number on the card...\n Ring... ring...\n "Hey Grandma!" the examiner answers.\n "Grandma? Huh? Bob, it's me. I found a payphone. Mission accomplished, right?"\n "You're not on a payphone...\n You're on my GRANDMOTHER's cellphone!!\n You FAIL!" """},

        'hippies_phone': {'text': """You approach the hippie, and ask him if he has a cell phone that you could use.
        "You kidding me?" she says. "Of course I have a cell phone, it's the 21st century! How else am I going to stream Netflix on the go? \U0001F4F1\n He hands you his cell phone, and you punch in the number on the card...\n Ring... ring...\n "Talk to me," your examiner answers.\n "Bob, it's me. I found a payphone. Mission accomplished, right?" """},

        'round_won': {'text': """Well done kid," he says, "you have 2 minutes and 38 seconds to be back in the driver's seat."\n You hang up the phone and take off running! \U0001F3C3 \n You get back to the car, your clothes drenched with sweat from sprinting, leap into the driver's seat, and fasten your seat belt.\n "Mission accomplished," he says.\n You start the engine, and he says to you,\n "We need to get gas, pull over at the gas station 2 miles up on the left..."\n """},

        'invalid_choice': {'text': "Please choose a choice provided"}
    }

    choices = ['1', '2', '3',]

    while True:
            slowprint(sections['bus_stop']['text'])

            choice = input()

            if choice == choices[0]:
                game_over()
                break

            elif choice == choices[1]:
                slowprint(sections['find_pay_phone']['text'])

                choice = input()

                if choice == choices[0]:
                    slowprint(sections['keep_running']['text'])

                    choice = input()

                    if choice == choices[0]:
                        slowprint(sections['techy_old_lady']['text'])
                        game_over()
                        break

                    elif choice == choices[1]:
                        slowprint(sections['collect_call']['text'])
                        slowprint(sections['round_won']['text'])
                        break

                    else:
                        slowprint(sections['invalid_choice']['text'])

                elif choice == choices[1]:
                    slowprint(sections['portapotty']['text'])

                    game_over()
                    break

                else:
                    slowprint(sections['invalid_choice']['text'])

            elif choice == choices[2]:
                slowprint(sections['find_cell_phone']['text'])

                choice = input()

                if choice == choices[0]:
                    slowprint(sections['grandmas_phone']['text'])
                    game_over()
                    break

                elif choice == choices[1]:
                    slowprint(sections['hippies_phone']['text'])
                    slowprint(sections['round_won']['text'])
                    break
                else:
                    slowprint(sections['invalid_choice']['text'])

            else:
                slowprint(sections['invalid_choice']['text'])

round3()
