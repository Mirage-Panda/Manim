from random import randint
import time
import sys

response_affirmative = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
]
response_neutral = [
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
]
response_negative = [
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]


def get_response():
    category = randint(1, 3)
    if category == 1:
        counter = randint(1, 10)
        response = response_affirmative[counter - 1]
    elif category == 2:
        counter = randint(1, 5)
        response = response_neutral[counter - 1]
    elif category == 3:
        counter = randint(1, 5)
        response = response_negative[counter - 1]
    print(response)


# def magic_8_ball():


# let's just hope and pray it works…
def loading_bar(duration=3, bar_length=30):
    start_char_empty = "\uEE00"  # U+EE00 ()
    spacer = "\uEE01"  # U+EE01 ()
    end_char_empty = "\uEE02"  # U+EE02 ()
    start_char_filled = "\uEE03"  # U+EE03 ()
    fill_char = "\uEE04"  # U+EE04 ()
    end_char_filled = "\uEE05"  # U+EE05 ()

    print("\nThinking...", end="")
    time.sleep(2 * duration / bar_length)
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)
        current_start_char = start_char_filled if i > 0 else start_char_empty
        current_end_char = end_char_filled if i == bar_length else end_char_empty
        sys.stdout.write(
            f"\rPredicting... {current_start_char}{fill_char * i}{spacer * (bar_length - i)}{current_end_char} {int((i / bar_length) * 100)}%"
        )
        sys.stdout.flush()
    print()
    time.sleep(duration / 3)
    print()


# final output
# magic_8_ball()
loading_bar(duration=4, bar_length=20)
get_response()
