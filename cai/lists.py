# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///
import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Lists: Practice Problems

    This notebook introduces Python lists through a series of problems set in a medical data
    science context. Each section covers one aspect of lists, starting at an easy level before
    building toward harder problems that combine ideas from earlier sections.

    **Prerequisites:** variables, numbers, strings, `range()`, comparisons (`<`, `>`, `==`, etc.),
    boolean operations (`and`, `or`, `not`), `if`/`elif`/`else`, `while` loops, and `for` loops
    with `range()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1: Creating Lists

    A **list** stores multiple values in a single variable, in order. You write a list using
    square brackets `[]`, with items separated by commas:

    ```python
    temperatures = [98.6, 99.1, 100.4, 98.2]
    patient_ids  = ["MRN001", "MRN002", "MRN003"]
    empty_list   = []
    ```

    Lists can hold integers, floats, strings, booleans, or a mix of types. An empty list
    `[]` is valid and useful. You will add items to it in later sections.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Create a list called `ages` containing the ages of five patients: 34, 67, 45, 23, 89.
    """)
    return


@app.cell
def _():
    _ages = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nages = [34, 67, 45, 23, 89]\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Create a list called `systolic_bp` containing five blood pressure readings: 120, 134, 118, 145, 122.
    """)
    return


@app.cell
def _():
    _systolic_bp = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nsystolic_bp = [120, 134, 118, 145, 122]\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Create a list called `patient_ids` containing three ID strings: `"MRN001"`, `"MRN002"`, `"MRN003"`.
    """)
    return


@app.cell
def _():
    _patient_ids = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\npatient_ids = ["MRN001", "MRN002", "MRN003"]\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Create an empty list called `flagged_patients`. You will add items to it in a later section.
    """)
    return


@app.cell
def _():
    _flagged_patients = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nflagged_patients = []\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** A list can hold values of different types. Create a list called `record`
    that holds the following information about a single patient in order: name `"Alice"`,
    age `42`, temperature `100.1`, and admitted status `False`.

    *Note: mixing types in one list is allowed, though later sections show a better way to
    organize multi-patient data.*
    """)
    return


@app.cell
def _():
    _record = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nrecord = ["Alice", 42, 100.1, False]\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 2: Helper Functions

    Python provides built-in functions that immediately give you useful facts about a list.

    ```python
    readings = [92.5, 110.3, 88.7, 145.2]

    len(readings)   # 4     (number of items)
    sum(readings)   # 436.7 (total of all items)
    max(readings)   # 145.2 (largest item)
    min(readings)   # 88.7  (smallest item)
    ```

    There is no built-in `average()`, but you can compute one:

    ```python
    average = sum(readings) / len(readings)
    ```

    `round(value, n)` rounds a number to `n` decimal places:

    ```python
    round(3.14159, 2)   # 3.14
    round(average, 2)   # rounds the average to 2 decimal places
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Given the list below, print how many readings were recorded.

    Expected output: `7`
    """)
    return


@app.cell
def _():
    _heart_rate = [72, 85, 91, 78, 95, 88, 83]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nheart_rate = [72, 85, 91, 78, 95, 88, 83]
print(len(heart_rate))\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Using the same `heart_rate` list, print the highest and lowest values.

    Expected output:
    ```
    Max: 95
    Min: 72
    ```
    """)
    return


@app.cell
def _():
    _heart_rate = [72, 85, 91, 78, 95, 88, 83]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nheart_rate = [72, 85, 91, 78, 95, 88, 83]
print("Max:", max(heart_rate))
print("Min:", min(heart_rate))\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Compute and print the average heart rate from the `heart_rate` list,
    rounded to two decimal places.

    Expected output: `Average: 84.57`
    """)
    return


@app.cell
def _():
    _heart_rate = [72, 85, 91, 78, 95, 88, 83]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nheart_rate = [72, 85, 91, 78, 95, 88, 83]
average = sum(heart_rate) / len(heart_rate)
print("Average:", round(average, 2))\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** The following list contains fasting glucose readings (mg/dL) from one
    patient over a week. The normal upper limit for fasting glucose is 99 mg/dL. Using
    `max()` and an `if`/`else` statement, print `"Peak glucose is elevated."` if the highest
    reading exceeds 99, or `"All readings within range."` otherwise.
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
if max(glucose) > 99:
    print("Peak glucose is elevated.")
else:
    print("All readings within range.")\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The `in` operator

    You can test whether a value is present in a list using `in`. The result is a boolean:

    ```python
    110.3 in glucose    # True
    55.0  in glucose    # False
    ```

    This is the same `in` keyword used in `for x in range(n)`, but here it is a membership
    test, not a loop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** Check whether a glucose reading of `145.2` is in the `glucose` list
    from Problem 4. Print `"Reading present."` or `"Reading not found."`.
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
if 145.2 in glucose:
    print("Reading present.")
else:
    print("Reading not found.")\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** White blood cell (WBC) count is considered elevated above 11.0 (x10³/uL).
    Given the list below, use `max()` and an `if`/`else` to print `"WBC elevated."` or
    `"WBC normal."`.
    """)
    return


@app.cell
def _():
    _wbc = [6.2, 7.1, 8.4, 9.3, 10.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwbc = [6.2, 7.1, 8.4, 9.3, 10.8]
if max(wbc) > 11.0:
    print("WBC elevated.")
else:
    print("WBC normal.")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### `sorted()`

    `sorted(lst)` returns a **new** sorted list without changing the original:

    ```python
    original  = [92.5, 110.3, 88.7]
    ascending = sorted(original)     # [88.7, 92.5, 110.3]
    print(original)                  # [92.5, 110.3, 88.7]  (unchanged)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** Print the `glucose` readings from Problem 4 in ascending order. Then
    print the original list to confirm it was not modified.
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
print(sorted(glucose))
print(glucose)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** You have patient counts from two separate clinics:

    ```python
    clinic_a = [14, 22, 18, 9, 31]
    clinic_b = [7, 19, 25]
    ```

    Without looking at the numbers, use `len()`, `sum()`, and `max()` to print:

    - which clinic had more recorded days
    - which clinic had the higher total patient count
    - the single highest daily count across both clinics

    *Hint: you can call `max()` with two arguments: `max(x, y)` returns the larger of the two.*
    """)
    return


@app.cell
def _():
    _clinic_a = [14, 22, 18, 9, 31]
    _clinic_b = [7, 19, 25]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nclinic_a = [14, 22, 18, 9, 31]
clinic_b = [7, 19, 25]
if len(clinic_a) > len(clinic_b):
    print("Clinic A had more recorded days.")
else:
    print("Clinic B had more recorded days.")
if sum(clinic_a) > sum(clinic_b):
    print("Clinic A had the higher total patient count.")
else:
    print("Clinic B had the higher total patient count.")
print("Highest daily count:", max(max(clinic_a), max(clinic_b)))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 3: Indexing

    ### Positive indexing

    Every item in a list has an **index**, which is its position counting from zero:

    ```python
    readings = [92.5, 110.3, 88.7, 145.2]
    #           [0]   [1]    [2]   [3]
    ```

    Access an item by writing its index in square brackets:

    ```python
    readings[0]   # 92.5
    readings[2]   # 88.7
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Print the first glucose reading.

    Expected output: `92.5`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
print(glucose[0])\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Print the third glucose reading (index 2).

    Expected output: `88.7`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
print(glucose[2])\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** The hyperglycemia threshold is 126 mg/dL. Check whether the fourth
    reading (index 3) exceeds this threshold. Print `"Hyperglycemic"` or `"Normal"`.
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
if glucose[3] > 126:
    print("Hyperglycemic")
else:
    print("Normal")\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Negative indexing

    You can count from the **end** of a list using negative indices. `-1` is the last item,
    `-2` is the second-to-last, and so on:

    ```python
    readings[-1]   # 99.8   (last)
    readings[-2]   # 145.2  (second to last)
    ```

    This is useful when you want the most recent entry without knowing how long the list is.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Print the last glucose reading using a negative index.

    Expected output: `99.8`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
print(glucose[-1])\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** Print the second-to-last glucose reading.

    Expected output: `145.2`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
print(glucose[-2])\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** A temperature of 100.4°F or higher indicates a fever. Using a negative
    index, check whether the most recent temperature in the list below is a fever. Print
    `"Fever"` or `"No fever"`.
    """)
    return


@app.cell
def _():
    _hourly_temps = [98.6, 98.9, 99.4, 100.1, 100.7]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nhourly_temps = [98.6, 98.9, 99.4, 100.1, 100.7]
if hourly_temps[-1] >= 100.4:
    print("Fever")
else:
    print("No fever")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modifying items by index

    You can replace any item by assigning to its index:

    ```python
    readings[0] = 95.0    # replaces the first item with 95.0
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** A technician recorded the second glucose reading incorrectly. Replace it
    with `97.4` and print the updated list.

    Expected output: `[92.5, 97.4, 88.7, 145.2, 99.8]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
glucose[1] = 97.4
print(glucose)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** A monitoring device stores `[min_hr, max_hr]` for the past 24 hours.
    After re-analysis, the true maximum heart rate was found to be `109` instead of `112`.
    Update the list to correct the maximum, then print: `"HR range: <min> to <max>"`.

    Expected output: `HR range: 58 to 109`
    """)
    return


@app.cell
def _():
    _hr_range = [58, 112]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nhr_range = [58, 112]
hr_range[1] = 109
print("HR range:", hr_range[0], "to", hr_range[1])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 9.** The normal range for systolic blood pressure is 90-120 mmHg. Given the
    list below, use indexing to check whether the *first* and *last* readings are both within
    the normal range. Print one of:

    - `"Both readings normal."`
    - `"First reading abnormal."`
    - `"Last reading abnormal."`
    - `"Both readings abnormal."`
    """)
    return


@app.cell
def _():
    _bp = [118, 132, 109, 145, 124]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nbp = [118, 132, 109, 145, 124]
first_normal = 90 <= bp[0] <= 120
last_normal = 90 <= bp[-1] <= 120
if first_normal and last_normal:
    print("Both readings normal.")
elif not first_normal and last_normal:
    print("First reading abnormal.")
elif first_normal and not last_normal:
    print("Last reading abnormal.")
else:
    print("Both readings abnormal.")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 4: Slicing

    ### Basic slicing

    **Slicing** extracts a portion of a list and returns it as a new list. The syntax is
    `lst[start:stop]`, where `stop` is *exclusive* (not included in the result):

    ```python
    glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    glucose[1:4]   # [110.3, 88.7, 145.2]                   (indices 1, 2, 3)
    glucose[:3]    # [92.5, 110.3, 88.7]                    (from the beginning)
    glucose[2:]    # [88.7, 145.2, 99.8, 103.6, 115.4]      (to the end)
    ```

    Slicing never raises an error if your indices are out of range; Python simply gives you
    what it can.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Extract and print the first three glucose readings.

    Expected output: `[92.5, 110.3, 88.7]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[:3])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Extract and print the last two glucose readings using a negative start index.

    Expected output: `[103.6, 115.4]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[-2:])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** A patient was monitored for 7 days. Days 3 through 5 (indices 2 through 4)
    coincided with a medication trial. Extract just those readings.

    Expected output: `[88.7, 145.2, 99.8]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[2:5])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** The first reading is a baseline taken before treatment. Extract all
    readings *after* the baseline (index 1 onward) and print them.

    Expected output: `[110.3, 88.7, 145.2, 99.8, 103.6, 115.4]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[1:])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Slicing with a step

    A third value `lst[start:stop:step]` controls how many positions to advance each time:

    ```python
    glucose[::2]    # every other item (indices 0, 2, 4, 6): [92.5, 88.7, 99.8, 115.4]
    glucose[::-1]   # reversed: [115.4, 103.6, 99.8, 145.2, 88.7, 110.3, 92.5]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** Print every other reading from the `glucose` list, starting from index 0.

    Expected output: `[92.5, 88.7, 99.8, 115.4]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[::2])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** Print the readings in reverse order.

    Expected output: `[115.4, 103.6, 99.8, 145.2, 88.7, 110.3, 92.5]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 115.4]
print(glucose[::-1])\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** A clinical trial recorded 10 measurements:

    ```python
    trial = [4.1, 3.8, 5.2, 4.9, 3.7, 5.5, 4.3, 4.8, 5.1, 3.9]
    ```

    Use slicing to create `first_half` (first 5 readings) and `second_half` (last 5
    readings). Print the maximum of each half, then print which half had the higher peak.
    """)
    return


@app.cell
def _():
    _trial = [4.1, 3.8, 5.2, 4.9, 3.7, 5.5, 4.3, 4.8, 5.1, 3.9]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\ntrial = [4.1, 3.8, 5.2, 4.9, 3.7, 5.5, 4.3, 4.8, 5.1, 3.9]
first_half = trial[:5]
second_half = trial[5:]
print("First half max:", max(first_half))
print("Second half max:", max(second_half))
if max(first_half) > max(second_half):
    print("First half had the higher peak.")
else:
    print("Second half had the higher peak.")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** A lab logs one blood draw per hour, starting at midnight (index 0 = midnight,
    index 1 = 1am, etc.).

    ```python
    glucose_hourly = [95.1, 88.3, 82.7, 79.4, 91.2, 103.6, 118.4,
                      132.1, 145.7, 138.2, 122.9, 109.4]
    ```

    Use slicing to extract readings from 6am through 11am (indices 6 through 11), then use
    `max()` and `min()` to print the highest and lowest readings during that window.
    """)
    return


@app.cell
def _():
    _glucose_hourly = [
        95.1,
        88.3,
        82.7,
        79.4,
        91.2,
        103.6,
        118.4,
        132.1,
        145.7,
        138.2,
        122.9,
        109.4,
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose_hourly = [95.1, 88.3, 82.7, 79.4, 91.2, 103.6, 118.4,
                  132.1, 145.7, 138.2, 122.9, 109.4]
window = glucose_hourly[6:12]
print("Highest:", max(window))
print("Lowest:", min(window))\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 5: List Methods

    Lists have built-in **methods**: functions attached to the list itself, called with dot
    notation: `my_list.method_name(arguments)`.

    ### Adding and removing items: `append`, `pop`

    ```python
    readings = [92.5, 110.3, 88.7]

    readings.append(99.4)    # add to end        -> [92.5, 110.3, 88.7, 99.4]
    readings.pop()           # remove last        -> returns 99.4; list is [92.5, 110.3, 88.7]
    readings.pop(0)          # remove at index 0  -> returns 92.5; list is [110.3, 88.7]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** A new glucose reading of `95.2` just arrived. Add it to the end of the
    list and print the updated list.

    Expected output: `[92.5, 110.3, 88.7, 145.2, 95.2]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2]
glucose.append(95.2)
print(glucose)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** The last reading in the list was logged twice by mistake. Remove it and
    print the corrected list.

    Expected output: `[120, 134, 118, 145]`
    """)
    return


@app.cell
def _():
    _bp = [120, 134, 118, 145, 145]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nbp = [120, 134, 118, 145, 145]
bp.pop()
print(bp)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** A patient queue is stored as a list, with the next patient at the front
    (index 0). Remove the first patient, print their name, then print the remaining queue.

    Expected output:
    ```
    Now seeing: Alice
    Remaining queue: ['Bob', 'Carol', 'David']
    ```
    """)
    return


@app.cell
def _():
    _queue = ["Alice", "Bob", "Carol", "David"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nqueue = ["Alice", "Bob", "Carol", "David"]
next_patient = queue.pop(0)
print("Now seeing:", next_patient)
print("Remaining queue:", queue)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Inserting and removing specific values: `insert`, `remove`

    ```python
    readings.insert(0, 999)    # insert 999 at index 0; everything else shifts right
    readings.remove(88.7)      # remove the first occurrence of 88.7
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** An urgent stat reading of `200` must be placed at the very beginning of
    the list. Insert it at index 0 and print the result.

    Expected output: `[200, 92.5, 110.3, 88.7]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7]
glucose.insert(0, 200)
print(glucose)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** A sensor error logged `-1` in the data. Remove the first occurrence of
    `-1` and print the corrected list.

    Expected output: `[72, 85, 78, 90, -1, 68]`

    *Note: only the first `-1` is removed.*
    """)
    return


@app.cell
def _():
    _heart_rate = [72, 85, -1, 78, 90, -1, 68]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nheart_rate = [72, 85, -1, 78, 90, -1, 68]
heart_rate.remove(-1)
print(heart_rate)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Combining lists: `extend`

    `lst.extend(other)` appends every item from `other` onto `lst`:

    ```python
    ward_a = [120, 118]
    ward_b = [132, 115]
    ward_a.extend(ward_b)    # ward_a is now [120, 118, 132, 115]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** Combine readings from two wards into one list, then print the combined
    list sorted from lowest to highest. *(Hint: use `sorted()` from Section 2.)*
    """)
    return


@app.cell
def _():
    _ward_a = [130, 128, 142]
    _ward_b = [119, 125, 138, 121]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nward_a = [130, 128, 142]
ward_b = [119, 125, 138, 121]
ward_a.extend(ward_b)
print(sorted(ward_a))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Inspecting values: `count`, `index`

    ```python
    readings = [120, 135, 120, 118, 120]
    readings.count(120)    # 3  (how many times 120 appears)
    readings.index(135)    # 1  (index of the first occurrence of 135)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** How many times does a glucose reading of `120` appear in the log?
    Print: `"Reading 120 appears X time(s)."` (replace X with the result).
    """)
    return


@app.cell
def _():
    _glucose_log = [110, 120, 135, 120, 118, 120, 109]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose_log = [110, 120, 135, 120, 118, 120, 109]
count = glucose_log.count(120)
print("Reading 120 appears", count, "time(s).")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** Find and print the index of the first occurrence of `145` in the list.

    Expected output: `First occurrence of 145 is at index 3.`
    """)
    return


@app.cell
def _():
    _bp_readings = [120, 134, 118, 145, 122, 145, 139]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nbp_readings = [120, 134, 118, 145, 122, 145, 139]
print("First occurrence of 145 is at index", str(bp_readings.index(145)) + ".")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sorting and reversing: `sort`, `reverse`

    `.sort()` and `.reverse()` change the list **in place**: they modify the original and
    return `None`. This differs from `sorted()`, which leaves the original alone and returns
    a new list.

    ```python
    readings = [3, 1, 4, 1, 5]
    readings.sort()      # readings is now [1, 1, 3, 4, 5]
    readings.reverse()   # readings is now [5, 4, 3, 1, 1]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 9.** Sort the ages list in ascending order, then print the sorted list and the age of the youngest patient.
    """)
    return


@app.cell
def _():
    _ages = [67, 34, 89, 45, 23]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nages = [67, 34, 89, 45, 23]
ages.sort()
print(ages)
print("Youngest:", ages[0])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 10.** Using methods from this section, print the three **lowest** blood
    pressure readings from the list below.

    *Hint: sort first, then slice.*
    """)
    return


@app.cell
def _():
    _bp = [145, 112, 138, 108, 129, 152, 117]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nbp = [145, 112, 138, 108, 129, 152, 117]
bp.sort()
print(bp[:3])\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 11.** *(Challenge)* A patient queue processes patients in order. Simulate the
    following sequence of events, printing a status message after each step:

    1. See the next patient (remove from the front).
    2. Add `"David"` to the back of the queue.
    3. See the next patient.
    4. Add `"Eve"` to the back of the queue.
    5. Print the final queue.

    Expected output:
    ```
    Now seeing: Alice
    Now seeing: Bob
    Final queue: ['Carol', 'David', 'Eve']
    ```
    """)
    return


@app.cell
def _():
    _queue = ["Alice", "Bob", "Carol"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nqueue = ["Alice", "Bob", "Carol"]
next_patient = queue.pop(0)
print("Now seeing:", next_patient)
queue.append("David")
next_patient = queue.pop(0)
print("Now seeing:", next_patient)
queue.append("Eve")
print("Final queue:", queue)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 6: Iterating Over Lists with For Loops

    ### Looping directly over a list

    You already know `for i in range(n)`. You can also loop directly over a list; each
    iteration gives you one item:

    ```python
    temperatures = [98.6, 99.1, 100.4]

    for temp in temperatures:
        print(temp)
    ```

    Output:
    ```
    98.6
    99.1
    100.4
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Print each patient name on its own line.
    """)
    return


@app.cell
def _():
    _patients = ["Alice", "Bob", "Carol", "David", "Eve"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\npatients = ["Alice", "Bob", "Carol", "David", "Eve"]
for name in patients:
    print(name)\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Loop over the WBC counts below and print each one followed by
    `"(normal)"` if it is between 4.5 and 11.0 (inclusive), or `"(abnormal)"` otherwise.

    Expected output:
    ```
    6.2 (normal)
    7.1 (normal)
    12.4 (abnormal)
    9.3 (normal)
    3.8 (abnormal)
    ```
    """)
    return


@app.cell
def _():
    _wbc = [6.2, 7.1, 12.4, 9.3, 3.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwbc = [6.2, 7.1, 12.4, 9.3, 3.8]
for count in wbc:
    if 4.5 <= count <= 11.0:
        print(count, "(normal)")
    else:
        print(count, "(abnormal)")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Using a `for` loop (not `sum()`), compute and print the total of all
    readings.

    Expected output: `Total: 536.5`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8]
total = 0
for g in glucose:
    total = total + g
print("Total:", total)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Getting both index and value: `enumerate`

    When you need the index *and* the value during a loop, use `enumerate()`:

    ```python
    for i, temp in enumerate(temperatures):
        print(i, temp)
    ```

    Output:
    ```
    0 98.6
    1 99.1
    2 100.4
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Print each patient's name with their patient number, starting from 1.

    Expected output:
    ```
    Patient 1: Alice
    Patient 2: Bob
    Patient 3: Carol
    Patient 4: David
    ```
    """)
    return


@app.cell
def _():
    _patients = ["Alice", "Bob", "Carol", "David"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\npatients = ["Alice", "Bob", "Carol", "David"]
for i, name in enumerate(patients):
    print("Patient", str(i + 1) + ":", name)\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** A temperature sensor logged readings every hour. Using `enumerate()`,
    print the hour number (starting from 1) and temperature for every reading that is a
    fever (>= 100.4°F).

    Expected output:
    ```
    Hour 3: 100.4 (fever)
    Hour 4: 101.2 (fever)
    Hour 5: 100.8 (fever)
    ```
    """)
    return


@app.cell
def _():
    _hourly_temps = [98.6, 99.1, 100.4, 101.2, 100.8, 99.5, 98.9]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nhourly_temps = [98.6, 99.1, 100.4, 101.2, 100.8, 99.5, 98.9]
for i, temp in enumerate(hourly_temps):
    if temp >= 100.4:
        print("Hour", str(i + 1) + ":", temp, "(fever)")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Building new lists inside a loop

    A common pattern is to start with an empty list and append items that meet a condition:

    ```python
    elevated = []
    for g in glucose:
        if g >= 100:
            elevated.append(g)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** Build and print a list of all glucose readings that fall in the normal
    fasting range (70-99 mg/dL, inclusive).

    Expected output: `[92.5, 88.7, 99.8, 97.2]`
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 97.2]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 103.6, 97.2]
normal = []
for g in glucose:
    if 70 <= g <= 99:
        normal.append(g)
print(normal)\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** Build a list called `categories` where each entry is `"normal"` if the
    corresponding WBC count is between 4.5 and 11.0 (inclusive), or `"abnormal"` otherwise.
    Print the `categories` list.

    Expected output: `['normal', 'normal', 'abnormal', 'normal', 'abnormal', 'normal']`
    """)
    return


@app.cell
def _():
    _wbc = [6.2, 7.1, 12.4, 9.3, 3.8, 8.9]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {"💡 Show solution": """\n```python\nwbc = [6.2, 7.1, 12.4, 9.3, 3.8, 8.9]
categories = []
for count in wbc:
    if 4.5 <= count <= 11.0:
        categories.append("normal")
    else:
        categories.append("abnormal")
print(categories)\n```\n"""}
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** Without using `max()`, find both the largest glucose reading and the
    index at which it first appears. Print: `"Peak reading: X at index Y."`.

    *Hint: track two variables (the largest value seen so far and its index) and update
    both whenever you find a new maximum.*
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 99.8, 141.0]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 99.8, 141.0]
peak = glucose[0]
peak_index = 0
for i, g in enumerate(glucose):
    if g > peak:
        peak = g
        peak_index = i
print("Peak reading:", peak, "at index", str(peak_index) + ".")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 9.** *(Challenge)* Find the index of the **first** glucose reading that
    exceeds 140 mg/dL. If no reading exceeds 140, print `"No elevated reading found."`.

    *Hint: use a variable `found_index = -1` initialized before the loop. Only update it
    the first time you find a reading above 140 (check that `found_index == -1` before
    updating). After the loop, check whether `found_index` was ever changed.*
    """)
    return


@app.cell
def _():
    _glucose = [92.5, 110.3, 88.7, 145.2, 103.6, 141.0]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nglucose = [92.5, 110.3, 88.7, 145.2, 103.6, 141.0]
found_index = -1
for i, g in enumerate(glucose):
    if g > 140 and found_index == -1:
        found_index = i
if found_index == -1:
    print("No elevated reading found.")
else:
    print(found_index)\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 10.** *(Challenge)* Given a list of systolic blood pressure readings, build
    two new lists:

    - `normal`: readings in the range 90-120 mmHg
    - `abnormal`: readings outside that range

    Print both lists, then print the percentage of readings that were abnormal (rounded to
    one decimal place).
    """)
    return


@app.cell
def _():
    _bp_readings = [118, 145, 109, 132, 98, 121, 88, 115, 152, 104]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Show solution": """\n```python\nbp_readings = [118, 145, 109, 132, 98, 121, 88, 115, 152, 104]
normal = []
abnormal = []
for bp in bp_readings:
    if 90 <= bp <= 120:
        normal.append(bp)
    else:
        abnormal.append(bp)
print(normal)
print(abnormal)
pct = round(len(abnormal) / len(bp_readings) * 100, 1)
print(str(pct) + "% of readings were abnormal.")\n```\n"""
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 7: Nested Lists

    ### Creating and accessing nested lists

    A list can contain other lists as items. A **nested list** is the natural way to
    represent a table of records in Python.

    ```python
    patients = [
        ["Alice", 34, 98.6],
        ["Bob",   67, 101.2],
        ["Carol", 45, 99.5]
    ]
    ```

    Each inner list is one row. To reach a single value, index twice: first select the
    row, then select the column within it:

    ```python
    patients[0]      # ["Alice", 34, 98.6]   (entire first row)
    patients[0][0]   # "Alice"               (row 0, column 0)
    patients[1][2]   # 101.2                 (row 1, column 2)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Print the name of the second patient.

    Expected output: `Bob`
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
print(patients[1][0])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Print the temperature of the third patient.

    Expected output: `99.5`
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
print(patients[2][2])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Carol's temperature was re-measured and is actually `100.2`. Update that value in the nested list and print the updated `patients`.
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
patients[2][2] = 100.2
print(patients)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Iterating over nested lists

    Loop over the outer list to process one row at a time:

    ```python
    for patient in patients:
        name = patient[0]
        temp = patient[2]
        print(name, temp)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Print the name and temperature of every patient, one per line.

    Expected output:
    ```
    Alice 98.6
    Bob 101.2
    Carol 99.5
    ```
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
for patient in patients:
    print(patient[0], patient[2])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** A fever is a temperature of 100.4°F or higher. Print the name of every patient who currently has a fever.
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
for patient in patients:
    if patient[2] >= 100.4:
        print(patient[0])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** Compute and print the average age of all patients, rounded to one decimal
    place.

    Expected output: `Average age: 48.7`
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
total_age = 0
for patient in patients:
    total_age = total_age + patient[1]
print("Average age:", round(total_age / len(patients), 1))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 7.** A new patient `["David", 52, 100.1]` has arrived. Add their record to the `patients` list and print the updated list.
    """)
    return


@app.cell
def _():
    _patients = [
        ["Alice", 34, 98.6],
        ["Bob", 67, 101.2],
        ["Carol", 45, 99.5],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [
    ["Alice", 34, 98.6],
    ["Bob",   67, 101.2],
    ["Carol", 45, 99.5],
]
patients.append(["David", 52, 100.1])
print(patients)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 8.** Each inner list below stores `[patient_id, glucose, systolic_bp]`.
    Without using `max()`, find and print the patient ID of the patient with the highest
    glucose reading.

    *Hint: track both the highest glucose seen so far and the corresponding patient ID,
    updating both whenever you find a new maximum.*
    """)
    return


@app.cell
def _():
    _records = [
        ["P001", 92.5, 120],
        ["P002", 145.2, 148],
        ["P003", 88.7, 112],
        ["P004", 110.3, 138],
        ["P005", 99.8, 125],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nrecords = [
    ["P001", 92.5,  120],
    ["P002", 145.2, 148],
    ["P003", 88.7,  112],
    ["P004", 110.3, 138],
    ["P005", 99.8,  125],
]
top_id = records[0][0]
top_glucose = records[0][1]
for record in records:
    if record[1] > top_glucose:
        top_glucose = record[1]
        top_id = record[0]
print(top_id)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 9.** Using the same `records` list, build two new lists of patient IDs:

    - `high_glucose`: patients whose glucose exceeds 100 mg/dL
    - `high_bp`: patients whose systolic BP exceeds 130 mmHg

    Print both lists.
    """)
    return


@app.cell
def _():
    _records = [
        ["P001", 92.5, 120],
        ["P002", 145.2, 148],
        ["P003", 88.7, 112],
        ["P004", 110.3, 138],
        ["P005", 99.8, 125],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nrecords = [
    ["P001", 92.5,  120],
    ["P002", 145.2, 148],
    ["P003", 88.7,  112],
    ["P004", 110.3, 138],
    ["P005", 99.8,  125],
]
high_glucose = []
high_bp = []
for record in records:
    if record[1] > 100:
        high_glucose.append(record[0])
    if record[2] > 130:
        high_bp.append(record[0])
print(high_glucose)
print(high_bp)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 10.** *(Challenge)* Using the `records` list, compute and print:

    - the average glucose across all patients (rounded to one decimal place)
    - the number of patients who have **both** elevated glucose (> 100) and elevated BP (> 130)

    Then print those patients' IDs.
    """)
    return


@app.cell
def _():
    _records = [
        ["P001", 92.5, 120],
        ["P002", 145.2, 148],
        ["P003", 88.7, 112],
        ["P004", 110.3, 138],
        ["P005", 99.8, 125],
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nrecords = [
    ["P001", 92.5,  120],
    ["P002", 145.2, 148],
    ["P003", 88.7,  112],
    ["P004", 110.3, 138],
    ["P005", 99.8,  125],
]
total_glucose = 0
for record in records:
    total_glucose = total_glucose + record[1]
print("Average glucose:", round(total_glucose / len(records), 1))
both_elevated = []
for record in records:
    if record[1] > 100 and record[2] > 130:
        both_elevated.append(record[0])
print(len(both_elevated), "patient(s) have both elevated glucose and BP:")
print(both_elevated)\n```\n"""})
    return


if __name__ == "__main__":
    app.run()
