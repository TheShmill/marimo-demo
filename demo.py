# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.3",
#     "pandas>=3.0.3",
#     "requests>=2.34.2",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import requests
    import pandas as pd
    import numpy as np
    import re

    return pd, re, requests


@app.cell
def _():
    x = 10
    return (x,)


@app.cell
def _():
    y = 5
    return (y,)


@app.cell
def _(x, y):
    x + y
    return


@app.cell
def _(re, requests):
    body = requests.get("https://www.gutenberg.org/cache/epub/2701/pg2701.txt").text.lower()
    body = re.sub("[^a-z]", " ", body)
    body[:20]
    return (body,)


@app.cell
def _(body, pd):
    words = pd.DataFrame({"words": body.split()})
    words[:20]
    return (words,)


@app.cell
def _(words):
    most_frequent_words = words.groupby("words").size().sort_values(ascending=False)
    most_frequent_words[:20]
    return


@app.cell
def _(words):
    long_words = words[words["words"].str.len() > 8]
    long_words[:20]
    return (long_words,)


@app.cell
def _(long_words):
    long_words.groupby("words").size().sort_values(ascending=False)[:20]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
