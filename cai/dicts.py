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
    # Python Dictionaries: Practice Problems

    This notebook introduces Python dictionaries through a series of problems set in a medical
    data science context. Each section covers one aspect of dictionaries, starting with simple
    creation and lookup before building toward harder problems that combine ideas from earlier
    sections.

    **Prerequisites:** variables, numbers, strings, booleans, comparisons (`<`, `>`, `==`, etc.),
    boolean operations (`and`, `or`, `not`), `if`/`elif`/`else`, `for` loops, and Python lists
    (as covered in the Lists notebook).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1: Creating Dictionaries (Literal Syntax)

    ### What is a Dictionary?

    A **dictionary** stores pairs of data. Each pair has a **key** and a **value**. You use the
    key to look up the value, similar to how a patient chart uses a field name to look up a
    measurement.

    Dictionaries are written with curly braces `{}`. Each key-value pair is separated by a
    colon `:`, and pairs are separated by commas:

    ```python
    heart_rates = {"P001": 72, "P002": 85, "P003": 68}
    ```

    Here, `"P001"`, `"P002"`, and `"P003"` are patient ID keys, and `72`, `85`, `68` are
    heart rate values.

    A few rules:
    - Keys must be **unique**: you cannot have two identical keys in one dictionary.
    - Keys are usually strings or numbers.
    - Values can be any type: numbers, strings, booleans, lists, other dictionaries, etc.
    - An empty dictionary is written as `{}`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.1.** Create a dictionary called `heart_rates` that maps three patient IDs
    (as strings) to their heart rates (as integers). For example, `"P001"` maps to `72`.
    Print the dictionary.
    """)
    return


@app.cell
def _():
    _heart_rates = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nheart_rates = {"P001": 72, "P002": 85, "P003": 68}\nprint(heart_rates)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.2.** Create a dictionary called `glucose_levels` that maps three patient IDs
    to their fasting glucose readings (as integers). Print the dictionary.
    """)
    return


@app.cell
def _():
    _glucose_levels = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose_levels = {"P001": 92, "P002": 110, "P003": 88}\nprint(glucose_levels)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.3.** Create an empty dictionary called `chart`. Print it.

    Expected output: `{}`
    """)
    return


@app.cell
def _():
    _chart = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nchart = {}\nprint(chart)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.4.** Create a dictionary called `patient` that describes a single patient.
    It should have the following key-value pairs:
    - `"mrn"` -> a string (e.g., `"MRN001"`)
    - `"age"` -> an integer
    - `"temperature"` -> a float (e.g., `98.6`)
    - `"admitted"` -> a boolean

    Print the dictionary.
    """)
    return


@app.cell
def _():
    _patient = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatient = {"mrn": "MRN001", "age": 45, "temperature": 98.6, "admitted": True}\nprint(patient)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.5.** Create a dictionary called `medication` that represents a drug with at
    least four fields of your choosing (for example: name, dose_mg, frequency,
    requires_monitoring). Print the dictionary.
    """)
    return


@app.cell
def _():
    _medication = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nmedication = {"name": "metformin", "dose_mg": 500, "frequency": "twice daily", "requires_monitoring": True}\nprint(medication)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.6.** You are given the following two lists:

    ```python
    patient_ids = ["P001", "P002", "P003", "P004"]
    systolic_bp = [118, 134, 122, 145]
    ```

    Without using any loops, create a dictionary called `bp_map` that maps each patient ID
    to their systolic blood pressure reading. Print the dictionary.

    *Hint: Write out the dictionary literal by hand, using the values from the lists.*
    """)
    return


@app.cell
def _():
    _patient_ids = ["P001", "P002", "P003", "P004"]
    _systolic_bp = [118, 134, 122, 145]
    _bp_map = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatient_ids = ["P001", "P002", "P003", "P004"]\nsystolic_bp = [118, 134, 122, 145]\nbp_map = {"P001": 118, "P002": 134, "P003": 122, "P004": 145}\nprint(bp_map)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 2: Indexing

    ### Reading and Writing Individual Values

    Once you have a dictionary, you access a value by writing the key inside square brackets:

    ```python
    heart_rates = {"P001": 72, "P002": 85}
    print(heart_rates["P001"])   # prints 72
    ```

    You can **change** a value using the same syntax on the left side of an assignment:

    ```python
    heart_rates["P001"] = 68     # P001's heart rate updated
    ```

    You can **add** a new key-value pair the same way; if the key does not exist yet,
    it is created:

    ```python
    heart_rates["P003"] = 91     # adds a new patient entry
    ```

    You can **delete** a key-value pair with `del`:

    ```python
    del heart_rates["P002"]      # removes P002 from the dictionary
    ```

    If you try to access a key that does not exist, Python raises a `KeyError`. You will
    learn a safer way to do this in the next section.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.1.**

    ```python
    heart_rates = {"P001": 72, "P002": 85, "P003": 91}
    ```

    Print the heart rate of patient `"P002"`.
    """)
    return


@app.cell
def _():
    _heart_rates = {"P001": 72, "P002": 85, "P003": 91}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nheart_rates = {"P001": 72, "P002": 85, "P003": 91}\nprint(heart_rates["P002"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.2.**

    ```python
    glucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    ```

    Patient P002's glucose was re-measured and is now `105.1`. Update the dictionary and
    print it.
    """)
    return


@app.cell
def _():
    _glucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}\nglucose["P002"] = 105.1\nprint(glucose)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.3.**

    ```python
    glucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    ```

    A new patient `"P004"` has a glucose reading of `99.2`. Add them to the dictionary.
    Print the dictionary.
    """)
    return


@app.cell
def _():
    _glucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose = {"P001": 92.5, "P002": 110.3, "P003": 88.7}\nglucose["P004"] = 99.2\nprint(glucose)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.4.**

    ```python
    admission = {"mrn": "P001", "fever": True, "hypertension": True, "diabetes": False}
    ```

    The `"hypertension"` flag was incorrectly recorded for this patient. Delete it from
    the dictionary. Print the dictionary.
    """)
    return


@app.cell
def _():
    _admission = {"mrn": "P001", "fever": True, "hypertension": True, "diabetes": False}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nadmission = {"mrn": "P001", "fever": True, "hypertension": True, "diabetes": False}\ndel admission["hypertension"]\nprint(admission)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.5.**

    ```python
    supplies = {"syringes": 50, "bandages": 30, "gloves": 100}
    ```

    Write code that:
    1. Prints the current number of bandages.
    2. Reduces the number of bandages by 5 (five were used during rounds).
    3. Prints the updated number of bandages.
    """)
    return


@app.cell
def _():
    _supplies = {"syringes": 50, "bandages": 30, "gloves": 100}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nsupplies = {"syringes": 50, "bandages": 30, "gloves": 100}\nprint(supplies["bandages"])\nsupplies["bandages"] = supplies["bandages"] - 5\nprint(supplies["bandages"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.6.**

    Start with an empty dictionary called `field_lengths`. For each measurement name in the
    list below, add an entry to the dictionary mapping the name to its character length
    (use the built-in `len()` function).

    ```python
    measurements = ["temperature", "heart_rate", "glucose", "blood_pressure", "weight"]
    ```

    Print the final dictionary.
    """)
    return


@app.cell
def _():
    _measurements = ["temperature", "heart_rate", "glucose", "blood_pressure", "weight"]
    _field_lengths = {}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nmeasurements = ["temperature", "heart_rate", "glucose", "blood_pressure", "weight"]\nfield_lengths = {}\nfor name in measurements:\n    field_lengths[name] = len(name)\nprint(field_lengths)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.7.**

    ```python
    glucose = {"P001": 78, "P002": 55, "P003": 92, "P004": 61}
    ```

    Write code that loops over the list of patient IDs below. For each ID, if the ID is in
    `glucose` and the reading is below `70` (hypoglycemic threshold), update the reading
    to `70` (minimum safe recording).

    ```python
    to_review = ["P002", "P003", "P004", "P005"]
    ```

    Print the final `glucose` dictionary.

    *Note: Accessing a key that is not in the dictionary raises a `KeyError`. For now, use
    an `if` statement with the `in` operator (covered in depth in the next section) to guard
    the access: `if pid in glucose:`*
    """)
    return


@app.cell
def _():
    _glucose = {"P001": 78, "P002": 55, "P003": 92, "P004": 61}
    _to_review = ["P002", "P003", "P004", "P005"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose = {"P001": 78, "P002": 55, "P003": 92, "P004": 61}\nto_review = ["P002", "P003", "P004", "P005"]\nfor pid in to_review:\n    if pid in glucose:\n        if glucose[pid] < 70:\n            glucose[pid] = 70\nprint(glucose)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 3: Dictionary Methods

    ### Useful Tools for Working with Dictionaries

    Python dictionaries come with several built-in methods and operators.

    **Checking length:**
    ```python
    len(d)          # number of key-value pairs
    ```

    **Checking if a key exists:**
    ```python
    "P001" in heart_rates        # True if "P001" is a key
    "P999" not in heart_rates    # True if "P999" is not a key
    ```

    **Safe access with a default:**
    ```python
    heart_rates.get("P001")          # returns the value, or None if key missing
    heart_rates.get("P999", 0)       # returns 0 if "P999" is not in the dict
    ```
    Unlike `d[key]`, `.get()` does **not** raise a `KeyError`.

    **Viewing keys, values, and pairs:**
    ```python
    d.keys()     # a view of all keys
    d.values()   # a view of all values
    d.items()    # a view of all (key, value) pairs
    ```
    These are often used in `for` loops, which you will practice in the next section. You
    can also wrap them in `list()` to get a plain list: `list(d.keys())`.

    **Removing a key and getting its value:**
    ```python
    d.pop("P001")          # removes "P001" and returns its value
    d.pop("P999", None)    # returns None if key missing, no error
    ```

    **Updating with another dictionary:**
    ```python
    d.update({"P004": 77, "P005": 90})   # adds or overwrites those keys
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.1.**

    ```python
    vitals = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120, "oxygen_sat": 98, "weight": 165}
    ```

    Print the number of vital signs recorded.
    """)
    return


@app.cell
def _():
    _vitals = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120, "oxygen_sat": 98, "weight": 165}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nvitals = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120, "oxygen_sat": 98, "weight": 165}\nprint(len(vitals))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.2.**

    ```python
    chart = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120}
    ```

    A nurse asks whether `"glucose"` has been recorded in the chart. Write code that prints
    `"Yes, glucose is recorded"` or `"Sorry, glucose is missing"` based on whether the key
    exists.
    """)
    return


@app.cell
def _():
    _chart = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nchart = {"temperature": 98.6, "heart_rate": 72, "blood_pressure": 120}\nif "glucose" in chart:\n    print("Yes, glucose is recorded")\nelse:\n    print("Sorry, glucose is missing")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.3.**

    ```python
    settings = {"alarm_threshold": 100, "sample_interval": 30}
    ```

    Use `.get()` to retrieve the value for `"battery_level"`. Since `"battery_level"` is
    not in the dictionary, provide a default of `100`. Print the result.
    """)
    return


@app.cell
def _():
    _settings = {"alarm_threshold": 100, "sample_interval": 30}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nsettings = {"alarm_threshold": 100, "sample_interval": 30}\nprint(settings.get("battery_level", 100))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.4.**

    ```python
    settings = {"alarm_threshold": 100, "sample_interval": 30}
    ```

    Use `.get()` to retrieve `"alarm_threshold"`. If the returned value is greater than
    `120` (hypertension alert level), print `"Threshold is set too high"`. Otherwise, print
    `"Threshold is acceptable"`.
    """)
    return


@app.cell
def _():
    _settings = {"alarm_threshold": 100, "sample_interval": 30}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nsettings = {"alarm_threshold": 100, "sample_interval": 30}\nthreshold = settings.get("alarm_threshold")\nif threshold > 120:\n    print("Threshold is set too high")\nelse:\n    print("Threshold is acceptable")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.5.**

    ```python
    lab_results = {"glucose": 110.3, "hba1c": 6.8, "cholesterol": 195, "creatinine": 0.9}
    ```

    Print a list of all the tests recorded in `lab_results`. Then print a list of all the
    values.
    """)
    return


@app.cell
def _():
    _lab_results = {"glucose": 110.3, "hba1c": 6.8, "cholesterol": 195, "creatinine": 0.9}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nlab_results = {"glucose": 110.3, "hba1c": 6.8, "cholesterol": 195, "creatinine": 0.9}\nprint(list(lab_results.keys()))\nprint(list(lab_results.values()))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.6.**

    ```python
    chart = {"P001": 88, "P002": 73, "P003": 95}
    ```

    Patient `"P002"` has been discharged. Use `.pop()` to remove them from the chart and
    store their last recorded glucose in a variable called `discharged_glucose`. Print
    `discharged_glucose`, then print the updated chart.
    """)
    return


@app.cell
def _():
    _chart = {"P001": 88, "P002": 73, "P003": 95}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nchart = {"P001": 88, "P002": 73, "P003": 95}\ndischarged_glucose = chart.pop("P002")\nprint(discharged_glucose)\nprint(chart)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.7.**

    ```python
    patient = {"mrn": "P001", "name": "Alice"}
    ```

    Use `.update()` to add `"age": 45` and `"diagnosis": "hypertension"` to the patient
    record. Print the result.
    """)
    return


@app.cell
def _():
    _patient = {"mrn": "P001", "name": "Alice"}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatient = {"mrn": "P001", "name": "Alice"}\npatient.update({"age": 45, "diagnosis": "hypertension"})\nprint(patient)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.8.**

    ```python
    wbc_counts = {"P001": 7.2, "P002": 9.4, "P003": 11.8, "P004": 6.1}
    ```

    Write code that:
    1. Checks whether `"P005"` is in the dictionary. If not, print
       `"P005 has no WBC count recorded"`.
    2. Uses `.get()` to retrieve P005's WBC count with a default of `0.0`, and stores it
       in `p005_wbc`.
    3. Prints `p005_wbc`.
    """)
    return


@app.cell
def _():
    _wbc_counts = {"P001": 7.2, "P002": 9.4, "P003": 11.8, "P004": 6.1}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwbc_counts = {"P001": 7.2, "P002": 9.4, "P003": 11.8, "P004": 6.1}\nif "P005" not in wbc_counts:\n    print("P005 has no WBC count recorded")\np005_wbc = wbc_counts.get("P005", 0.0)\nprint(p005_wbc)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.9.**

    ```python
    baseline = {"heart_rate": 72, "blood_pressure": 120, "temperature": 98.6}
    new_vitals = {"blood_pressure": 135, "oxygen_sat": 97}
    ```

    Use `.update()` to apply `new_vitals` to `baseline`. Print the result. Notice which key
    changed and which was added.
    """)
    return


@app.cell
def _():
    _baseline = {"heart_rate": 72, "blood_pressure": 120, "temperature": 98.6}
    _new_vitals = {"blood_pressure": 135, "oxygen_sat": 97}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nbaseline = {"heart_rate": 72, "blood_pressure": 120, "temperature": 98.6}\nnew_vitals = {"blood_pressure": 135, "oxygen_sat": 97}\nbaseline.update(new_vitals)\nprint(baseline)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 4: Iterating Over Dictionaries

    ### Looping Through Keys, Values, and Pairs

    You can use a `for` loop to go through every entry in a dictionary.

    **Iterating over keys** (the default when you loop over a dictionary directly):
    ```python
    for pid in heart_rates:
        print(pid)
    ```

    **Iterating over values:**
    ```python
    for rate in heart_rates.values():
        print(rate)
    ```

    **Iterating over key-value pairs** with `.items()`:
    ```python
    for pid, rate in heart_rates.items():
        print(pid, "has heart rate", rate)
    ```
    `.items()` gives you both at once, unpacked into two variables.

    The order of iteration matches the order items were inserted (Python 3.7+).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.1.**

    ```python
    lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    ```

    Write a loop that prints each patient ID (just the keys, not the values).
    """)
    return


@app.cell
def _():
    _lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nlab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}\nfor pid in lab_panels:\n    print(pid)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.2.**

    ```python
    lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    ```

    Write a loop that prints each glucose reading (just the values).
    """)
    return


@app.cell
def _():
    _lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nlab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}\nfor reading in lab_panels.values():\n    print(reading)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.3.**

    ```python
    lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    ```

    Write a loop using `.items()` that prints each pair in the format:
    ```
    Patient P001: glucose = 92.5
    ```
    """)
    return


@app.cell
def _():
    _lab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nlab_panels = {"P001": 92.5, "P002": 110.3, "P003": 88.7}\nfor pid, glucose in lab_panels.items():\n    print("Patient " + pid + ": glucose =", glucose)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.4.**

    ```python
    daily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}
    ```

    Use a loop to compute the total number of admissions across all days. Print the total.
    """)
    return


@app.cell
def _():
    _daily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndaily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}\ntotal = 0\nfor count in daily_admissions.values():\n    total = total + count\nprint(total)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.5.**

    ```python
    daily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}
    ```

    Use a loop to find the day with the highest number of admissions. Print that day and its
    admission count.

    *Hint: Keep track of the best day and best count seen so far as you loop.*
    """)
    return


@app.cell
def _():
    _daily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndaily_admissions = {"Monday": 12, "Tuesday": 18, "Wednesday": 9, "Thursday": 15, "Friday": 21}\nbest_day = None\nbest_count = 0\nfor day, count in daily_admissions.items():\n    if count > best_count:\n        best_day = day\n        best_count = count\nprint(best_day, best_count)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.6.**

    ```python
    glucose_readings = {"P001": 92.5, "P002": 145.2, "P003": 88.7, "P004": 110.3}
    ```

    Write a loop that prints only the patients whose glucose exceeds `100.0` mg/dL
    (hyperglycemic), in the format:
    ```
    P002: 145.2 mg/dL
    ```
    """)
    return


@app.cell
def _():
    _glucose_readings = {"P001": 92.5, "P002": 145.2, "P003": 88.7, "P004": 110.3}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose_readings = {"P001": 92.5, "P002": 145.2, "P003": 88.7, "P004": 110.3}\nfor pid, reading in glucose_readings.items():\n    if reading > 100.0:\n        print(pid + ": " + str(reading) + " mg/dL")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.7.**

    ```python
    glucose_readings = {"P001": 62, "P002": 88, "P003": 132, "P004": 195, "P005": 108}
    ```

    Create a new dictionary called `glucose_flags` that maps each patient ID to a clinical
    flag string, using the following scale:
    - 180 and above -> `"critical"`
    - 126-179 -> `"high"`
    - 100-125 -> `"elevated"`
    - 70-99 -> `"normal"`
    - Below 70 -> `"low"`

    Build `glucose_flags` by looping over `glucose_readings`. Print the result.
    """)
    return


@app.cell
def _():
    _glucose_readings = {"P001": 62, "P002": 88, "P003": 132, "P004": 195, "P005": 108}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose_readings = {"P001": 62, "P002": 88, "P003": 132, "P004": 195, "P005": 108}\nglucose_flags = {}\nfor pid, g in glucose_readings.items():\n    if g >= 180:\n        glucose_flags[pid] = "critical"\n    elif g >= 126:\n        glucose_flags[pid] = "high"\n    elif g >= 100:\n        glucose_flags[pid] = "elevated"\n    elif g >= 70:\n        glucose_flags[pid] = "normal"\n    else:\n        glucose_flags[pid] = "low"\nprint(glucose_flags)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.8.**

    ```python
    diagnoses = ["hypertension", "diabetes", "hypertension", "asthma", "hypertension", "diabetes"]
    ```

    Create a dictionary called `diagnosis_counts` that maps each unique diagnosis to how many
    times it appears in `diagnoses`. Start with an empty dictionary and build it using a loop.

    *Hint: Use `.get()` with a default value to handle the first time you see a diagnosis.*
    """)
    return


@app.cell
def _():
    _diagnoses = ["hypertension", "diabetes", "hypertension", "asthma", "hypertension", "diabetes"]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndiagnoses = ["hypertension", "diabetes", "hypertension", "asthma", "hypertension", "diabetes"]\ndiagnosis_counts = {}\nfor d in diagnoses:\n    diagnosis_counts[d] = diagnosis_counts.get(d, 0) + 1\nprint(diagnosis_counts)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.9.**

    ```python
    heart_rates = {
        "Monday": 68, "Tuesday": 72, "Wednesday": 75,
        "Thursday": 71, "Friday": 69, "Saturday": 73, "Sunday": 70
    }
    ```

    Compute and print the average heart rate for the week. Use a loop (do not hardcode the
    number of days).
    """)
    return


@app.cell
def _():
    _heart_rates = {
        "Monday": 68, "Tuesday": 72, "Wednesday": 75,
        "Thursday": 71, "Friday": 69, "Saturday": 73, "Sunday": 70
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nheart_rates = {\n    "Monday": 68, "Tuesday": 72, "Wednesday": 75,\n    "Thursday": 71, "Friday": 69, "Saturday": 73, "Sunday": 70\n}\ntotal = 0\nfor rate in heart_rates.values():\n    total = total + rate\nprint(round(total / len(heart_rates), 2))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 5: Nested Dictionaries

    ### Dictionaries Inside Dictionaries

    A dictionary's values can themselves be dictionaries. This lets you represent structured,
    layered data such as a patient record with multiple lab panels:

    ```python
    patient = {
        "mrn": "P001",
        "labs": {
            "glucose": 92.5,
            "wbc": 7.2
        }
    }
    ```

    To access a nested value, chain the bracket indexing:

    ```python
    patient["labs"]["glucose"]    # 92.5
    ```

    To update a nested value:

    ```python
    patient["labs"]["wbc"] = 8.1
    ```

    You can loop over the outer dictionary and then access the inner dictionary inside the
    loop body.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.1.**

    ```python
    patients = {
        "P001": {"name": "Alice", "age": 34, "glucose": 92.5},
        "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},
        "P003": {"name": "Carol", "age": 45, "glucose": 88.7}
    }
    ```

    Print the name of patient `"P002"`.
    """)
    return


@app.cell
def _():
    _patients = {
        "P001": {"name": "Alice", "age": 34, "glucose": 92.5},
        "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},
        "P003": {"name": "Carol", "age": 45, "glucose": 88.7}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = {\n    "P001": {"name": "Alice", "age": 34, "glucose": 92.5},\n    "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},\n    "P003": {"name": "Carol", "age": 45, "glucose": 88.7}\n}\nprint(patients["P002"]["name"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.2.**

    ```python
    patients = {
        "P001": {"name": "Alice", "age": 34, "glucose": 92.5},
        "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},
        "P003": {"name": "Carol", "age": 45, "glucose": 88.7}
    }
    ```

    Add a `"blood_pressure"` key to `"P001"` with the value `118`. Print the updated entry
    for `"P001"`.
    """)
    return


@app.cell
def _():
    _patients = {
        "P001": {"name": "Alice", "age": 34, "glucose": 92.5},
        "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},
        "P003": {"name": "Carol", "age": 45, "glucose": 88.7}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = {\n    "P001": {"name": "Alice", "age": 34, "glucose": 92.5},\n    "P002": {"name": "Bob",   "age": 67, "glucose": 145.2},\n    "P003": {"name": "Carol", "age": 45, "glucose": 88.7}\n}\npatients["P001"]["blood_pressure"] = 118\nprint(patients["P001"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.3.**

    ```python
    patients = {
        "Alice": {"glucose": 88,  "flagged": False},
        "Bob":   {"glucose": 155, "flagged": True},
        "Carol": {"glucose": 92,  "flagged": False}
    }
    ```

    Loop over `patients` and print each patient's name along with whether they are flagged,
    in the format:
    ```
    Alice: clear
    Bob: flagged
    Carol: clear
    ```
    """)
    return


@app.cell
def _():
    _patients = {
        "Alice": {"glucose": 88,  "flagged": False},
        "Bob":   {"glucose": 155, "flagged": True},
        "Carol": {"glucose": 92,  "flagged": False}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = {\n    "Alice": {"glucose": 88,  "flagged": False},\n    "Bob":   {"glucose": 155, "flagged": True},\n    "Carol": {"glucose": 92,  "flagged": False}\n}\nfor name, data in patients.items():\n    if data["flagged"]:\n        print(name + ": flagged")\n    else:\n        print(name + ": clear")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.4.**

    ```python
    wards = {
        "cardiology": {"beds": 20, "type": "specialty"},
        "oncology":   {"beds": 15, "type": "specialty"},
        "general":    {"beds": 40, "type": "general"},
        "pediatrics": {"beds": 25, "type": "general"}
    }
    ```

    Use a loop to compute the total number of beds across all wards. Print the total.
    """)
    return


@app.cell
def _():
    _wards = {
        "cardiology": {"beds": 20, "type": "specialty"},
        "oncology":   {"beds": 15, "type": "specialty"},
        "general":    {"beds": 40, "type": "general"},
        "pediatrics": {"beds": 25, "type": "general"}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwards = {\n    "cardiology": {"beds": 20, "type": "specialty"},\n    "oncology":   {"beds": 15, "type": "specialty"},\n    "general":    {"beds": 40, "type": "general"},\n    "pediatrics": {"beds": 25, "type": "general"}\n}\ntotal = 0\nfor ward_data in wards.values():\n    total = total + ward_data["beds"]\nprint(total)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.5.**

    ```python
    wards = {
        "cardiology": {"beds": 20, "type": "specialty"},
        "oncology":   {"beds": 15, "type": "specialty"},
        "general":    {"beds": 40, "type": "general"},
        "pediatrics": {"beds": 25, "type": "general"}
    }
    ```

    Print the names and bed counts of only the `"specialty"` wards.
    """)
    return


@app.cell
def _():
    _wards = {
        "cardiology": {"beds": 20, "type": "specialty"},
        "oncology":   {"beds": 15, "type": "specialty"},
        "general":    {"beds": 40, "type": "general"},
        "pediatrics": {"beds": 25, "type": "general"}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwards = {\n    "cardiology": {"beds": 20, "type": "specialty"},\n    "oncology":   {"beds": 15, "type": "specialty"},\n    "general":    {"beds": 40, "type": "general"},\n    "pediatrics": {"beds": 25, "type": "general"}\n}\nfor ward, data in wards.items():\n    if data["type"] == "specialty":\n        print(ward, data["beds"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.6.**

    ```python
    staff = {
        "S001": {"name": "Dana",  "role": "physician", "salary": 220000},
        "S002": {"name": "Felix", "role": "nurse",     "salary": 72000},
        "S003": {"name": "Gina",  "role": "physician", "salary": 210000},
        "S004": {"name": "Hank",  "role": "nurse",     "salary": 68000}
    }
    ```

    Write code that gives every `"physician"` a 5% salary increase. Update the values in
    place. Print the final `staff` dictionary.
    """)
    return


@app.cell
def _():
    _staff = {
        "S001": {"name": "Dana",  "role": "physician", "salary": 220000},
        "S002": {"name": "Felix", "role": "nurse",     "salary": 72000},
        "S003": {"name": "Gina",  "role": "physician", "salary": 210000},
        "S004": {"name": "Hank",  "role": "nurse",     "salary": 68000}
    }
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nstaff = {\n    "S001": {"name": "Dana",  "role": "physician", "salary": 220000},\n    "S002": {"name": "Felix", "role": "nurse",     "salary": 72000},\n    "S003": {"name": "Gina",  "role": "physician", "salary": 210000},\n    "S004": {"name": "Hank",  "role": "nurse",     "salary": 68000}\n}\nfor sid in staff:\n    if staff[sid]["role"] == "physician":\n        staff[sid]["salary"] = staff[sid]["salary"] * 1.05\nprint(staff)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.7.** Build a nested dictionary called `patient_records` from scratch. It
    should store data for three patients of your choosing. Each patient ID should map to an
    inner dictionary with keys `"glucose"`, `"blood_pressure"`, and `"heart_rate"`, each
    holding a numeric measurement.

    Then write a loop that prints each patient's ID and their average measurement across
    the three values.
    """)
    return


@app.cell
def _():
    _patient_records = None  # replace with your answer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatient_records = {\n    "P001": {"glucose": 92.5, "blood_pressure": 118, "heart_rate": 72},\n    "P002": {"glucose": 145.2, "blood_pressure": 148, "heart_rate": 88},\n    "P003": {"glucose": 88.7, "blood_pressure": 112, "heart_rate": 65}\n}\nfor pid, data in patient_records.items():\n    avg = (data["glucose"] + data["blood_pressure"] + data["heart_rate"]) / 3\n    print(pid, round(avg, 2))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 6: Lists of Dictionaries

    ### Collections of Records

    A very common pattern in medical data science is a **list of dictionaries**, where each
    dictionary represents one patient record (like a row in a table). All the dictionaries
    in the list typically have the same keys.

    ```python
    records = [
        {"mrn": "P001", "glucose": 92.5},
        {"mrn": "P002", "glucose": 145.2},
        {"mrn": "P003", "glucose": 88.7}
    ]
    ```

    You access a specific record by its list index, then use a key to get a field:

    ```python
    records[0]["mrn"]    # "P001"
    ```

    You loop over records the same way you loop over any list:

    ```python
    for r in records:
        print(r["mrn"], ":", r["glucose"])
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.1.**

    ```python
    patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    ```

    Print the name and glucose reading of the third patient (index 2).
    """)
    return


@app.cell
def _():
    _patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [\n    {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},\n    {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},\n    {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},\n    {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}\n]\nprint(patients[2]["name"], patients[2]["glucose"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.2.**

    ```python
    patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    ```

    Loop over `patients` and print the name of every patient who is currently admitted.
    """)
    return


@app.cell
def _():
    _patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [\n    {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},\n    {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},\n    {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},\n    {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}\n]\nfor p in patients:\n    if p["admitted"]:\n        print(p["name"])\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.3.**

    ```python
    patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    ```

    Compute and print the average glucose reading across all patients in the list.
    """)
    return


@app.cell
def _():
    _patients = [
        {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},
        {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},
        {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},
        {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [\n    {"mrn": "P001", "name": "Alice", "glucose": 92.5,  "admitted": True},\n    {"mrn": "P002", "name": "Bob",   "glucose": 145.2, "admitted": True},\n    {"mrn": "P003", "name": "Carol", "glucose": 88.7,  "admitted": False},\n    {"mrn": "P004", "name": "David", "glucose": 110.3, "admitted": True}\n]\ntotal = 0\nfor p in patients:\n    total = total + p["glucose"]\nprint(round(total / len(patients), 2))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.4.**

    ```python
    patients = [
        {"mrn": "P001", "name": "Alice", "heart_rate": 91},
        {"mrn": "P002", "name": "Bob",   "heart_rate": 74},
        {"mrn": "P003", "name": "Carol", "heart_rate": 108},
        {"mrn": "P004", "name": "David", "heart_rate": 63},
        {"mrn": "P005", "name": "Eve",   "heart_rate": 97}
    ]
    ```

    Find and print the name of the patient with the highest heart rate.
    """)
    return


@app.cell
def _():
    _patients = [
        {"mrn": "P001", "name": "Alice", "heart_rate": 91},
        {"mrn": "P002", "name": "Bob",   "heart_rate": 74},
        {"mrn": "P003", "name": "Carol", "heart_rate": 108},
        {"mrn": "P004", "name": "David", "heart_rate": 63},
        {"mrn": "P005", "name": "Eve",   "heart_rate": 97}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [\n    {"mrn": "P001", "name": "Alice", "heart_rate": 91},\n    {"mrn": "P002", "name": "Bob",   "heart_rate": 74},\n    {"mrn": "P003", "name": "Carol", "heart_rate": 108},\n    {"mrn": "P004", "name": "David", "heart_rate": 63},\n    {"mrn": "P005", "name": "Eve",   "heart_rate": 97}\n]\ntop_name = patients[0]["name"]\ntop_rate = patients[0]["heart_rate"]\nfor p in patients:\n    if p["heart_rate"] > top_rate:\n        top_rate = p["heart_rate"]\n        top_name = p["name"]\nprint(top_name)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.5.**

    ```python
    lab_results = [
        {"mrn": "P001", "glucose": 92.5,  "status": "normal"},
        {"mrn": "P002", "glucose": 145.2, "status": "high"},
        {"mrn": "P003", "glucose": 75.0,  "status": "normal"},
        {"mrn": "P004", "glucose": 188.3, "status": "high"},
        {"mrn": "P005", "glucose": 62.1,  "status": "low"}
    ]
    ```

    Compute the total glucose for patients with `"normal"` status and the total for patients
    with `"high"` status separately. Print both totals.
    """)
    return


@app.cell
def _():
    _lab_results = [
        {"mrn": "P001", "glucose": 92.5,  "status": "normal"},
        {"mrn": "P002", "glucose": 145.2, "status": "high"},
        {"mrn": "P003", "glucose": 75.0,  "status": "normal"},
        {"mrn": "P004", "glucose": 188.3, "status": "high"},
        {"mrn": "P005", "glucose": 62.1,  "status": "low"}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nlab_results = [\n    {"mrn": "P001", "glucose": 92.5,  "status": "normal"},\n    {"mrn": "P002", "glucose": 145.2, "status": "high"},\n    {"mrn": "P003", "glucose": 75.0,  "status": "normal"},\n    {"mrn": "P004", "glucose": 188.3, "status": "high"},\n    {"mrn": "P005", "glucose": 62.1,  "status": "low"}\n]\nnormal_total = 0\nhigh_total = 0\nfor r in lab_results:\n    if r["status"] == "normal":\n        normal_total = normal_total + r["glucose"]\n    elif r["status"] == "high":\n        high_total = high_total + r["glucose"]\nprint("Normal total:", normal_total)\nprint("High total:", high_total)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.6.**

    You have two separate lists:

    ```python
    mrns        = ["P001", "P002", "P003"]
    temperatures = [98.6, 101.2, 99.5]
    ```

    Build a list of dictionaries called `temp_records` where each dictionary has an `"mrn"`
    key and a `"temperature"` key, using the corresponding entries from the two lists. Print
    `temp_records`.

    *Hint: Use a `for` loop with `range(len(mrns))` to pair them up.*
    """)
    return


@app.cell
def _():
    _mrns = ["P001", "P002", "P003"]
    _temperatures = [98.6, 101.2, 99.5]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nmrns = ["P001", "P002", "P003"]\ntemperatures = [98.6, 101.2, 99.5]\ntemp_records = []\nfor i in range(len(mrns)):\n    temp_records.append({"mrn": mrns[i], "temperature": temperatures[i]})\nprint(temp_records)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.7.**

    ```python
    staff = [
        {"name": "Dana",  "department": "Cardiology", "salary": 220000},
        {"name": "Felix", "department": "Oncology",   "salary": 185000},
        {"name": "Gina",  "department": "Cardiology", "salary": 215000},
        {"name": "Hank",  "department": "Oncology",   "salary": 190000},
        {"name": "Iris",  "department": "Cardiology", "salary": 230000}
    ]
    ```

    Build a dictionary called `dept_totals` that maps each department name to the total
    salary of all staff in that department. Print `dept_totals`.

    *Hint: Use `.get()` with a default of `0` to handle a department you haven't seen yet.*
    """)
    return


@app.cell
def _():
    _staff = [
        {"name": "Dana",  "department": "Cardiology", "salary": 220000},
        {"name": "Felix", "department": "Oncology",   "salary": 185000},
        {"name": "Gina",  "department": "Cardiology", "salary": 215000},
        {"name": "Hank",  "department": "Oncology",   "salary": 190000},
        {"name": "Iris",  "department": "Cardiology", "salary": 230000}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nstaff = [\n    {"name": "Dana",  "department": "Cardiology", "salary": 220000},\n    {"name": "Felix", "department": "Oncology",   "salary": 185000},\n    {"name": "Gina",  "department": "Cardiology", "salary": 215000},\n    {"name": "Hank",  "department": "Oncology",   "salary": 190000},\n    {"name": "Iris",  "department": "Cardiology", "salary": 230000}\n]\ndept_totals = {}\nfor s in staff:\n    dept = s["department"]\n    dept_totals[dept] = dept_totals.get(dept, 0) + s["salary"]\nprint(dept_totals)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.8.**

    ```python
    staff = [
        {"name": "Dana",  "department": "Cardiology", "salary": 220000},
        {"name": "Felix", "department": "Oncology",   "salary": 185000},
        {"name": "Gina",  "department": "Cardiology", "salary": 215000},
        {"name": "Hank",  "department": "Oncology",   "salary": 190000},
        {"name": "Iris",  "department": "Cardiology", "salary": 230000}
    ]
    ```

    Build a dictionary called `dept_counts` that maps each department name to the number of
    staff in it. Then compute and print the average salary per department.
    """)
    return


@app.cell
def _():
    _staff = [
        {"name": "Dana",  "department": "Cardiology", "salary": 220000},
        {"name": "Felix", "department": "Oncology",   "salary": 185000},
        {"name": "Gina",  "department": "Cardiology", "salary": 215000},
        {"name": "Hank",  "department": "Oncology",   "salary": 190000},
        {"name": "Iris",  "department": "Cardiology", "salary": 230000}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nstaff = [\n    {"name": "Dana",  "department": "Cardiology", "salary": 220000},\n    {"name": "Felix", "department": "Oncology",   "salary": 185000},\n    {"name": "Gina",  "department": "Cardiology", "salary": 215000},\n    {"name": "Hank",  "department": "Oncology",   "salary": 190000},\n    {"name": "Iris",  "department": "Cardiology", "salary": 230000}\n]\ndept_totals = {}\ndept_counts = {}\nfor s in staff:\n    dept = s["department"]\n    dept_totals[dept] = dept_totals.get(dept, 0) + s["salary"]\n    dept_counts[dept] = dept_counts.get(dept, 0) + 1\nfor dept in dept_counts:\n    print(dept, round(dept_totals[dept] / dept_counts[dept], 2))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.9.**

    ```python
    patients = [
        {"mrn": "P001", "name": "Alice", "condition": "hypertension", "severity": 3},
        {"mrn": "P002", "name": "Bob",   "condition": "diabetes",     "severity": 4},
        {"mrn": "P003", "name": "Carol", "condition": "hypertension", "severity": 2},
        {"mrn": "P004", "name": "David", "condition": "asthma",       "severity": 3},
        {"mrn": "P005", "name": "Eve",   "condition": "hypertension", "severity": 5}
    ]
    ```

    Write code that:
    1. Prints the names of all patients with `"hypertension"`.
    2. Finds and prints the name of the patient with the highest severity score overall.
    """)
    return


@app.cell
def _():
    _patients = [
        {"mrn": "P001", "name": "Alice", "condition": "hypertension", "severity": 3},
        {"mrn": "P002", "name": "Bob",   "condition": "diabetes",     "severity": 4},
        {"mrn": "P003", "name": "Carol", "condition": "hypertension", "severity": 2},
        {"mrn": "P004", "name": "David", "condition": "asthma",       "severity": 3},
        {"mrn": "P005", "name": "Eve",   "condition": "hypertension", "severity": 5}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\npatients = [\n    {"mrn": "P001", "name": "Alice", "condition": "hypertension", "severity": 3},\n    {"mrn": "P002", "name": "Bob",   "condition": "diabetes",     "severity": 4},\n    {"mrn": "P003", "name": "Carol", "condition": "hypertension", "severity": 2},\n    {"mrn": "P004", "name": "David", "condition": "asthma",       "severity": 3},\n    {"mrn": "P005", "name": "Eve",   "condition": "hypertension", "severity": 5}\n]\nfor p in patients:\n    if p["condition"] == "hypertension":\n        print(p["name"])\ntop_name = patients[0]["name"]\ntop_sev = patients[0]["severity"]\nfor p in patients:\n    if p["severity"] > top_sev:\n        top_sev = p["severity"]\n        top_name = p["name"]\nprint(top_name)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.10.** *(Challenge)*

    ```python
    records = [
        {"mrn": "P001", "labs": {"glucose": 90.0, "wbc": 7.0, "creatinine": 0.9}},
        {"mrn": "P002", "labs": {"glucose": 140.0, "wbc": 9.5, "creatinine": 1.2}},
        {"mrn": "P003", "labs": {"glucose": 85.0,  "wbc": 6.5, "creatinine": 0.8}},
        {"mrn": "P004", "labs": {"glucose": 109.0, "wbc": 8.0, "creatinine": 1.1}}
    ]
    ```

    Each record is a patient's lab results for three tests.

    Write code that computes the average value for each lab test across all patients. Print
    the results in the format:
    ```
    glucose: 106.0
    wbc: 7.75
    creatinine: 1.0
    ```

    *Hint: This combines lists of dictionaries (Section 6) with nested dictionaries
    (Section 5). Loop over the records, then loop over each patient's labs to accumulate
    totals per test.*
    """)
    return


@app.cell
def _():
    _records = [
        {"mrn": "P001", "labs": {"glucose": 90.0, "wbc": 7.0, "creatinine": 0.9}},
        {"mrn": "P002", "labs": {"glucose": 140.0, "wbc": 9.5, "creatinine": 1.2}},
        {"mrn": "P003", "labs": {"glucose": 85.0,  "wbc": 6.5, "creatinine": 0.8}},
        {"mrn": "P004", "labs": {"glucose": 109.0, "wbc": 8.0, "creatinine": 1.1}}
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nrecords = [\n    {"mrn": "P001", "labs": {"glucose": 90.0, "wbc": 7.0, "creatinine": 0.9}},\n    {"mrn": "P002", "labs": {"glucose": 140.0, "wbc": 9.5, "creatinine": 1.2}},\n    {"mrn": "P003", "labs": {"glucose": 85.0,  "wbc": 6.5, "creatinine": 0.8}},\n    {"mrn": "P004", "labs": {"glucose": 109.0, "wbc": 8.0, "creatinine": 1.1}}\n]\ntotals = {}\nfor r in records:\n    for test, val in r["labs"].items():\n        totals[test] = totals.get(test, 0) + val\nfor test, total in totals.items():\n    print(test + ": " + str(round(total / len(records), 2)))\n```\n"""})
    return


if __name__ == "__main__":
    app.run()
