"""
Scrapes recipe urls from recipetineats.com and saves to recipes_list.txt.
The list of all recipes is at the url
https://www.recipetineats.com/recipes/?fwp_paged=*
with * from 1 to 80 (as of July 2025)
"""

# Imports

import time
from pathlib import Path
from random import randint

from src.scraping import soupify

# Constants

NUMBER_RECIPE_PAGES = 80

# Functions


def get_recipe_links(url):
    """
    Gets all the recipe links on the given page.
    """
    soup = soupify(url)
    # Recipes are listed with the class below
    recipes = soup.find_all("a", class_="entry-title-link")
    # Extract the html from the list
    return [recipe["href"] for recipe in recipes]


# Main function


def main():
    """
    Adds all recipe links to a txt file.
    """
    for nb_page in range(1, NUMBER_RECIPE_PAGES):
        url = "https://www.recipetineats.com/recipes/?fwp_paged=" + str(nb_page)
        recipes_urls = get_recipe_links(url)
        main_dir = Path(__file__).parent.parent
        with open(main_dir / "results/recipes_urls.txt", "a") as f:
            for line in recipes_urls:
                f.write(f"{line}\n")
        time.sleep(randint(0, 3))


if __name__ == "__main__":
    main()
