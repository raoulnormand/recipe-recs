"""
Scrapes recipes from recipetineats.com, using the list of urls
of the recipes_urls.txt file.
"""

# Imports

import time
from pathlib import Path
from random import randint

from src.scraping import soupify

# Functions


def get_instructions(url):
    """
    Gets the recipe instructions on the given page.
    """
    recipe = soupify(url)
    # Instructions are listed with the class below
    instructions_list = recipe.find_all("div", class_="wprm-recipe-instruction-text")
    # Get only the text and concatenate
    instructions_text = [instruction.get_text() for instruction in instructions_list]
    return " ".join(instructions_text)


# Main function


def main():
    """
    Adds the instructions all recipe links and instructions
    to a csv file.
    """
    # Save instructions from each url in a csv file
    main_dir = Path(__file__).parent.parent
    with open(
        main_dir / "/results/recipes_instructions.csv", "w", encoding="utf-8"
    ) as recipes_instructions:
        recipes_instructions.write("url,instructions\n")
        with open(main_dir / "/results/recipes_urls.txt", "r") as recipes_urls:
            for url in recipes_urls:
                instructions = get_instructions(url)
                # Only add if there are instructions, i.e. the link is to a recipe
                if instructions:
                    # Replace , by ; to avoid issues in csv
                    instructions = instructions.replace(",", ";")
                    recipes_instructions.write(url.strip() + ", " + instructions + "\n")
                time.sleep(randint(1, 3))


if __name__ == "__main__":
    main()
