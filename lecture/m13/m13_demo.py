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
    mo.md(r"""
    # Bootstrapping Confidence Intervals
    We will look at a synthesized dataset of 10,000 adults seen at a county health screening program, which we treat as the whole population. Each row represents one adult, and the heart_rate column holds the adult's resting heart rate in beats per minute.
    """)
    return


@app.cell
def _(pd):
    heart_df = pd.read_csv("m13_demo_heart_rate.csv")
    heart_df
    return (heart_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A Single Sample
    We'll take a sample of 100 adults to use for our bootstrap. In practice, you would only have the sample, not the population.
    """)
    return


@app.cell
def _(heart_df):
    sample = heart_df.sample(100, random_state=37)
    sample
    return (sample,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The sample mean is our estimate of the population mean.
    """)
    return


@app.cell
def _(sample):
    sample["heart_rate"].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bootstrapping
    We take 10,000 resamples of 100 adults from our sample and compute the mean heart rate of each one. This forms our bootstrap distribution.
    """)
    return


@app.cell
def _(pd, sample):
    bootstrap_means = []
    for _i in range(10000):
        # replace=True draws with replacement
        # random_state=_i gives the same bootstrap distribution every run
        _bootstrap_sample = sample.sample(100, replace=True, random_state=_i)
        bootstrap_means.append(_bootstrap_sample["heart_rate"].mean())
    # Convert the list to a pandas Series
    bootstrap_means = pd.Series(bootstrap_means)
    bootstrap_means
    return (bootstrap_means,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bootstrap Distribution
    The resampled means form a roughly normal distribution.
    """)
    return


@app.cell
def _(bootstrap_means, plt, sns):
    sns.histplot(x=bootstrap_means)
    plt.xlabel("Bootstrap mean heart rate (beats per minute)")
    plt.ylabel("Number of resamples")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 95% Confidence Interval
    The 95% confidence interval runs from the 2.5th to the 97.5th percentile of the bootstrap means.
    """)
    return


@app.cell
def _(bootstrap_means):
    ci_95 = bootstrap_means.quantile([0.025, 0.975])
    f"95% confidence interval: [{ci_95[0.025]:.1f}, {ci_95[0.975]:.1f}]"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We are 95% confident that the population mean resting heart rate is between 70.8 and 75.1 beats per minute.

    In practice, the population mean is unknown. Here we have the whole population, so we can check whether our interval captured it.
    """)
    return


@app.cell
def _(heart_df):
    population_mean = heart_df["heart_rate"].mean()
    round(population_mean, 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The population mean of 71.5 falls inside our 95% confidence interval of 70.8 to 75.1.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bootstrap vs Sampling Distribution
    The bootstrap method works because the spread of the bootstrap distribution mirrors the spread of the sampling distribution, even though the bootstrap is centered on the sample mean rather than the population mean. The visualization below shows the two distributions together, with a table of each one's mean, standard deviation and width of the middle 95%. The slider controls what sample size is used to build the distributions.
    """)
    return


@app.cell(hide_code=True)
def _(heart_df, mo, pd):
    # Compute all the distributions ahead of time so the visualization updates quickly
    sample_sizes = list(range(25, 425, 25))
    _heart_rates = heart_df["heart_rate"]
    _rows = []
    for _n in sample_sizes:
        _one_sample = _heart_rates.sample(_n, random_state=37)
        for _i in range(1000):
            _sampling_mean = _heart_rates.sample(_n, random_state=_i).mean()
            _resample_mean = _one_sample.sample(_n, replace=True, random_state=_i).mean()
            _rows.append({"sample_size": _n, "distribution": "Sampling", "mean": _sampling_mean})
            _rows.append({"sample_size": _n, "distribution": "Bootstrap", "mean": _resample_mean})
    all_comparisons_df = pd.DataFrame(_rows)

    # Slider for the sample size
    size_slider = mo.ui.slider(steps=sample_sizes, value=100, label="Sample size", show_value=True)
    size_slider
    return all_comparisons_df, size_slider


@app.cell(hide_code=True)
def _(all_comparisons_df, plt, size_slider, sns):
    # The precomputed means for the sample size chosen on the slider
    comparison_df = all_comparisons_df[all_comparisons_df["sample_size"] == size_slider.value]

    # Sampling and bootstrap distributions on the same axis
    sns.histplot(comparison_df, x="mean", hue="distribution")
    plt.xlim(60, 82)
    plt.xlabel("Mean heart rate (beats per minute)")
    plt.ylabel("Number of means")
    plt.show()
    return (comparison_df,)


@app.cell(hide_code=True)
def _(comparison_df, mo):
    # Calculate mean, stdev, and 95% width
    _summary = comparison_df.groupby("distribution")["mean"].agg(["mean", "std"])
    _percentiles = comparison_df.groupby("distribution")["mean"].quantile([0.025, 0.975]).unstack()
    _width = _percentiles[0.975] - _percentiles[0.025]
    mo.md(f"""
    | Distribution | Mean | Standard deviation | Width of middle 95% |
    |---|---|---|---|
    | Sampling | {_summary.loc["Sampling", "mean"]:.2f} | {_summary.loc["Sampling", "std"]:.2f} | {_width["Sampling"]:.2f} |
    | Bootstrap | {_summary.loc["Bootstrap", "mean"]:.2f} | {_summary.loc["Bootstrap", "std"]:.2f} | {_width["Bootstrap"]:.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(size_slider):
    # Same slider as the one above
    size_slider
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Hypothesis Testing
    We will look at a synthesized dataset from an 8-week trial of 200 adults with insomnia. Half were randomly assigned to use a sleep app and half to use no app, and everyone kept a nightly sleep diary. Each row represents one patient, with the following details:
    - group, App or Control (no app)
    - sleep_change, the patient's average nightly sleep in the last week minus the first week, in minutes, so a positive value means they slept more
    """)
    return


@app.cell
def _(pd):
    sleep_df = pd.read_csv("m13_demo_sleep.csv")
    sleep_df
    return (sleep_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Setting Up the Test
    Before looking at the results, we make these choices, like a trial's pre-specified analysis plan:
    - Null hypothesis: the sleep app has no effect on sleep_change compared to no app.
    - Alternative hypothesis: the sleep app changes sleep_change compared to no app.
    - Test statistic: the difference in median sleep_change, App minus Control. The median is less affected by a few patients whose sleep changed a lot.
    - A two-sided test, because the app could increase or decrease sleep.
    - A significance level of 0.05.
    """)
    return


@app.cell
def _():
    significance_level = 0.05
    return (significance_level,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Observed Statistic
    We calculate the median sleep_change in each group, then the difference, App minus Control. This is our observed statistic.
    """)
    return


@app.cell
def _(sleep_df):
    group_medians = sleep_df.groupby("group")["sleep_change"].median()
    group_medians
    return (group_medians,)


@app.cell
def _(group_medians):
    observed_diff = group_medians["App"] - group_medians["Control"]
    observed_diff
    return (observed_diff,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A box plot shows the two groups side by side. The line in the middle of each box is the group's median.
    """)
    return


@app.cell
def _(plt, sleep_df, sns):
    sns.boxplot(sleep_df, x="group", y="sleep_change")
    plt.xlabel("Group")
    plt.ylabel("Change in nightly sleep (minutes)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Permutation Test
    If the app has no effect, the group labels don't matter, so we can shuffle them. We shuffle the labels 10,000 times and compute the difference in medians each time. This forms our permutation distribution.
    """)
    return


@app.cell
def _(pd, sleep_df):
    shuffled_diffs = []
    for _i in range(10000):
        _shuffled = sleep_df.copy()
        # .values drops the index, so pandas doesn't line the shuffled labels back up
        _shuffled["group"] = sleep_df["group"].sample(frac=1, random_state=_i).values
        _medians = _shuffled.groupby("group")["sleep_change"].median()
        shuffled_diffs.append(_medians["App"] - _medians["Control"])
    # Convert the list to a pandas Series
    shuffled_diffs = pd.Series(shuffled_diffs)
    shuffled_diffs
    return (shuffled_diffs,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Permutation Distribution
    The histogram shows the 10,000 shuffled differences. The black lines mark our observed difference of 19 minutes and its opposite, -19, since our test is two-sided.
    """)
    return


@app.cell
def _(observed_diff, plt, shuffled_diffs, sns):
    sns.histplot(x=shuffled_diffs)
    plt.axvline(observed_diff, color="black", linewidth=2, label="Observed difference")
    plt.axvline(-observed_diff, color="black", linewidth=2)
    plt.legend()
    plt.xlabel("Shuffled difference in median sleep change (minutes)")
    plt.ylabel("Number of shuffles")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # p-Value
    The p-value is the share of shuffles with a difference at least as extreme as our observed difference. Since our test is two-sided, a shuffle counts if its difference is at least 19 or at most -19.
    """)
    return


@app.cell
def _(observed_diff, shuffled_diffs):
    extreme_diffs = shuffled_diffs[shuffled_diffs.abs() >= abs(observed_diff)]
    p_value = len(extreme_diffs) / len(shuffled_diffs)
    p_value
    return (p_value,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Statistical Significance
    We compare the p-value to the significance level we chose before looking at the results.
    """)
    return


@app.cell
def _(p_value, significance_level):
    p_value < significance_level
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The p-value of 0.040 is below 0.05, so the result is statistically significant. We reject the null hypothesis: the sleep app changed sleep_change compared to no app, with the App group's median sleep_change 19 minutes higher than the Control group's.
    """)
    return


if __name__ == "__main__":
    app.run()
