"""
Scrapes ingredients from the recipes of recipetineats.com, using the list of urls of the recipes_urls.txt file.
"""

# Imports

import time
from pathlib import Path
from random import randint

from src.scraping import soupify

# Functions


def get_ingredients(url):
    """
    Gets the recipe instructions on the given page.
    """
    recipe = soupify(url)
    # Instructions are listed with the class below
    instructions_list = recipe.find_all("span", class_="wprm-recipe-ingredient-name")
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
        main_dir / "results/recipes_ingredients.csv", "w", encoding="utf-8"
    ) as recipes_ingredients:
        recipes_ingredients.write("url,ingredients\n")
        with open(
            main_dir / "results/recipes_urls.txt", "r", encoding="utf-8"
        ) as recipes_urls:
            for url in recipes_urls:
                ingredients = get_ingredients(url)
                # Only add if there are ingredients, i.e. the link is to a recipe
                if ingredients:
                    # Replace , by ; to avoid issues in csv
                    ingredients = ingredients.replace(",", ";")
                    recipes_ingredients.write(url.strip() + ", " + ingredients + "\n")
                time.sleep(randint(1, 3))


if __name__ == "__main__":
    main()
