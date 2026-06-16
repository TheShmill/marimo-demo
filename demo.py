# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App()


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


if __name__ == "__main__":
    app.run()
