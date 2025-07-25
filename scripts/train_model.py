"""
Train the model.
"""

# Imports

from pathlib import Path
from pickle import dump

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from src.data_processing import process

# Main function


def main():
    """
    Defines and saves the model.
    """
    # Process the instructions text
    main_dir = Path(__file__).parent.parent
    df = pd.read_csv(main_dir / "results/recipes_instructions.csv")
    df["instructions"] = df["instructions"].apply(process)
    # Define model
    vectorizer = TfidfVectorizer(min_df=0.001)
    model = vectorizer.fit_transform(df["instructions"])
    # Pickle vectorizer and model
    with open(main_dir / "results/vectorizer.pkl", "wb") as f:
        dump(vectorizer, f)
    with open(main_dir / "results/model.pkl", "wb") as f:
        dump(model, f)


if __name__ == "__main__":
    main()
