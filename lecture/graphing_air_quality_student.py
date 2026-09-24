# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.2",
#     "matplotlib>=3.8,<3.11",
#     "numpy",
#     "pandas==3.0.5",
#     "seaborn>=0.13,<0.14",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, np, pd, plt, sns


@app.cell(hide_code=True)
def title(mo):
    mo.md("""
    # Air Quality and Asthma Analysis

    This dataset covers the full year 2025 in three neighboring cities in a region tracked by the health department: Riverton (a city with a lot of heavy industry), Lakeside (a city with some light industry), and Hillcrest (a mostly residential city with almost no industry).

    Each row is one city's measurements for one day, so every day appears three times, once for each city. It tells you:
    - the date, written as text (for example, 2025-01-01)
    - the week of the year, numbered 1 to 52 (week 1 is January 1 to 7, and so on, and week 52 has 8 days so that the year ends cleanly)
    - the city
    - the air quality index (AQI) in that city
    - the pollen level forecast in that city
    - how many people in that city went to the emergency room for asthma that day

    A higher AQI means worse air. An AQI of 50 or below is considered good, and above 100 is unhealthy for sensitive groups, such as people with asthma. The department wants to know whether bad air days go along with more asthma visits, whether anything else, such as pollen, also matters, and whether the cities differ. You will use charts to find out. Every chart will be posted on the department's website, so each one needs to be clear enough for the public to read.
    """)
    return


@app.cell(hide_code=True)
def step1_md(mo):
    mo.md("""
    ## What does the air quality dataset contain?

    You have been given a year of daily air quality and asthma data for three cities from the regional health department. Before you can make any charts, you need to load the file and look at what is in it.

    **Instructions:** Load `air_quality.csv` into a DataFrame called `df` and display it.
    """)
    return


@app.cell
def step1(pd):
    # Your code here
    return


@app.cell(hide_code=True)
def step2_md(mo):
    mo.md("""
    ## How good was the air this year?

    The department wants to know whether bad air goes along with more asthma visits. Before comparing anything, you need a sense of what the air was like. Across all three cities, were most days clean, or was bad air common?

    **Instructions:** Make a histogram of the daily AQI values.
    """)
    return


@app.cell
def step2(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step2_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Each cell starts with a blank chart, so the chart you drew in the cell above is not carried over. Redraw the chart in the cell below first. Then add a title, label both axes, set the x-axis limits from 0 to 200, and mark the AQI thresholds with a green vertical line at 50 (the top of the good range) and a red vertical line at 100 (where air becomes unhealthy for sensitive groups).
    """)
    return


@app.cell
def step2_pretty(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step3_md(mo):
    mo.md("""
    ## Was the air equally good in every city?

    That histogram lumps the three cities together. But Riverton has a lot of heavy industry and Hillcrest has almost none, so the department suspects the air is not equally good everywhere. Look at the AQI values city by city.

    **Instructions:** Make box plots comparing the daily AQI values of the three cities.
    """)
    return


@app.cell
def step3(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step3_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart in the cell below first. Then set `hue` to the city to tell the boxes apart, add a title, label both axes, and set the y-axis limits from 0 to 200 with ticks every 25 AQI points.
    """)
    return


@app.cell
def step3_pretty(df, np, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step4_md(mo):
    mo.md("""
    ## How often was pollen high?

    Riverton had the worst air, but air pollution is not the only thing that can make breathing harder. The department also tracks pollen, which is worth keeping in mind when you compare air quality with asthma visits. First, see how often each pollen level was reported.

    **Instructions:** Make a bar chart of how many daily readings fell into each pollen level.
    """)
    return


@app.cell
def step4(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step4_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart in the cell below first. Then add a title, label both axes, and set the y-axis limits from 0 to 500 with ticks every 100 readings.
    """)
    return


@app.cell
def step4_pretty(df, np, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step5_md(mo):
    mo.md("""
    ## Are there more asthma visits on bad air days?

    Now you know what the air and pollen looked like across the year. This is the core question for the health department: if worse air goes along with more asthma visits, the department could use AQI forecasts to warn residents.

    **Instructions:** Make a scatter plot of daily asthma visits against AQI.
    """)
    return


@app.cell
def step5(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step5_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart in the cell below first. Then add a title, label both axes, set the x-axis limits from 0 to 200 and the y-axis limits from 0 to 25, and put x-axis ticks every 50 AQI points.
    """)
    return


@app.cell
def step5_pretty(df, np, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step6_md(mo):
    mo.md("""
    ## Do asthma visits go up on high pollen days?

    The scatter plot suggests that asthma visits rise with AQI, but pollen might matter too. To check pollen directly, compare asthma visits across the three pollen levels.

    **Instructions:** Make box plots comparing daily asthma visits across the pollen levels.
    """)
    return


@app.cell
def step6(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step6_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart in the cell below first. Then set `hue` to the pollen level to tell the boxes apart, add a title, label both axes, and set the y-axis limits from 0 to 25.
    """)
    return


@app.cell
def step6_pretty(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step7_md(mo):
    mo.md("""
    ## How did asthma visits change over the year?

    Both air quality and pollen seem to matter. Now look at how asthma visits changed over the whole year, so the department can plan staffing for next year. Daily counts bounce around a lot, so look at the year one week at a time (across all three cities) to make the busy stretches easier to see.

    **Instructions:** Make a line chart of the average number of asthma visits for each week. Add a red horizontal line at the overall average of the daily asthma visits values.
    """)
    return


@app.cell
def step7(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step7_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart, including the red line, in the cell below first. Then, if your chart has a shaded band, remove it by adding `errorbar=None` to the plotting call. Also add a title, label both axes, set the x-axis limits from 1 to 52 with ticks every 4 weeks (4, 8, and so on up to 52), and set the y-axis limits from 0 to 20.
    """)
    return


@app.cell
def step7_pretty(df, np, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step8_md(mo):
    mo.md("""
    ## Did every city follow the same pattern?

    The weekly chart averages all three cities together. But the cities have different amounts of industry, and so different air, so the department wants to know whether each city followed the same yearly pattern, or whether one city stood out.

    **Instructions:** Make a line chart of the average number of asthma visits for each week, with a separate line for each city.
    """)
    return


@app.cell
def step8(df, plt, sns):
    # Your code here
    return


@app.cell(hide_code=True)
def step8_pretty_md(mo):
    mo.md("""
    **Make it ready for the public:** Redraw the chart in the cell below first. Then remove the shaded bands around the lines by adding `errorbar=None` to the plotting call, add a title, label both axes, set the x-axis limits from 1 to 52 with ticks every 4 weeks (4, 8, and so on up to 52), and set the y-axis limits from 0 to 20.
    """)
    return


@app.cell
def step8_pretty(df, np, plt, sns):
    # Your code here
    return


if __name__ == "__main__":
    app.run()
