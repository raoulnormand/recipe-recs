# recipe-recs

A recommendation system for recipes of [recipetineats](https://www.recipetineats.com/).

# Introduction

The [recipetineats](https://www.recipetineats.com/) contains about 1400 recipes. This repository contains scripts to scrape the content of these recipes and to get recommendations: after inputting what one desires to eat, they obtain the recipes from the website that are most related to the query. 

## Web app

Try it [here](https://recipe-recs.streamlit.app/)!

## Example

Using either the web app or the `get_recommendations` function, a request for "chicken with mushroom and onions" would yield the following results.

- [Ginger chicken and rice]("https://www.recipetineats.com/ginger-chicken-and-rice/)

- [Chicken tetrazzini pasta bake](https://www.recipetineats.com/chicken-tetrazzini-pasta-bake/)

- [Chicken fricassee](https://www.recipetineats.com/chicken-fricassee-quick-french-chicken-stew/) (chicken stew)

- [Coq au vin](https://www.recipetineats.com/coq-au-vin/) (chicken in red wine sauce)

- [Chicken and mushroom risotto](https://www.recipetineats.com/chicken-and-mushroom-risotto/)

# Getting started

## Dependencies

Project built with

- beautifulsoup 4.13.4
- nltk 3.9.1
- numpy 2.3.2
- pandas 2.3.1
- scikit-learn 1.6.1
- setuptools 72.1.0
- streamlit 1.47.0

## Installation

Clone with repo with
```
git clone https://github.com/raoulnormand/recipe-recs.git
```
then install the dependencies with
```
pip -r requirements.txt
```
Install the src module with
```
pip install -e .
```
Recommendations can be obtained with the `get_recommendations` function, using
```
from src.recommendations import get_recommendations
get_recommendations('what I want to eat', number_recommendations)
```

## Description of the techniques

The [recipetineats](https://www.recipetineats.com/) contains a list of its recipes on this [page](https://www.recipetineats.com/recipes/). The corresponding urls can be scraped by running
```
python scripts/urls_scraping.py
```
which saves the list of urls in `results/recipes_urls.txt`. On each page, the ingredients and instructions are obtained by running the `recipes_scraping.py` and `ingredients_scraping.py` scripts. This is done with the beautifulsoup package and extracting the corresponding html anchors from the website. *Note that only the ingredients lists are actually used for recommendations.* The results are saved in the `result` folder.

The `process` function in the `data_processing` module cleans up a chunk of text by performing word tokenization, removing all punctuation and digits, removing stop words, and finally lemmatization.

The model is a bag-of-words model containing 1- and 2- grams. It is trained by using the `process` function on each list of ingredients, and the counting the appearance of each word in the vocabulary (using word count or tfidf seems to make little difference). Training and pickling the model is achieved by running
```
python scripts/train_model.py
```

Finally, recommendations for a given query are obtained as follows:
- the query is `process`-ed;
- the cosine similarity with all the recipes is calculated;
- the recipes (5 by default) with the largest similarity are returned.
This can be obtained using the `get_recommendations` function, as described above.

