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

category = randint(1, 3)

if category == 1:
    pointer = randint(1, 10)
    response = response_affirmative[pointer - 1]
elif category == 2:
    pointer = randint(1, 5)
    response = response_neutral[pointer - 1]
elif category == 3:
    pointer = randint(1, 5)
    response = response_negative[pointer - 1]


# done with ChatGPT. Let's just hope and pray it works…
def loading_bar(duration=3, bar_length=30):
    # Define characters
    start_char_empty = "\uEE00"  # U+EE00 ()
    start_char_filled = "\uEE03"  # U+EE03 ()
    fill_char = "\uEE04"  # U+EE04 ()
    end_char_empty = "\uEE02"  # U+EE02 ()
    end_char_filled = "\uEE05"  # U+EE05 ()
    spacer = "\uEE01"  # U+EE01 ()

    print("\nPredicting the Future...", end="")
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)

        # Dynamically change start and end characters based on progress
        current_start_char = start_char_filled if i > 0 else start_char_empty
        current_end_char = end_char_filled if i == bar_length else end_char_empty

        sys.stdout.write(
            f"\rThinking... {current_start_char}{fill_char * i}{spacer * (bar_length - i)}{current_end_char} {int((i / bar_length) * 100)}%"
        )
        sys.stdout.flush()
    print()
    time.sleep(duration / 2)
    print()


# final output
loading_bar(duration=3, bar_length=20)
print(response)
