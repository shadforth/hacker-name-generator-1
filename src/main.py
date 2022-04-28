# ---------------------------------- MODULES ---------------------------------- #

from flask import Flask, render_template

import random

from src.data.adjectives import adjectives
from src.data.nouns import nouns
from src.data.seperators import separators
from src.data.leet import leet

# ---------------------------------- MAIN ---------------------------------- #


def generate_hacker_name():
    """Generate a hacker name."""

    # Randomly chooses the elements of the name.
    adjective = random.choice(adjectives)
    separator = random.choice(separators)
    noun = random.choice(nouns)

    # Concatenates the string together. Separator goes in the middle to split name parts.
    hacker_name = adjective + separator + noun

    # Swaps some letters to l33t.
    for x, y in leet.items():
        # 50/50 chance to l33t each letter.
        first_flip = random.randint(0, 1)
        if first_flip == 0:
            hacker_name = hacker_name.replace(x, y)

    # Randomly capitalises letters in hacker name.
    capital_hacker_name = ""
    for c in hacker_name:
        # 50/50 chance to upper or lower case letter.
        second_flip = random.randint(0, 1)
        if second_flip == 0:
            capital_hacker_name += c.upper()
        else:
            capital_hacker_name += c.lower()

    # 1/3 chance to capitalise the whole name.
    third_flip = random.randint(0, 2)
    if third_flip == 0:
        capital_hacker_name = capital_hacker_name.upper()

    # Variable back to the original name - easier to read.
    hacker_name = capital_hacker_name

    # Return the newly generated name.
    return hacker_name

# ---------------------------------- FLASK APP ---------------------------------- #


# Creates the Flask app.
app = Flask(__name__)


# Creates a route directory to be used for index.html.
@app.route("/")
def index():
    return render_template("index.html", name=generate_hacker_name())


# Run the app.
if __name__ == "__main__":
    app.run()
