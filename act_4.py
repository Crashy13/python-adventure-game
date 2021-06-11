import sys
import time


def slowprint(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 20)


slowprint(
    """You pull into the gas station at the pump, and then you realize you don't have any currency. You have three choices. \n
[1] Ask for the examiner to pay. \n
[2] Ask the guy on the corner with three gold chains around his neck for a few bucks. \n
[3] Tell the examiner (they) are going to pay since they volunteered you for so much driving."""
)

choice = input("1/2/3?")

if "1" in choice:
    slowprint(
        """Examiner didn’t like your tone, but he offers you gas money in exchange for another favor, much more serious in tone. He doesn’t tell you what the favor is unless you agree to it, so he gives you a moment to think it over. What do you do?"""
    )
    choice = input("Do the favor = y; Say no = n")

    if "y" in choice:
        slowprint(
            """The examiner reveals that he's actually an alien, and he needs a human sacrifice; you've just been beamed up into a spaceship, never to be seen again. \n
        Game over."""
        )

    if "n" in choice:
        slowprint(
            """The examiner shrugs his shoulders, seemingly unbothered, and decides to give you the money anyways. You head back to the DMV to get scored and discover if you passed or failed."""
        )

if "2" in choice:
    slowprint(
        """The man actually turns out to be a really nice guy, gives you twenty bucks and tells you next time he sees you he wants to offer you an.... opportunity. You fill up and head back to the DMV to finish your test. """
    )
