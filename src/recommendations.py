"""
Define the function to recommend recipes from the website.
"""

# Imports

from pathlib import Path
from pickle import load

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.data_processing import process

# Functions


def get_recommendations(query, nb_results=5):
    """
    Give *nb_results* recommendations that most match the *query*.
    """
    # Load vectorizer and model
    main_dir = Path(__file__).parent.parent
    with open(main_dir / "results/vectorizer.pkl", "rb") as f:
        vectorizer = load(f)
    with open(main_dir / "results/model.pkl", "rb") as f:
        model = load(f)
    # Process and evctorize the query
    query_vec = vectorizer.transform([process(query)])
    # Compute cosine similarity
    cossim = cosine_similarity(model, query_vec)
    # Return best results in decreasing order
    indices = np.argsort(cossim.flatten())[: -nb_results - 1 : -1]
    df = pd.read_csv(main_dir / "results/recipes_ingredients.csv")
    return df.loc[indices, "url"]
