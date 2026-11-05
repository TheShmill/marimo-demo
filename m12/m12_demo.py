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
    # Import the libraries
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # The Dataset
    We will look at a synthesized dataset of 400 days at one emergency department, 9,600 hours in all, which we treat as the whole **population**. Each row represents one hour, with the following details:
    - hour_id, 1 to 9,600, in time order
    - hour, the hour of the day, from 0 (midnight) to 23
    - time_of_day, Night (hours 0 to 5), Morning (6 to 11), Afternoon (12 to 17) or Evening (18 to 23)
    - arrivals, the number of patients who arrived during that hour
    """)
    return


@app.cell
def _(pd):
    # Load the dataset
    df = pd.read_csv("m12_demo.csv")
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Population Mean
    *The **population mean** is a **population parameter**: the true value we want to estimate. In practice it is unknown, since checking every record is too slow or costly, so we estimate it from a sample.* Here we have the whole population, so we can calculate it and see how close each sample gets.
    """)
    return


@app.cell
def _(df):
    # Mean arrivals per hour in the population
    population_mean = df["arrivals"].mean()
    population_mean
    return (population_mean,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On average, **about 5 patients arrive each hour**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Simple Random Sample
    *In a **simple random sample**, every row has **the same chance of being chosen**.* `df.sample(100)` picks 100 hours at random.
    """)
    return


@app.cell
def _(df):
    # 100 hours chosen at random
    srs = df.sample(100)
    srs
    return (srs,)


@app.cell
def _(srs):
    # Mean arrivals in the simple random sample
    srs["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *The mean of a sample is a **sample statistic**, our estimate of the population mean.* It is usually close to 5, but not exactly 5.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sampling Distribution: Simple Random
    *One sample gives one estimate, and a different sample gives a different one. The **sampling distribution** shows **how much the sample statistic varies from sample to sample**.* We take 1,000 simple random samples of 100 hours and store the mean of each one.
    """)
    return


@app.cell
def _(df):
    # Means of 1,000 simple random samples of 100 hours
    srs_means = []
    for _ in range(1000):
        srs_means.append(df.sample(100)["arrivals"].mean())
    return (srs_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A histogram of the 1,000 means shows the sampling distribution, with a red line at the population mean.
    """)
    return


@app.cell
def _(plt, population_mean, sns, srs_means):
    # Sampling distribution of the mean for simple random samples
    sns.histplot(x=srs_means)
    plt.axvline(population_mean, color="red")
    plt.xlabel("Sample mean arrivals per hour")
    plt.ylabel("Number of samples")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *The **mean** of a sampling distribution shows where the estimates are centered, and its **standard deviation** shows how far a single estimate typically falls from that center. In practice we take **only one sample**, so we cannot see how far our estimate is from the truth. A small standard deviation means **most samples give an estimate close to the center**, so the one sample we take is likely to be close. That is why a good sampling method keeps this standard deviation as **small** as possible.*
    """)
    return


@app.cell(hide_code=True)
def _(mo, pd, srs_means):
    mo.md(rf"""
    | Method | Mean of the sample means | Standard deviation of the sample means |
    |---|---|---|
    | Simple random | {pd.Series(srs_means).mean():.2f} | {pd.Series(srs_means).std():.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The simple random sample means are **centered on the population mean of about 5.0**, with a standard deviation of about 0.31.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Systematic Sample
    *A **systematic sample** keeps **every kth row** from a starting row.* `df["hour_id"] % 100 == 50` keeps every 100th hour starting at hour_id 50, which gives 96 rows. We picked 50 for illustration; *in practice the starting row should be chosen at random*.
    """)
    return


@app.cell
def _(df):
    # Every 100th hour, starting at hour_id 50
    systematic_100 = df[df["hour_id"] % 100 == 50]
    systematic_100
    return (systematic_100,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    100 hours is 4 days and 4 hours, so each row of the sample is **4 hours later in the day** than the row before. We count the hours in the sample to check.
    """)
    return


@app.cell
def _(systematic_100):
    # Rows per hour of the day in the systematic sample
    systematic_100["hour"].value_counts()
    return


@app.cell
def _(systematic_100):
    # Mean arrivals in the systematic sample
    systematic_100["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The sample has 16 rows at each of 1, 5 and 9 a.m. and 1, 5 and 9 p.m., spread evenly across the day, and its mean is **about 4.8 patients an hour, close to the population mean**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sampling Distribution: Systematic, Every 100th Hour
    *A systematic sample of every 100th row can start at only 100 places, so there are **only 100 possible systematic samples**.* We store the mean of every one of them, with remainders 0 to 99.
    """)
    return


@app.cell
def _(df):
    # Means of all 100 possible systematic samples with a step of 100
    systematic_100_means = []
    for start_100 in range(100):
        systematic_100_means.append(df[df["hour_id"] % 100 == start_100]["arrivals"].mean())
    return (systematic_100_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *To compare sampling methods, we compare their sampling distributions: a good method gives sample means **centered on the population mean** and **close together**.* The two lists have different lengths (1,000 and 100), so we pass them to `sns.boxplot` as a dictionary, with one key per box.
    """)
    return


@app.cell
def _(plt, sns, srs_means, systematic_100_means):
    # Simple random and systematic sample means
    sns.boxplot({"Simple random": srs_means, "Every 100th hour": systematic_100_means})
    plt.ylabel("Sample mean arrivals per hour")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo, pd, srs_means, systematic_100_means):
    mo.md(rf"""
    | Method | Mean of the sample means | Standard deviation of the sample means |
    |---|---|---|
    | Simple random | {pd.Series(srs_means).mean():.2f} | {pd.Series(srs_means).std():.2f} |
    | Every 100th hour | {pd.Series(systematic_100_means).mean():.2f} | {pd.Series(systematic_100_means).std():.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Both methods are centered on the population mean of about 5.0**, and the systematic sample means are less spread out: a standard deviation of about 0.26, compared with about 0.31 for simple random samples. Each systematic sample is spread evenly across the day.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Step That Lines Up
    Now we take every 96th hour instead, again starting at hour_id 50, which gives 100 rows.
    """)
    return


@app.cell
def _(df):
    # Every 96th hour, starting at hour_id 50
    systematic_96 = df[df["hour_id"] % 96 == 50]
    systematic_96
    return (systematic_96,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    96 hours is exactly 4 days, so every row in this sample falls at **the same hour of the day**. We count the hours in the sample to check.
    """)
    return


@app.cell
def _(systematic_96):
    # Rows per hour of the day in the systematic sample
    systematic_96["hour"].value_counts()
    return


@app.cell
def _(systematic_96):
    # Mean arrivals in the systematic sample
    systematic_96["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Every row is from 1 a.m., and this sample's mean is **about 2.3 patients an hour, less than half the population mean**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sampling Distribution: Systematic, Every 96th Hour
    A step of 96 can start at 96 places, so there are 96 possible systematic samples. We store the mean of every one of them, with remainders 0 to 95, and compare them with the simple random sample means.
    """)
    return


@app.cell
def _(df):
    # Means of all 96 possible systematic samples with a step of 96
    systematic_96_means = []
    for start_96 in range(96):
        systematic_96_means.append(df[df["hour_id"] % 96 == start_96]["arrivals"].mean())
    return (systematic_96_means,)


@app.cell
def _(plt, sns, srs_means, systematic_96_means):
    # Simple random and systematic sample means
    sns.boxplot({"Simple random": srs_means, "Every 96th hour": systematic_96_means})
    plt.ylabel("Sample mean arrivals per hour")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo, pd, srs_means, systematic_96_means):
    mo.md(rf"""
    | Method | Mean of the sample means | Standard deviation of the sample means |
    |---|---|---|
    | Simple random | {pd.Series(srs_means).mean():.2f} | {pd.Series(srs_means).std():.2f} |
    | Every 96th hour | {pd.Series(systematic_96_means).mean():.2f} | {pd.Series(systematic_96_means).std():.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Both methods are centered on the population mean of about 5.0**, but the systematic sample means are far more spread out: a standard deviation of about 2.2, compared with about 0.31 for simple random samples.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mean Arrivals by Hour
    To see why the two steps behave so differently, we look at how arrivals change through the day.
    """)
    return


@app.cell
def _(df):
    # Mean arrivals for each hour of the day
    df.groupby("hour")["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Arrivals are lowest around 4 a.m., about 1.6 an hour, and highest around noon, about 7.8 an hour. *If the rows follow **a repeating pattern** and the step of a systematic sample **lines up with it**, every row of the sample lands at the same point in the pattern.* Here the hours repeat every 24 rows and 96 is a multiple of 24, so each sample of every 96th hour contains a single hour of the day, and its mean is close to that hour's mean: low for a night hour, high for a midday hour.

    *When the step **does not line up** with the pattern, each sample **lands at several points spread across the pattern**, so it can give estimates **closer together than a simple random sample**. The problem is the step lining up with the pattern, not the pattern itself. The catch is that a repeating pattern is often unknown before sampling, so we cannot be sure the step avoids it.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Stratified Sample
    *A **stratified sample** splits the population into groups, called **strata**, and takes a random sample from each one.* `groupby("time_of_day").sample(25)` takes 25 random hours from each time of day, 100 rows in all.
    """)
    return


@app.cell
def _(df):
    # 25 random hours from each time of day
    stratified = df.groupby("time_of_day").sample(25)
    stratified
    return (stratified,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We count the rows from each time of day in the stratified sample and in the simple random sample.
    """)
    return


@app.cell
def _(stratified):
    # Rows per time of day in the stratified sample
    stratified["time_of_day"].value_counts()
    return


@app.cell
def _(srs):
    # Rows per time of day in the simple random sample
    srs["time_of_day"].value_counts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Every stratified sample has **exactly the same share of each group as the population***, here 25 of each, while the simple random sample has more of some times of day and fewer of others.
    """)
    return


@app.cell
def _(stratified):
    # Mean arrivals in the stratified sample
    stratified["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sampling Distribution: Stratified
    We take 1,000 stratified samples of 25 hours from each time of day, store the mean of each one, and compare them with the simple random sample means.
    """)
    return


@app.cell
def _(df):
    # Means of 1,000 stratified samples of 25 hours per time of day
    stratified_means = []
    for _ in range(1000):
        stratified_means.append(df.groupby("time_of_day").sample(25)["arrivals"].mean())
    return (stratified_means,)


@app.cell
def _(plt, sns, srs_means, stratified_means):
    # Simple random and stratified sample means
    sns.boxplot({"Simple random": srs_means, "Stratified": stratified_means})
    plt.ylabel("Sample mean arrivals per hour")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo, pd, srs_means, stratified_means):
    mo.md(rf"""
    | Method | Mean of the sample means | Standard deviation of the sample means |
    |---|---|---|
    | Simple random | {pd.Series(srs_means).mean():.2f} | {pd.Series(srs_means).std():.2f} |
    | Stratified | {pd.Series(stratified_means).mean():.2f} | {pd.Series(stratified_means).std():.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Both methods are centered on the population mean of about 5.0**, and the stratified sample means are less spread out: a standard deviation of about 0.25, compared with about 0.31 for simple random samples.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mean Arrivals by Time of Day
    To see why stratifying helps, we look at mean arrivals in each time of day.
    """)
    return


@app.cell
def _(df):
    # Mean arrivals for each time of day
    df.groupby("time_of_day")["arrivals"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Night hours average about 2.1 arrivals, far fewer than the afternoon's 7.1. A simple random sample can have more or fewer night hours by chance, and each extra night hour pulls its mean down. *Stratifying **removes the variation that comes from the mix of groups**, so it helps most when **the groups differ a lot from each other**.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sample Size
    *As the sample size grows, the sample mean **tends to get closer to the population mean**, so the sampling distribution gets narrower.* Use the slider to choose a sample size; the histogram shows the means of 1,000 simple random samples of that size, on the same axis every time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Slider for the sample size
    size_slider = mo.ui.slider(steps=[10, 20, 40, 80, 160, 320, 640], value=10, label="Sample size", show_value=True)
    size_slider
    return (size_slider,)


@app.cell
def _(df, plt, size_slider, sns):
    # Means of 1,000 simple random samples of the size chosen on the slider
    slider_means = []
    for _ in range(1000):
        slider_means.append(df.sample(size_slider.value)["arrivals"].mean())
    sns.histplot(x=slider_means)
    plt.xlim(1, 9)
    plt.xlabel("Sample mean arrivals per hour")
    plt.ylabel("Number of samples")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sample Means by Sample Size
    To compare sample sizes side by side, we take 1,000 simple random samples at each of four sizes and store each sample's size and mean in a long table with one row per sample.
    """)
    return


@app.cell
def _(df, pd):
    # Means of 1,000 simple random samples for each sample size
    sizes = []
    means = []
    for n in [10, 40, 160, 640]:
        for _ in range(1000):
            sizes.append(n)
            means.append(df.sample(n)["arrivals"].mean())
    means_by_size = pd.DataFrame({"sample_size": sizes, "sample_mean": means})
    means_by_size
    return (means_by_size,)


@app.cell
def _(means_by_size, plt, sns):
    # One box per sample size
    sns.boxplot(means_by_size, x="sample_size", y="sample_mean")
    plt.xlabel("Sample size (hours)")
    plt.ylabel("Sample mean arrivals per hour")
    plt.show()
    return


@app.cell
def _(means_by_size):
    # Standard deviation of the sample means for each sample size
    means_by_size.groupby("sample_size")["sample_mean"].std()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The standard deviation falls from about 0.98 for samples of 10 to about 0.12 for samples of 640. **Each time the sample size is multiplied by 4, the spread is cut about in half.** *To halve the typical error of an estimate, we need a sample about four times as large.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Choosing a Sampling Method
    - ***Simple random sampling** is the default. It needs no knowledge of the population, and its sample means are **centered on the population mean**.*
    - ***Systematic sampling** is easy to carry out, such as checking every 100th record. It works like a simple random sample when the rows are in **no particular order**. When the rows follow a pattern, a step that **does not line up with it** spreads the sample across the pattern and can beat a simple random sample, but a step that **lines up with it** can be far off.*
    - ***Stratified sampling** guarantees **each group's share of the sample**. It gives closer estimates than a simple random sample when the groups differ a lot, but we need to know each row's group before sampling.*
    - *For every method, **a larger sample gives a more precise estimate**.*
    """)
    return


if __name__ == "__main__":
    app.run()
