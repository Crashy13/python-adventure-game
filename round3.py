import sys
import time

examiner = {"first_name": "Bob", "last_name": "Brown", "occupation": "Driver's License Examiner", "phone_number": "555-555-5555"}

def slowprint(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 20)

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


def find_cell_phone():
    slowprint("""You start running away from the car, once it's out of sight,
    you start looking for signs of life! \U0001F9D0
    Where are all the people when you need them?!

    Suddenly, you spy two people!
    To your left: An old lady who must be close to 100 years old!

    To your right: A baby boomer hippie, wearing a tie-die 'Save the Trees' shirt and Birkenstocks.

    What are the odds that EITHER of these interesting characters have a cell phone on them?

    Time is running out! Who are you going to pick???

    1. The Old Lady
    2. The Hippie """)
    print("Enter: 1 or 2.")
    answer = input()

    if "1" in answer:
        slowprint("""You approach the old lady, and ask her if she has a cell phone that you could use.

        "Aren't you precious!" she says. "Of course I have a cell phone, it's the 21st century! How else am I going to stream Netflix on the go?"

        She hands you her cell phone, and you punch in the number on the card...

        Ring... ring...

        "Hey Grandma!" the examiner answers.

        "Grandma? Huh? Bob, it's me. I found a payphone. Mission accomplished, right?"

        "You're not on a payphone, you're on my GRANDMOTHER's cellphone!! You FAIL!" """)
        game_over()

    elif "2" in answer:
        slowprint("""You approach the hippie, and ask him if he has a cell phone that you could use.
        "You kidding me?" she says. "Of course I have a cell phone, it's the 21st century! How else am I going to stream Netflix on the go?

        He hands you his cell phone, and you punch in the number on the card...

        Ring... ring...

        "Talk to me," your examiner answers.

        "Bob, it's me. I found a payphone. Mission accomplished, right?" """)
        gas_station()


def gas_station():
    slowprint("""Well done kid," he says, "you have 2 minutes and 38 seconds to be back in the driver's seat."
    You hang up the phone and take off running! \U0001F3C3

    You get back to the car, your clothes drenched with sweat from sprinting,
    leap into the driver's seat, and fasten your seat belt.

    "Mission accomplished," he says.
    You start the engine, and he says to you,
    "We need to get gas, pull over at the gas station 2 miles up on the left."
    "You pull into the gas station and park the car..." """)


def find_pay_phone():
    slowprint("""You take off running! Your belly starts to rumble... uh oh... Maybe the Cheetos you had for breakfast weren't a good idea... \U0001F922
    More rumbles... your mind starts to scatter from the mission. You need a bathroom ASAP!

    What do you do???

    1. Driver's License or Bust! You keep running & risk an "accident"!

    2. Find a bathroom first!""")
    print("Enter: 1 or 2.")
    answer = input()

    if "1" in answer:
        slowprint("""...\U0001F3C3 ...\U0001F3C3 ...\U0001F3C3 ...
        Like an oasis in the dessert, you see in the distance what appears to be a payphone!
        You run to the phone, pick up the receiver, and start to punch in the number on the card...
        Nothing happens. /U0001F997 /U0001F997 /U0001F997
        You were born in 2005! You've never used one of these antiquated things before...
        P-A-Y Phone...
        You reach for your wallet to take out your mom's credit card, and then notice the empty slot with 25¢ written next to it.'Does anyone even carry coins anymore?!'

        What do you do???

        1. You see an old lady a block away. Old people love coins. She's gotta have 25¢ on her, right???

        2. You start searching on the ground for dropped coins""")
        print("Enter: 1 or 2.")
        answer = input()

        if "1" in answer:
            slowprint("""You run up to the old lady, and ask her if she has a quarter she can spare! She starts laughing! "Does anyone even carry coins anymore? I only use Apple Pay! Sorry kid..."""
            )
            game_over()
        elif "2" in answer:
            slowprint("""You start searching for dropped coins, then out of the corner of your eye you notice a worn sticker on the payphone that says, "1-800-COLLECT." You punch in the number. The examiner accepts the collect call."""
            )
            gas_station()
    elif "2" in answer:
        game_over()


def round3():
    slowprint("""You're pulled over at the bus stop... \U0001F68C \U0001F6D1
    Your \U0001F49B starts to race! Did you fail the test?
    Why did he tell you to pull over? \U0001F633
    'Get out of the car,' he says to you. Uh oh... \U0001F648
    'FIRE DRILL!!!' he shouts. \U0001F525 \U0001F525 \U0001F525

    Wait, whaaa...?' you start to question.

    'Car is on fire! Gimmee your phone! You have 10 minutes to find a payphone,
    call the number on this card, and get your tail back here...

    or else... BOOM! The car explodes! \U000023F0 \U0001F4A5

    ...oh and if that happens, you FAIL the test!
    Hope you like having your momma drive you around!'

    You quickly glance at the card he slapped in your hand: """)
    print(examiner["first_name"], examiner["last_name"], examiner["occupation"], examiner["phone_number"])
    slowprint("""'What are you waiting for?!' he shouts!
    '9 minutes 27 seconds' he says again.
    You now notice he's holding a stop watch! This guy's not messing around...

    What do you do???

    1. You're in your best suit (always gotta be lookin' fly!), you're not gonna get it sweaty! Take the bus back to the DMV.

    2. Run like the wind!!! \U0001F3C3 \U0001F32C
    A driver's license = freedom! Challenge accepted!

    3. Do payphones even exist any more?? There's gotta be someone nearby with a cell phone you can borrow and pretend it's a pay phone. """)
    print("Enter: 1, 2, or 3.")
    answer = input()

    if "1" in answer:
        game_over()
    elif "2" in answer:
        find_pay_phone()
    elif "3" in answer:
        find_cell_phone()
    else:
        game_over()


round3()
