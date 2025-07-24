"""
Utility functions for scraping.
"""

from urllib.request import urlopen

from bs4 import BeautifulSoup


def soupify(url):
    """
    Reads a url and returns it as a BeautifulSoup object.
    """
    html = urlopen(url).read().decode("utf8")
    return BeautifulSoup(html, "html.parser")
