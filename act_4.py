import sys
import time


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
        gas_station_shenanigans()
    elif "n" in answer:
        exit()
    else:
        print("Please enter y for yes or n for no")
        play_again()
#############################################


def gas_station_shenanigans():
    slowprint(
        """You pull into the gas station at the pump, and then you realize you don't have any currency. You have three choices. \n
    [1] Ask for Mr. Brown to pay. \n
    [2] Ask the guy on the corner with three gold chains around his neck for a few bucks. \n
    [3] Tell Mr. Bob Brown he is going to pay since he volunteered you for all the troubles."""
    )

    choice = input("1/2/3?")

    if "1" in choice:
        slowprint(
            """Mr. Brown didn’t like your tone, but he offers you gas money in exchange for another favor, much more serious in tone. He doesn’t tell you what the favor is unless you agree to it, so he gives you a moment to think it over. What do you do?"""
        )
        choice = input("Do the favor = y; Say no = n")

        if "y" in choice:
            slowprint(
                """Mr. 'Bob Brown' explains that he's still involved with the military and on a covert mission and he looks to recruit you into it. You've now agreed to yet another ridiculous adventure. Then he starts to laugh, noticing how well he fooled you, slaps twenty bucks in your hand for your troubles. This guy's nuts!"""
            )
            one_last_thing()

        if "n" in choice:
            slowprint(
                """Mr. Brown shrugs his shoulders, seemingly unbothered, and is now screaming for you to get out of your own car, now you're walking back to the DMV and you're not getting your license!"""
            )
            game_over()

    elif "2" in choice:
        slowprint(
            """The man actually turns out to be a really nice guy, gives you twenty bucks and tells you next time he sees you he wants to offer you an... opportunity. You fill up and head back to the DMV to finish your test. """
        )
        one_last_thing()

    elif "3" in choice:
        slowprint(
            """He replies with a booming laugh, saying, 'I like your enthusiasm! Also, that's prolly fair,' and hands you twenty bucks."""
        )
        one_last_thing()


#############################################


def one_last_thing():
    slowprint(
        """You pile into the car, and reach to put the key in the ignition. Mr. Brown asks, 'What are you doing? What are you missing?' You have three choices: \n
    [1] Tell him it's been an odd day, you forgot the must-do's before you start the car, and you put your seatbelt on and check your mirrors. \n
    [2] You grumble, put your seatbelt on, turn the ignition, and throw the car into drive."""
    )

    choice = input("1/2?")

    if "1" in choice:
        slowprint(
            """Thank goodness you did that, had you taken off in haste, you would've been hit. It would've been a horrible accident! Might've totaled your car. Whew!"""
        )
        the_drive_back()

    elif "2" in choice:
        slowprint(
            """In your haste, you were involved in a violent accident. You've totaled your car! Definitely won't be getting your license now."""
        )
        game_over()


############################################


def the_drive_back():
    slowprint(
        """You're on your way back, and stop at a red light. Mr. Brown has seemed to change his pace, much less erratic and talkative. Apparently he has no more test questions for you. All of a sudden, you hear a tapping on your window. You look over, and a man has a gun pointed into your window, and tells you to get out of the car. You have three choices: \n
        [1] You keep your cool for a moment, and then decide to floor it through the red light and hope for the best. \n
        [2] You look the man in the eyes, wave your hand and say, 'You don't want this car.' \n
        [3] You freeze, completely overcome with fear, with no idea what to do."""
    )

    choice = input("1/2/3?")

    if "1" in choice:
        slowprint(
            """You plow through the red light, but get clipped in the tail by another car. And mystery criminal decides to shoot you just for kicks since your act of heroism failed rather suddenly."""
        )
        game_over()

    elif "2" in choice:
        slowprint(
            """Okay, I'm not sure what you thought was gonna happen, but as the narrator I respect the last ditch effort, and thankfully for you, so does Mr. Brown, who takes the opportunity of the man's confusion and pulls his own weapon, at which moment the criminal decides it's not worth his life and probably went home in complete shambles, what with being so caught off-guard by your last-ditch effort being a star wars reference. Kudos to you."""
        )
        next_level()

    elif "3" in choice:
        slowprint(
            """Mr. Brown siezes the opportunity you just missed out on, and uses the star wars line to catch the hijacker off guard, pulls his own weapon, at which point the hijacker chooses to walk away, not risking his life. Congratulations, Mr. Crazy is now cooler than you, in so many ways."""
        )
        next_level()


############################################


def back_at_the_DMV():
    slowprint(
        """You make it to the DMV in one piece, surprisingly. Your brother asks you, 'Why did it take you SO long?' You don't even bother to answer him, it's been a long day. Mr. Brown disappears behind the counter for quite some time... and you start to get nervous about whether you passed or failed. Failed! After the sequence of events that you've had today, you loathe the thought. \n
    Mr. Brown reappears, with your results. 'Son, you've been through a slew of trouble today. But I can't save you from your horrible driving skills, and other miscellaneous skills that we've explored today. You're not getting your license... \n
    You have three choices. \n
    [1] You accept your fate, walk away hanging your head, and try again in who knows how long. The DMV is a nightmare. \n
    [2] Enraged, you tell that man he's gonna reconsider what he just said for his and your own health (probably not the best idea, but people do lots of crazy things when they're mad). \n
    [3] You take a gamble, give a laugh and tell him that was a good joke."""
    )

    main_choice = [
        {
            1: "You accept your fate, walk away hanging your head, and try again in who knows how long. The DMV is a nightmare.",
            2: "Enraged, you tell that man he's gonna reconsider what he just said for his and your own health (probably not the best idea, but people do lots of crazy things when they're mad).",
            3: "You take a gamble, give a laugh and tell him that was a good joke.",
        }
    ]


for i in main_choice:
    for key, value in i.items():
        print(f"{key}-{value}")
main_choice_input = input("1/2/3?")
if main_choice_input == 1:
    slowprint(
        """You really just picked that to start over, and I don't know if I respect it, or hate it. Either way,"""
    )
    game_over()
elif main_choice_input == 2:
    choice_two_intro = "Mr. Brown is not impressed with your spunk, and tells you to take a hike before you get hurt. You now have two choices. "
    secondary_choice = [
        {
            1: "You tell him to bring it outside and find out who's really gonna get hurt. You're really hoping he doesn't call your bluff.",
            2: "Bluff a recording on your phone of him threatening you, and blackmail him into giving you your license.",
        }
    ]
    slowprint(choice_two_intro)
    for i in secondary_choice:
        for key, value in i.items():
            print(f"{key}-{value}")
    secondary_choice_input = input("1/2?")
    if "1" in choice:
        slowprint(
            """He calls your bluff. To make a long story short, you didn't get your license."""
        )
        game_over()
    elif "2" in choice:
        slowprint(
            """He takes the bait, grumbling about it, but obliges to your demands. Congratulations! Don't kill anyone."""
        )
        play_again()
    elif "3" in choice:
        slowprint(
            """He looks at you sternly, tells you it wasn't a joke, and to go home. But you're not finished yet. You give it another attempt. And, oddly enough, Mr. Brown starts booming laughing, and says he almost had you. He gives you a ticket for the camera line. You've successfully gotten your driver's license. Congratulations!"""
        )
        play_again()

gas_station_shenanigans()
