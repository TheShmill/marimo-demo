# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.2",
#     "matplotlib==3.11.2",
#     "pandas==3.0.5",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Clinic Wait Times

    An outpatient clinic recorded every appointment over 100 weeks. The clinic is open Monday to Friday, and the rows are in date and appointment order. We treat these 10,000 simulated appointments as the whole population. Each row is one appointment, with these columns:
    - visit_id, 1 to 10,000, in date and appointment order
    - appointment_time, the time the appointment was booked for, from 08:00 to 17:30
    - visit_type, Follow-up, New or Same-day
    - wait_time, in minutes from the appointment time until the patient is seen

    To write an answer, double-click its cell, replace the placeholder text, and run the cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # The Population
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Clinic Visits

    **Instructions:** Load `clinic_visits.csv` into a DataFrame and display it.
    """)
    return


@app.cell
def _(pd):
    # Your code here
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Population Mean

    **Instructions:** Calculate the mean wait time of the population.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Simple Random Sampling
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Simple Random Sample

    **Instructions:** Take a simple random sample of 100 rows and calculate its mean wait time.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sampling Distribution: Simple Random

    **Instructions:** Take 1,000 simple random samples of 100 rows and calculate the mean wait time of each one. Store the 1,000 means in a variable.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return (srs_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Plotting the Simple Random Sample Means

    **Instructions:** Create a histogram of the simple random sample means, with a vertical line at the population mean.
    """)
    return


@app.cell
def _(df, plt, sns, srs_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spread: Simple Random

    **Instructions:** Calculate the standard deviation of the simple random sample means.
    """)
    return


@app.cell
def _(pd, srs_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Systematic Sampling
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Choosing Good and Bad Steps

    **Instructions:** A systematic sample with a step of k keeps every kth row, so it has about 10,000 / k rows, and there are only k possible systematic samples, one for each remainder from 0 to k - 1. Think about the patterns in the dataset, especially the order of the rows. Choose a good step and a bad step, each giving samples of about 100 rows, and explain why you picked them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Double click here to write your answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sampling Distribution: Bad Step

    **Instructions:** Calculate the mean wait time of every possible systematic sample with your bad step and store the means in a variable.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return (systematic_100_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sampling Distribution: Good Step

    **Instructions:** Calculate the mean wait time of every possible systematic sample with your good step and store the means in a variable.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return (systematic_99_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Comparing the Two Steps

    **Instructions:** Create a box plot of the sample means of your two steps, with one box per step.
    """)
    return


@app.cell
def _(plt, sns, systematic_100_means, systematic_99_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spread: Bad Step

    **Instructions:** Calculate the standard deviation of your bad step's sample means.
    """)
    return


@app.cell
def _(pd, systematic_100_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spread: Good Step

    **Instructions:** Calculate the standard deviation of your good step's sample means.
    """)
    return


@app.cell
def _(pd, systematic_99_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Did Your Steps Behave as Expected?

    **Instructions:** Did your good and bad steps behave the way you expected? Compare their standard deviations with each other and with the standard deviation of the simple random sample means.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Double click here to write your answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Stratified Sampling
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Stratified Sample

    **Instructions:** Take a stratified sample of 1% of the rows from each visit type and count the rows of each visit type in it.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sampling Distribution: Stratified

    **Instructions:** Take 1,000 stratified samples of 1% of the rows from each visit type and calculate the mean wait time of each one. Store the 1,000 means in a variable.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return (stratified_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Plotting the Stratified Sample Means

    **Instructions:** Create a histogram of the stratified sample means.
    """)
    return


@app.cell
def _(plt, sns, stratified_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spread: Stratified

    **Instructions:** Calculate the standard deviation of the stratified sample means.
    """)
    return


@app.cell
def _(pd, stratified_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mean Wait by Visit Type

    **Instructions:** Calculate the mean wait time for each visit type in the population.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Stratifying Helps

    **Instructions:** Using the mean wait by visit type, explain why the stratified sample means vary less than the simple random sample means.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Double click here to write your answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Comparing the Methods

    **Instructions:** How did the standard deviations of the sample means compare between simple random sampling, your good and bad systematic steps, and stratified sampling? Which methods gave the most precise estimates?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Double click here to write your answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Sample Size
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sampling Distribution: 400 Rows

    **Instructions:** Take 1,000 simple random samples of 400 rows and calculate the mean wait time of each one. Store the 1,000 means in a variable.
    """)
    return


@app.cell
def _(df):
    # Your code here
    return (srs_400_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Comparing Sample Sizes

    **Instructions:** Create a box plot of your simple random sample means of 100 rows and of 400 rows, with one box per sample size.
    """)
    return


@app.cell
def _(plt, sns, srs_400_means, srs_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Spread: 400 Rows

    **Instructions:** Calculate the standard deviation of the simple random sample means of 400 rows.
    """)
    return


@app.cell
def _(pd, srs_400_means):
    # Your code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sample Size and the Sampling Distribution

    **Instructions:** How does the sampling distribution of the mean change when the sample size grows from 100 to 400 rows?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Double click here to write your answer.
    """)
    return


if __name__ == "__main__":
    app.run()
