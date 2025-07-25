"""
Script to create the webapp with Streamlit.
"""

# Imports

import streamlit as st

from src import recommendations

# Build app

st.write("## Hi there!")

query = st.text_input(
    "Please write down what you would like to eat and we will suggest similar recipes from recipetineats.com."
)
nb_queries = st.text_input("How many recipes do you want? Default is 5.")

if st.button("Show me!"):
    st.write("Here are our recommendations!")
    if not nb_queries:
        recs = recommendations.get_recommendations(query)
    else:
        recs = recommendations.get_recommendations(query, int(nb_queries))
    for row in recs:
        st.write(row)
