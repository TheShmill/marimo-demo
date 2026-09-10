# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///
import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Functions: Practice Problems

    In medicine and data science, we constantly repeat the same kinds of calculations: converting
    units, checking whether a lab value is abnormal, computing a patient's BMI, or categorizing a
    blood pressure reading. Without functions, we would have to copy and paste the same code every
    time we needed it, and a copy-pasted mistake in a clinical formula could affect every patient.
    Functions let us write a calculation once, give it a name, test it carefully, and then reuse it
    confidently throughout our code. They are the basic unit of reliable, readable medical software.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 1: Syntax: Defining a Function

    A function is defined with the `def` keyword, followed by the function name, parentheses, and
    a colon. The body is indented. Until you add a `return` statement (covered in Section 3), the
    function runs its body and returns `None`.

    ```python
    def greet_patient(name):
        print("Hello, " + name + ". Welcome to the clinic.")

    greet_patient("Maria")
    # Hello, Maria. Welcome to the clinic.
    ```

    A function is only *defined* when Python reaches the `def` block. It does not run until you
    *call* it.

    ```python
    def print_separator():
        print("--------------------")

    print_separator()
    print_separator()
    # --------------------
    # --------------------
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Define a function called `print_header` that prints the following two lines exactly:

    ```
    === Patient Record ===
    ======================
    ```

    Expected output:
    ```
    === Patient Record ===
    ======================
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_header():\n    print("=== Patient Record ===")\n    print("======================")\n\nprint_header()\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Define a function called `print_vitals_label` that prints the following line exactly:

    ```
    --- Vitals ---
    ```

    Call it three times in a row.

    Expected output:
    ```
    --- Vitals ---
    --- Vitals ---
    --- Vitals ---
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_vitals_label():\n    print("--- Vitals ---")\n\nprint_vitals_label()\nprint_vitals_label()\nprint_vitals_label()\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** The code below has a syntax error. Fix it so it runs correctly.

    ```python
    def announce_patient
        print("Next patient, please approach the desk.")

    announce_patient()
    ```

    Expected output:
    ```
    Next patient, please approach the desk.
    ```
    """)
    return


@app.cell
def _():
    # Fix the syntax error and write the corrected function here
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef announce_patient():\n    print("Next patient, please approach the desk.")\n\nannounce_patient()\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Define a function called `print_record_footer` that prints:

    ```
    --- End of Record ---
    ```

    Then write a short program that prints a header (using `print_header` from problem 1), a
    vitals label (using `print_vitals_label` from problem 2), and a footer (using
    `print_record_footer`).

    Expected output:
    ```
    === Patient Record ===
    ======================
    --- Vitals ---
    --- End of Record ---
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_header():\n    print("=== Patient Record ===")\n    print("======================")\n\ndef print_vitals_label():\n    print("--- Vitals ---")\n\ndef print_record_footer():\n    print("--- End of Record ---")\n\nprint_header()\nprint_vitals_label()\nprint_record_footer()\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 2: Parameters: Passing Information In

    Parameters let you give a function information to work with. You list them inside the
    parentheses in the `def` line. When you call the function, the values you pass are called
    *arguments* and they are bound to the parameter names for the duration of that call.

    ```python
    def print_patient_name(name):
        print("Patient: " + name)

    print_patient_name("James")
    print_patient_name("Anika")
    # Patient: James
    # Patient: Anika
    ```

    A function can accept more than one parameter:

    ```python
    def print_glucose_reading(patient_name, glucose):
        print(patient_name + " - glucose: " + str(glucose) + " mg/dL")

    print_glucose_reading("James", 105)
    print_glucose_reading("Anika", 243)
    # James - glucose: 105 mg/dL
    # Anika - glucose: 243 mg/dL
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Define a function called `print_heart_rate` that takes one parameter, `bpm`,
    and prints:

    ```
    Heart rate: <bpm> bpm
    ```

    Call it with the value `72`.

    Expected output:
    ```
    Heart rate: 72 bpm
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_heart_rate(bpm):\n    print("Heart rate: " + str(bpm) + " bpm")\n\nprint_heart_rate(72)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Define a function called `print_patient_age` that takes two parameters,
    `name` and `age`, and prints:

    ```
    <name> is <age> years old.
    ```

    Call it with `"Liu Yang"` and `34`.

    Expected output:
    ```
    Liu Yang is 34 years old.
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_patient_age(name, age):\n    print(name + " is " + str(age) + " years old.")\n\nprint_patient_age("Liu Yang", 34)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Define a function called `print_blood_pressure` that takes two parameters,
    `systolic` and `diastolic`, and prints:

    ```
    Blood pressure: <systolic>/<diastolic> mmHg
    ```

    Call it twice: once with `120` and `80`, and once with `145` and `95`.

    Expected output:
    ```
    Blood pressure: 120/80 mmHg
    Blood pressure: 145/95 mmHg
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_blood_pressure(systolic, diastolic):\n    print("Blood pressure: " + str(systolic) + "/" + str(diastolic) + " mmHg")\n\nprint_blood_pressure(120, 80)\nprint_blood_pressure(145, 95)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Define a function called `print_lab_result` that takes three parameters:
    `patient_name`, `test_name`, and `value`. It should print:

    ```
    <patient_name> | <test_name>: <value>
    ```

    Call it for each row in the following table:

    | Patient   | Test        | Value |
    |-----------|-------------|-------|
    | Ortega    | WBC         | 7.2   |
    | Chen      | Hemoglobin  | 11.4  |
    | Patel     | Creatinine  | 1.1   |

    Expected output:
    ```
    Ortega | WBC: 7.2
    Chen | Hemoglobin: 11.4
    Patel | Creatinine: 1.1
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef print_lab_result(patient_name, test_name, value):\n    print(patient_name + " | " + test_name + ": " + str(value))\n\nprint_lab_result("Ortega", "WBC", 7.2)\nprint_lab_result("Chen", "Hemoglobin", 11.4)\nprint_lab_result("Patel", "Creatinine", 1.1)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** *(Challenge)* The list below contains patient records as dictionaries. Define a
    function called `print_patient_summary` that takes a single dictionary with keys `"name"`,
    `"age"`, `"heart_rate"`, and `"glucose"`, and prints a two-line summary:

    ```
    Patient: <name>, Age: <age>
    HR: <heart_rate> bpm | Glucose: <glucose> mg/dL
    ```

    Then use a for loop to call it for every record.

    Expected output:
    ```
    Patient: Maria Santos, Age: 45
    HR: 78 bpm | Glucose: 102 mg/dL
    Patient: David Okonkwo, Age: 61
    HR: 92 bpm | Glucose: 189 mg/dL
    Patient: Priya Nair, Age: 29
    HR: 65 bpm | Glucose: 94 mg/dL
    ```
    """)
    return


@app.cell
def _():
    _records = [
        {"name": "Maria Santos",  "age": 45, "heart_rate": 78,  "glucose": 102},
        {"name": "David Okonkwo", "age": 61, "heart_rate": 92,  "glucose": 189},
        {"name": "Priya Nair",    "age": 29, "heart_rate": 65,  "glucose": 94},
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nrecords = [\n    {"name": "Maria Santos",  "age": 45, "heart_rate": 78,  "glucose": 102},\n    {"name": "David Okonkwo", "age": 61, "heart_rate": 92,  "glucose": 189},\n    {"name": "Priya Nair",    "age": 29, "heart_rate": 65,  "glucose": 94},\n]\n\ndef print_patient_summary(record):\n    print("Patient: " + record["name"] + ", Age: " + str(record["age"]))\n    print("HR: " + str(record["heart_rate"]) + " bpm | Glucose: " + str(record["glucose"]) + " mg/dL")\n\nfor record in records:\n    print_patient_summary(record)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 3: Return Values

    So far our functions have only *printed* things. More useful functions *compute* a result and
    hand it back with `return`. The caller can then store that result in a variable or use it in
    an expression.

    ```python
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    temp_f = celsius_to_fahrenheit(37.0)
    print(temp_f)   # 98.6
    ```

    A function stops as soon as it hits a `return` statement:

    ```python
    def classify_heart_rate(bpm):
        if bpm < 60:
            return "bradycardia"
        if bpm > 100:
            return "tachycardia"
        return "normal"

    print(classify_heart_rate(55))   # bradycardia
    print(classify_heart_rate(88))   # normal
    print(classify_heart_rate(115))  # tachycardia
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Define a function called `double_dose` that takes one parameter, `dose_mg`,
    and returns twice that value.

    Expected output:
    ```
    50
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef double_dose(dose_mg):\n    return dose_mg * 2\n\nprint(double_dose(25))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Define a function called `fahrenheit_to_celsius` that converts a Fahrenheit
    temperature to Celsius using the formula `(f - 32) * 5 / 9`. Return the result.

    Call it with `98.6` and print the result.

    Expected output:
    ```
    37.0
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef fahrenheit_to_celsius(f):\n    return (f - 32) * 5 / 9\n\nprint(fahrenheit_to_celsius(98.6))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Define a function called `is_febrile` that takes a temperature in Celsius and
    returns `True` if it is 38.0 °C or above, and `False` otherwise.

    Call it with `37.2` and `38.5` and print both results.

    Expected output:
    ```
    False
    True
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef is_febrile(temp_celsius):\n    return temp_celsius >= 38.0\n\nprint(is_febrile(37.2))\nprint(is_febrile(38.5))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Define a function called `bmi` that takes `weight_kg` and `height_m` and
    returns the BMI using the formula `weight_kg / height_m ** 2`. Round the result to one
    decimal place using `round(value, 1)`.

    Call it with weight `70` kg and height `1.75` m and print the result.

    Expected output:
    ```
    22.9
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef bmi(weight_kg, height_m):\n    return round(weight_kg / height_m ** 2, 1)\n\nprint(bmi(70, 1.75))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** Define a function called `classify_glucose` that takes a fasting glucose
    reading in mg/dL and returns a string category:

    - Below 100: `"normal"`
    - 100–125 (inclusive): `"prediabetes"`
    - 126 or above: `"diabetes"`

    Call it with `88`, `112`, and `140` and print each result.

    Expected output:
    ```
    normal
    prediabetes
    diabetes
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef classify_glucose(glucose):\n    if glucose < 100:\n        return "normal"\n    elif glucose <= 125:\n        return "prediabetes"\n    else:\n        return "diabetes"\n\nprint(classify_glucose(88))\nprint(classify_glucose(112))\nprint(classify_glucose(140))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 6.** *(Challenge)* Define a function called `mean_glucose` that takes a list of
    glucose readings and returns their mean. Do not use any built-in functions except `len`.
    Return `0` if the list is empty.

    ```python
    readings = [98, 143, 112, 201, 88, 130]
    ```

    Expected output:
    ```
    128.67
    ```
    """)
    return


@app.cell
def _():
    _readings = [98, 143, 112, 201, 88, 130]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef mean_glucose(readings):\n    if len(readings) == 0:\n        return 0\n    total = 0\n    for r in readings:\n        total = total + r\n    return round(total / len(readings), 2)\n\nreadings = [98, 143, 112, 201, 88, 130]\nprint(mean_glucose(readings))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 4: Optional Parameters

    Sometimes a parameter has a sensible default value that will be right most of the time. You
    can make a parameter *optional* by giving it a default value in the `def` line. If the caller
    does not supply that argument, the default is used.

    ```python
    def print_temperature(temp, unit="C"):
        print(str(temp) + " °" + unit)

    print_temperature(37.2)         # 37.2 °C
    print_temperature(98.6, "F")    # 98.6 °F
    ```

    Required parameters (those without defaults) must come *before* optional ones in the `def`
    line.

    ```python
    def flag_abnormal(value, low, high, label="value"):
        if value < low or value > high:
            print("Abnormal " + label + ": " + str(value))
        else:
            print("Normal " + label + ": " + str(value))

    flag_abnormal(7.2, 4.5, 11.0, "WBC")
    flag_abnormal(37.2, 36.1, 37.9)
    # Normal WBC: 7.2
    # Normal value: 37.2
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Define a function called `format_glucose` that takes `glucose` and an optional
    parameter `unit` with default `"mg/dL"`. It should return the string `"<glucose> <unit>"`.

    Expected output:
    ```
    105 mg/dL
    5.8 mmol/L
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef format_glucose(glucose, unit="mg/dL"):\n    return str(glucose) + " " + unit\n\nprint(format_glucose(105))\nprint(format_glucose(5.8, "mmol/L"))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Define a function called `patient_greeting` that takes `name` and an optional
    parameter `title` with default `"Patient"`. It should return the string
    `"Hello, <title> <name>."`.

    Expected output:
    ```
    Hello, Patient Rivera.
    Hello, Dr. Osei.
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef patient_greeting(name, title="Patient"):\n    return "Hello, " + title + " " + name + "."\n\nprint(patient_greeting("Rivera"))\nprint(patient_greeting("Osei", "Dr."))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Define a function called `describe_bp` that takes `systolic`, `diastolic`,
    and an optional parameter `patient_name` with default `"Unknown"`. It should print:

    ```
    <patient_name> - BP: <systolic>/<diastolic> mmHg
    ```

    Call it once without a name and once with `"Torres"`.

    Expected output:
    ```
    Unknown - BP: 118/76 mmHg
    Torres - BP: 152/98 mmHg
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef describe_bp(systolic, diastolic, patient_name="Unknown"):\n    print(patient_name + " - BP: " + str(systolic) + "/" + str(diastolic) + " mmHg")\n\ndescribe_bp(118, 76)\ndescribe_bp(152, 98, "Torres")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Define a function called `classify_bmi` that takes `weight_kg`, `height_m`,
    and an optional `round_to` parameter with default `1`. It should compute the BMI (same
    formula as Section 3 problem 4), round it to `round_to` decimal places, and return the BMI
    value and a category string as a list `[bmi_value, category]`, where the categories are:

    - Below 18.5: `"underweight"`
    - 18.5–24.9: `"normal"`
    - 25.0–29.9: `"overweight"`
    - 30.0 or above: `"obese"`

    Expected output:
    ```
    [22.9, 'normal']
    [22.86, 'normal']
    [30.9, 'obese']
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef classify_bmi(weight_kg, height_m, round_to=1):\n    value = round(weight_kg / height_m ** 2, round_to)\n    if value < 18.5:\n        category = "underweight"\n    elif value < 25.0:\n        category = "normal"\n    elif value < 30.0:\n        category = "overweight"\n    else:\n        category = "obese"\n    return [value, category]\n\nprint(classify_bmi(70, 1.75))\nprint(classify_bmi(70, 1.75, 2))\nprint(classify_bmi(90, 1.71))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** *(Challenge)* Define a function called `flag_vitals` that takes a dictionary
    of vitals and an optional `verbose` parameter with default `False`. The vitals dictionary
    will always contain `"heart_rate"`, `"systolic"`, and `"temp_c"`. Normal ranges are:

    - Heart rate: 60–100 bpm
    - Systolic BP: 90–140 mmHg
    - Temperature: 36.1–37.9 °C

    When `verbose` is `False`, print only the abnormal vitals, one per line in the format
    `"ABNORMAL <name>: <value>"`. When `verbose` is `True`, print *all* vitals, using `"OK"` or
    `"ABNORMAL"` as appropriate.

    Expected output when called as `flag_vitals(vitals)`:
    ```
    ABNORMAL heart_rate: 112
    ```

    Expected output when called as `flag_vitals(vitals, verbose=True)`:
    ```
    ABNORMAL heart_rate: 112
    OK systolic: 128
    OK temp_c: 37.2
    ```
    """)
    return


@app.cell
def _():
    _vitals = {"heart_rate": 112, "systolic": 128, "temp_c": 37.2}
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef flag_vitals(vitals, verbose=False):\n    ranges = {\n        "heart_rate": [60, 100],\n        "systolic": [90, 140],\n        "temp_c": [36.1, 37.9],\n    }\n    for name in ranges:\n        low = ranges[name][0]\n        high = ranges[name][1]\n        value = vitals[name]\n        if value < low or value > high:\n            status = "ABNORMAL"\n        else:\n            status = "OK"\n        if status == "ABNORMAL" or verbose:\n            print(status + " " + name + ": " + str(value))\n\nvitals = {"heart_rate": 112, "systolic": 128, "temp_c": 37.2}\nflag_vitals(vitals)\nprint()\nflag_vitals(vitals, verbose=True)\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 5: Keyword Arguments: Calling by Name

    When calling a function, you can supply arguments by name instead of by position. This is
    called using *keyword arguments*. It makes calls easier to read and lets you provide optional
    arguments in any order.

    ```python
    def record_vital(patient, measure, value, unit="\"):
        print(patient + " | " + measure + ": " + str(value) + " " + unit)

    # positional
    record_vital("Kim", "glucose", 118, "mg/dL")

    # keyword, same result
    record_vital(patient="Kim", measure="glucose", value=118, unit="mg/dL")

    # mix: positional for required args, keyword for optional
    record_vital("Kim", "glucose", 118, unit="mg/dL")
    ```

    You can also skip to a later optional argument by naming it, leaving earlier optional
    arguments at their defaults:

    ```python
    def describe_lab(test, value, unit="\", flag="\"):
        print(test + ": " + str(value) + " " + unit + " " + flag)

    describe_lab("WBC", 14.2, flag="HIGH")
    # WBC: 14.2  HIGH
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** The function below is already defined. Call it three ways: all positional,
    all keyword, and a mix (positional for `patient_id` and `temp`, keyword for `unit`).

    Expected output (same line printed three times):
    ```
    ID 1042: 38.1 °C
    ID 1042: 38.1 °C
    ID 1042: 38.1 °C
    ```
    """)
    return


@app.cell
def _():
    def log_temperature(patient_id, temp, unit="C"):
        print("ID " + str(patient_id) + ": " + str(temp) + " °" + unit)

    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef log_temperature(patient_id, temp, unit="C"):\n    print("ID " + str(patient_id) + ": " + str(temp) + " °" + unit)\n\nlog_temperature(1042, 38.1)\nlog_temperature(patient_id=1042, temp=38.1, unit="C")\nlog_temperature(1042, 38.1, unit="C")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** The function below accepts `systolic`, `diastolic`, `patient_name="Unknown"`,
    and `units="mmHg"`. Call it for each scenario listed using keyword arguments for every
    parameter.

    Scenarios:
    1. systolic=130, diastolic=85, patient_name="Gomez"
    2. systolic=118, diastolic=76 (no name, default units)
    3. systolic=155, diastolic=100, patient_name="Yıldız", units="mmHg"

    Expected output:
    ```
    Gomez: 130/85 mmHg
    Unknown: 118/76 mmHg
    Yıldız: 155/100 mmHg
    ```
    """)
    return


@app.cell
def _():
    def log_bp(systolic, diastolic, patient_name="Unknown", units="mmHg"):
        print(patient_name + ": " + str(systolic) + "/" + str(diastolic) + " " + units)

    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef log_bp(systolic, diastolic, patient_name="Unknown", units="mmHg"):\n    print(patient_name + ": " + str(systolic) + "/" + str(diastolic) + " " + units)\n\nlog_bp(systolic=130, diastolic=85, patient_name="Gomez")\nlog_bp(systolic=118, diastolic=76)\nlog_bp(systolic=155, diastolic=100, patient_name="Yıldız", units="mmHg")\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Define a function called `summarize_lab` with parameters `test`, `value`,
    `low`, `high`, `unit="\"`. It should return a string in the format:

    ```
    <test>: <value> <unit> [<status>]
    ```

    where `<status>` is `"NORMAL"` if `low <= value <= high`, otherwise `"ABNORMAL"`. If `unit`
    is the empty string, omit the trailing space before the bracket.

    Then call it for each test using keyword arguments:

    | test         | value | low  | high  | unit    |
    |--------------|-------|------|-------|---------|
    | "Glucose"    | 105   | 70   | 99    | "mg/dL" |
    | "Hemoglobin" | 13.2  | 12.0 | 17.5  | "g/dL"  |
    | "WBC"        | 11.8  | 4.5  | 11.0  | "K/µL"  |

    Expected output:
    ```
    Glucose: 105 mg/dL [ABNORMAL]
    Hemoglobin: 13.2 g/dL [NORMAL]
    WBC: 11.8 K/µL [ABNORMAL]
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef summarize_lab(test, value, low, high, unit=""):\n    status = "NORMAL" if low <= value <= high else "ABNORMAL"\n    if unit == "":\n        return test + ": " + str(value) + " [" + status + "]"\n    return test + ": " + str(value) + " " + unit + " [" + status + "]"\n\nprint(summarize_lab(test="Glucose",    value=105,  low=70,   high=99,   unit="mg/dL"))\nprint(summarize_lab(test="Hemoglobin", value=13.2, low=12.0, high=17.5, unit="g/dL"))\nprint(summarize_lab(test="WBC",        value=11.8, low=4.5,  high=11.0, unit="K/µL"))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** *(Challenge)* Define a function called `risk_score` with parameters `age`,
    `smoker=False`, `diabetic=False`, `hypertensive=False`. It computes a simple cardiovascular
    risk score as follows:

    - Start at 0
    - Add 1 for every 10 years of age (integer division)
    - Add 2 if `smoker` is `True`
    - Add 2 if `diabetic` is `True`
    - Add 1 if `hypertensive` is `True`

    Return the score.

    Call it for the three patients below using keyword arguments for all boolean parameters:

    | age | smoker | diabetic | hypertensive |
    |-----|--------|----------|--------------|
    | 55  | True   | False    | True         |
    | 42  | False  | True     | False        |
    | 67  | True   | True     | True         |

    Expected output:
    ```
    8
    6
    14
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\ndef risk_score(age, smoker=False, diabetic=False, hypertensive=False):\n    score = age // 10\n    if smoker:\n        score = score + 2\n    if diabetic:\n        score = score + 2\n    if hypertensive:\n        score = score + 1\n    return score\n\nprint(risk_score(55, smoker=True, hypertensive=True))\nprint(risk_score(42, diabetic=True))\nprint(risk_score(67, smoker=True, diabetic=True, hypertensive=True))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Section 6: Lambda Functions

    A *lambda* is a compact way to define a simple, one-expression function. Instead of `def`,
    you write:

    ```python
    variable = lambda parameter: expression
    ```

    The result of the expression is automatically returned. Lambda functions are most useful when
    you need a short, throwaway function and the full `def` syntax would be distracting.

    ```python
    to_fahrenheit = lambda c: c * 9 / 5 + 32

    print(to_fahrenheit(37.0))   # 98.6
    ```

    You call a lambda stored in a variable exactly the same way you call any other function:

    ```python
    flag_glucose = lambda g: "high" if g >= 126 else "normal"

    print(flag_glucose(98))    # normal
    print(flag_glucose(143))   # high
    ```

    A lambda can take multiple parameters, separated by commas:

    ```python
    pulse_pressure = lambda systolic, diastolic: systolic - diastolic

    print(pulse_pressure(120, 80))   # 40
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 1.** Write a lambda called `kg_to_lbs` that converts kilograms to pounds. One
    kilogram is approximately 2.205 pounds. Store it in a variable and call it with `70`.

    Expected output:
    ```
    154.35
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nkg_to_lbs = lambda kg: round(kg * 2.205, 2)\n\nprint(kg_to_lbs(70))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 2.** Write a lambda called `is_tachycardic` that takes a heart rate in bpm and
    returns `True` if it is above 100, otherwise `False`. Call it with `85` and `115`.

    Expected output:
    ```
    False
    True
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nis_tachycardic = lambda bpm: bpm > 100\n\nprint(is_tachycardic(85))\nprint(is_tachycardic(115))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 3.** Write a lambda called `mean_arterial_pressure` that computes MAP from systolic
    and diastolic blood pressure using the formula:

    ```
    MAP = diastolic + (systolic - diastolic) / 3
    ```

    Round to one decimal place. Call it with systolic `120` and diastolic `80`.

    Expected output:
    ```
    93.3
    ```
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nmean_arterial_pressure = lambda systolic, diastolic: round(diastolic + (systolic - diastolic) / 3, 1)\n\nprint(mean_arterial_pressure(120, 80))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 4.** Write a lambda called `wbc_status` that takes a WBC count in K/µL and returns:

    - `"low"` if below 4.5
    - `"normal"` if between 4.5 and 11.0 (inclusive)
    - `"high"` if above 11.0

    Call it with `3.1`, `7.8`, and `13.4`.

    Expected output:
    ```
    low
    normal
    high
    ```

    *Hint: you can chain ternary expressions: `A if cond1 else B if cond2 else C`.*
    """)
    return


@app.cell
def _():
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nwbc_status = lambda wbc: "low" if wbc < 4.5 else "high" if wbc > 11.0 else "normal"\n\nprint(wbc_status(3.1))\nprint(wbc_status(7.8))\nprint(wbc_status(13.4))\n```\n"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Problem 5.** *(Challenge)* You have a list of patient dictionaries. Each has `"name"`,
    `"glucose"`, and `"heart_rate"` keys. Write:

    - A lambda `glucose_label` that takes a glucose value and returns `"diabetic"` if ≥ 126,
      `"prediabetic"` if ≥ 100, otherwise `"normal"`.
    - A lambda `hr_label` that takes a heart rate and returns `"brady"` if < 60, `"tachy"` if
      > 100, otherwise `"normal"`.

    Then loop over the list below and, for each patient, print one line in the format:

    ```
    <name>: glucose=<glucose_label> hr=<hr_label>
    ```

    Expected output:
    ```
    Abara: glucose=normal hr=normal
    Lindqvist: glucose=diabetic hr=brady
    Oduya: glucose=prediabetic hr=tachy
    Reyes: glucose=diabetic hr=normal
    ```
    """)
    return


@app.cell
def _():
    _patients = [
        {"name": "Abara",     "glucose": 88,  "heart_rate": 72},
        {"name": "Lindqvist", "glucose": 130, "heart_rate": 55},
        {"name": "Oduya",     "glucose": 110, "heart_rate": 108},
        {"name": "Reyes",     "glucose": 140, "heart_rate": 88},
    ]
    # Your answer here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"💡 Show solution": """\n```python\nglucose_label = lambda g: "diabetic" if g >= 126 else "prediabetic" if g >= 100 else "normal"\nhr_label = lambda hr: "brady" if hr < 60 else "tachy" if hr > 100 else "normal"\n\npatients = [\n    {"name": "Abara",     "glucose": 88,  "heart_rate": 72},\n    {"name": "Lindqvist", "glucose": 130, "heart_rate": 55},\n    {"name": "Oduya",     "glucose": 110, "heart_rate": 108},\n    {"name": "Reyes",     "glucose": 140, "heart_rate": 88},\n]\n\nfor p in patients:\n    print(p["name"] + ": glucose=" + glucose_label(p["glucose"]) + " hr=" + hr_label(p["heart_rate"]))\n```\n"""})
    return


if __name__ == "__main__":
    app.run()
