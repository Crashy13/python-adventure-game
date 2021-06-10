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

user_dec = input("1/2/3/4?")
