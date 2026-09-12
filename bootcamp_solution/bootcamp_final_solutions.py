import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


# ── Imports ───────────────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _():
    from sklearn.linear_model import LinearRegression
    return (LinearRegression,)


@app.cell
def _():
    from sklearn.model_selection import train_test_split
    return (train_test_split,)


# ── Section 1: Variables & Input/Output ───────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 1: Variables & Input/Output
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Variables

    A **variable** is a named container for a value. You create one with the assignment operator `=`.

    ```python
    course_name = "Introduction to Computer Science"
    num_students = 28
    passing_grade = 70.0
    ```

    Variable names should be lowercase with underscores (`snake_case`). Choose names that describe what the value represents.

    Python figures out the type automatically:

    | Value | Type | Example |
    |-------|------|---------|
    | Whole number | `int` | `28` |
    | Decimal number | `float` | `70.0` |
    | Text | `str` | `"Introduction to Computer Science"` |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Printing Output

    `print()` displays values to the screen.

    ```python
    print("Welcome to class!")
    print(num_students)
    ```

    ### f-strings

    f-strings let you embed variables directly inside a string. Prefix the string with `f` and wrap variable names in `{}`.

    ```python
    student_name = "Alex"
    grade = 92.5

    print(f"Student: {student_name}")
    print(f"Grade: {grade}")
    ```

    Output:
    ```
    Student: Alex
    Grade: 92.5
    ```

    You can also do math or format values inside the `{}`:

    ```python
    print(f"Grade: {grade:.1f}%")   # one decimal place
    print(f"Points lost: {100 - grade}")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1

    A student named `"Jordan"` scored `87` out of `100` on an exam. Assign these values to `ex1_name`, `ex1_score`, and `ex1_total`, then print a formatted summary using an f-string.

    Example output:
    ```
    Jordan scored 87 out of 100.
    ```
    """)
    return


@app.cell
def _():
    ex1_name = "Jordan"
    ex1_score = 87
    ex1_total = 100
    print(f"{ex1_name} scored {ex1_score} out of {ex1_total}.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Getting Input

    `input()` pauses the program and waits for the user to type something. It always returns a **string**.

    ```python
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    ```

    If you need a number, convert it:

    ```python
    score = input("Enter your score: ")
    score = int(score)       # or float(score) for decimals
    ```

    Or in one line:

    ```python
    score = int(input("Enter your score: "))
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 2

    Ask the user for their name, their exam score, and the total possible points. Store them in `ex2_name`, `ex2_score`, and `ex2_total`. Calculate the percentage, store it in `ex2_percentage`, and print a formatted summary.

    Example output:
    ```
    Enter your name: Jordan
    Enter your exam score: 43
    Enter the total possible points: 50
    Jordan scored 43/50 (86.0%).
    ```
    """)
    return


@app.cell
def _():
    ex2_name = input("Enter your name: ")
    ex2_score = int(input("Enter your exam score: "))
    ex2_total = int(input("Enter the total possible points: "))
    ex2_percentage = ex2_score / ex2_total * 100
    print(f"{ex2_name} scored {ex2_score}/{ex2_total} ({ex2_percentage:.1f}%).")
    return


# ── Section 2: Functions ──────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 2: Functions

    Functions let you write logic once and call it many times -- the functions you define here will be called again in later sections.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Defining a Function

    A **function** is a reusable block of code that runs when you call it. You define one with `def`.

    ```python
    def greet():
        print("Welcome to class!")

    greet()  # call the function
    ```

    Everything indented under `def` is the function body. Nothing inside runs until you call it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Parameters and Arguments

    Functions can accept **parameters**: inputs that change what the function does.

    ```python
    def greet_student(name):
        print(f"Welcome, {name}!")

    greet_student("Alex")
    greet_student("Jordan")
    ```

    Output:
    ```
    Welcome, Alex!
    Welcome, Jordan!
    ```

    You can have multiple parameters:

    ```python
    def greet_student(name, course):
        print(f"Welcome, {name}! You're enrolled in {course}.")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Return Values

    Functions can **return** a value back to the caller using `return`.

    ```python
    def add(a, b):
        return a + b

    result = add(10, 5)
    print(result)  # 15
    ```

    A function that uses `return` gives back a value you can store in a variable or use in an expression. A function that only calls `print()` displays output but returns nothing useful.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 4

    Write a function called `calculate_percentage` that takes a `score` and a `total` and returns the percentage as a float.

    Example: `calculate_percentage(43, 50)` should return `86.0`.
    """)
    return


@app.cell
def _():
    def calculate_percentage(score, total):
        return score / total * 100
    return (calculate_percentage,)


@app.cell
def _(calculate_percentage):
    ex4_percentage = calculate_percentage(43, 50)
    print(f"43 out of 50 is {ex4_percentage:.1f}%")
    return (ex4_percentage,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Default Parameter Values

    Parameters can have default values, making them optional when calling the function.

    ```python
    def greet_student(name, course="this course"):
        print(f"Welcome, {name}! You're enrolled in {course}.")

    greet_student("Alex")                          # uses default
    greet_student("Jordan", "Data Science 101")   # overrides default
    ```

    Output:
    ```
    Welcome, Alex! You're enrolled in this course.
    Welcome, Jordan! You're enrolled in Data Science 101.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 5

    Write a function called `format_score` that takes a `score` and `total` and **returns** a formatted string like `"43/50 (86.0%)"`.

    Hint: call `calculate_percentage` inside your function to compute the percentage.
    """)
    return


@app.cell
def _(calculate_percentage):
    def format_score(score, total):
        percentage = calculate_percentage(score, total)
        return f"{score}/{total} ({percentage:.1f}%)"
    return (format_score,)


@app.cell
def _(format_score):
    ex5_formatted = format_score(43, 50)
    print(ex5_formatted)
    return (ex5_formatted,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 6

    Write a function called `summarize_student` that takes a student's `name`, `score`, and `total`, with a default `total` of `100`. It should return a single string summarizing the student's result, like `"Alex: 76/100 (76.0%)"`. Use `format_score` inside it.
    """)
    return


@app.cell
def _(format_score):
    def summarize_student(name, score, total=100):
        return f"{name}: {format_score(score, total)}"
    return (summarize_student,)


@app.cell
def _(format_score, summarize_student):
    ex6_summary_custom = summarize_student("Jordan", 43, 50)
    ex6_summary_default = summarize_student("Alex", 76)
    print(ex6_summary_custom)
    print(ex6_summary_default)
    return (ex6_summary_custom, ex6_summary_default)


# ── Section 3: Conditionals ───────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 3: Conditionals
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `if` Statement

    An `if` statement runs a block of code only when a condition is true.

    ```python
    score = 85

    if score >= 60:
        print("You passed!")
    ```

    The condition (`score >= 60`) evaluates to either `True` or `False`. The indented block only runs when it is `True`. If it is `False`, nothing happens.

    Common comparison operators:

    | Operator | Meaning |
    |----------|---------|
    | `==` | equal to |
    | `!=` | not equal to |
    | `>` | greater than |
    | `<` | less than |
    | `>=` | greater than or equal to |
    | `<=` | less than or equal to |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `else` Clause

    An `else` clause runs when the `if` condition is `False`.

    ```python
    score = 45

    if score >= 60:
        print("You passed!")
    else:
        print("You did not pass.")
    ```

    Exactly one of the two blocks will always run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 7

    Write a function called `passing_status(percentage)` that returns `"Passing"` if the
    percentage is 60 or above, and `"Failing"` otherwise.
    """)
    return


@app.cell
def _():
    def passing_status(percentage):
        if percentage >= 60:
            return "Passing"
        else:
            return "Failing"
    return (passing_status,)


@app.cell
def _(passing_status):
    ex7_status_passing = passing_status(85)
    ex7_status_failing = passing_status(42)
    print(ex7_status_passing)
    print(ex7_status_failing)
    return (ex7_status_passing, ex7_status_failing)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `elif` Clause

    `elif` (short for "else if") lets you check multiple conditions in sequence. Python
    evaluates them top to bottom and runs the first block whose condition is `True`.

    ```python
    score = 74

    if score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Satisfactory")
    else:
        print("Needs improvement")
    ```

    The `else` at the end is a catch-all that runs if none of the conditions above were true.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 8

    Write a function called `letter_grade(percentage)` that returns the letter grade for a
    given percentage.

    | Grade | Range |
    |-------|-------|
    | A | 90 and above |
    | B | 80-89 |
    | C | 70-79 |
    | D | 60-69 |
    | F | below 60 |
    """)
    return


@app.cell
def _():
    def letter_grade(percentage):
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    return (letter_grade,)


@app.cell
def _(letter_grade):
    ex8_grade_a = letter_grade(95)
    ex8_grade_b = letter_grade(83)
    ex8_grade_c = letter_grade(74)
    ex8_grade_d = letter_grade(61)
    ex8_grade_f = letter_grade(42)
    print(ex8_grade_a, ex8_grade_b, ex8_grade_c, ex8_grade_d, ex8_grade_f)
    return (ex8_grade_a, ex8_grade_b, ex8_grade_c, ex8_grade_d, ex8_grade_f)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Combining Conditions

    Use `and` and `or` to combine multiple conditions in a single `if` statement.

    - `and` - both conditions must be true
    - `or` - at least one condition must be true

    ```python
    percentage = 85
    absences = 1

    if percentage >= 60 and absences <= 3:
        print("Eligible to advance")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 9

    Write a function called `can_graduate(percentage, credits_completed)` that returns
    `True` if a student meets the normal graduation requirements (percentage of 60 or above
    **and** at least 120 credits completed), **or** if the student has completed 150 or more
    credits (extended-study waiver, regardless of their grade). Return `False` otherwise.
    """)
    return


@app.cell
def _():
    def can_graduate(percentage, credits_completed):
        if (percentage >= 60 and credits_completed >= 120) or credits_completed >= 150:
            return True
        else:
            return False
    return (can_graduate,)


@app.cell
def _(can_graduate):
    ex9_result_yes = can_graduate(72, 125)
    ex9_result_no_grade = can_graduate(45, 125)
    ex9_result_no_credits = can_graduate(72, 100)
    ex9_result_waiver = can_graduate(55, 155)
    print(ex9_result_yes)
    print(ex9_result_no_grade)
    print(ex9_result_no_credits)
    print(ex9_result_waiver)
    return (ex9_result_yes, ex9_result_no_grade, ex9_result_no_credits, ex9_result_waiver)


# ── Section 4: Loops ──────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 4: Loops
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## While Loops

    A `while` loop repeats a block of code as long as a condition is true.

    ```python
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown = countdown - 1
    print("Done!")
    ```

    Output:
    ```
    3
    2
    1
    Done!
    ```

    While loops are useful when you don't know in advance how many times you need to repeat. For most tasks in data analysis and everyday programming, `for` loops are more common.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## For Loops

    A `for` loop repeats a block of code once for each item in a sequence. The most common way to generate a sequence of numbers is `range()`.

    ```python
    for i in range(5):
        print(i)
    ```

    Output:
    ```
    0
    1
    2
    3
    4
    ```

    `range(n)` generates numbers from `0` up to (but not including) `n`. You can also provide a start and stop:

    ```python
    for i in range(1, 6):
        print(i)   # prints 1, 2, 3, 4, 5
    ```

    And an optional step to control the increment:

    ```python
    for i in range(0, 11, 2):
        print(i)   # prints 0, 2, 4, 6, 8, 10
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 10

    **Instructions:** Use a `for` loop and `range()` to print the letter grade for every 10-point increment from 0 to 100. Use your `letter_grade` function. Name your loop variable `ex10_score`.

    Example output:
    ```
    0%: F
    10%: F
    20%: F
    30%: F
    40%: F
    50%: F
    60%: D
    70%: C
    80%: B
    90%: A
    100%: A
    ```
    """)
    return


@app.cell
def _(letter_grade):
    for ex10_score in range(0, 101, 10):
        print(f"{ex10_score}%: {letter_grade(ex10_score)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Counting with a Loop

    A common pattern is to use a counter variable that you increment inside a loop.

    ```python
    count = 0
    for i in range(10):
        if i >= 5:
            count = count + 1
    print(count)  # 5
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nested Loops

    A **nested loop** is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

    ```python
    for row in range(1, 3):
        for col in range(1, 3):
            print(f"row {row}, col {col}")
    ```

    Output:
    ```
    row 1, col 1
    row 1, col 2
    row 2, col 1
    row 2, col 2
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 12

    **Instructions:** Write a function called `print_extra_credit_impact(base_score, total, max_extra)` that shows how each additional extra credit point (from 0 up to `max_extra`) changes a student's letter grade. Use `calculate_percentage` and `letter_grade`.
    """)
    return


@app.cell
def _(calculate_percentage, letter_grade):
    def print_extra_credit_impact(base_score, total, max_extra):
        for extra in range(0, max_extra + 1):
            new_score = base_score + extra
            percentage = calculate_percentage(new_score, total)
            grade = letter_grade(percentage)
            print(f"+{extra} points: {new_score}/{total} -> {grade}")
    return (print_extra_credit_impact,)


@app.cell
def _(print_extra_credit_impact):
    print_extra_credit_impact(55, 100, 10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 13

    **Instructions:** A professor wants to see how different combinations of homework average and final exam score affect a student's final grade. The homework average counts for 70% of the final grade and the final exam counts for 30%. Compute the combined score with: `ex13_combined = ex13_homework_average * 0.7 + ex13_final_score * 0.3`, then pass `ex13_combined` to `letter_grade` to get the grade. Use nested loops to print the resulting letter grade for homework averages and final exam scores of 70, 80, and 90. Use `range(70, 100, 10)` to generate those three values. Name your loop variables `ex13_homework_average` and `ex13_final_score`.

    Example output:
    ```
    Homework: 70, Final: 70 -> C
    Homework: 70, Final: 80 -> C
    Homework: 70, Final: 90 -> C
    Homework: 80, Final: 70 -> C
    Homework: 80, Final: 80 -> B
    Homework: 80, Final: 90 -> B
    Homework: 90, Final: 70 -> B
    Homework: 90, Final: 80 -> B
    Homework: 90, Final: 90 -> A
    ```
    """)
    return


@app.cell
def _(letter_grade):
    for ex13_homework_average in range(70, 100, 10):
        for ex13_final_score in range(70, 100, 10):
            ex13_combined = ex13_homework_average * 0.7 + ex13_final_score * 0.3
            print(f"Homework: {ex13_homework_average}, Final: {ex13_final_score} -> {letter_grade(ex13_combined)}")
    return


# ── Section 5: Lists ──────────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 5: Lists
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Lists

    A **list** is an ordered collection of values. Create one with square brackets, separating items with commas.

    ```python
    scores = [88, 72, 95, 61, 83]
    names = ["Alex", "Jordan", "Morgan"]
    ```

    Lists can hold any type of value, and a single list can mix types. In practice, lists usually hold one type.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Indexing

    Access individual items by their **index** - their position in the list, starting at 0.

    ```python
    scores = [88, 72, 95, 61, 83]

    print(scores[0])   # 88  (first item)
    print(scores[2])   # 95  (third item)
    print(scores[-1])  # 83  (last item)
    print(scores[-2])  # 61  (second to last)
    ```

    Negative indices count from the end of the list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looping Over Lists

    `for` loops become much more useful with lists. Instead of using `range()`, you can loop directly over a list's items.

    ```python
    scores = [88, 72, 95]

    for score in scores:
        print(score)
    ```

    Output:
    ```
    88
    72
    95
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 14

    Write a function called `print_class_grades(scores)` that takes a list of scores and prints the letter grade for each one. Use your `letter_grade` function.

    Each line of output should follow this format:
    ```
    72 -> C
    88 -> B
    ```
    """)
    return


@app.cell
def _(letter_grade):
    def print_class_grades(scores):
        for score in scores:
            print(f"{score} -> {letter_grade(score)}")
    return (print_class_grades,)


@app.cell
def _(print_class_grades):
    print_class_grades([72, 88, 65, 91, 78])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Useful List Functions and Methods

    ```python
    scores = [88, 72, 95, 61, 83]

    len(scores)       # 5    - number of items
    max(scores)       # 95   - largest value
    min(scores)       # 61   - smallest value
    sum(scores)       # 399  - sum of all values
    sorted(scores)    # [61, 72, 83, 88, 95] - returns a new sorted list

    scores.append(79) # adds 79 to the end of the list
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 16

    Write a function called `class_report(scores)` that takes a list of scores and prints a class performance summary: the number of students, the class average with its letter grade, and the highest and lowest scores. This is the most complex exercise in the section - take it step by step.

    Example output:
    ```
    Students: 10
    Average: 68.1 (D)
    Highest: 95
    Lowest: 39
    ```
    """)
    return


@app.cell
def _(letter_grade):
    def class_report(scores):
        count = len(scores)
        average = sum(scores) / count
        print(f"Students: {count}")
        print(f"Average: {average:.1f} ({letter_grade(average)})")
        print(f"Highest: {max(scores)}")
        print(f"Lowest: {min(scores)}")
    return (class_report,)


@app.cell
def _(class_report):
    ex16_scores = [88, 45, 72, 61, 39, 95, 58, 83, 76, 64]
    class_report(ex16_scores)
    return (ex16_scores,)


# ── Section 6: Dictionaries ───────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 6: Dictionaries

    A list is good when order matters and all items are the same kind of thing. A dictionary is better when each item has a name -- like a student name paired with their score.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Dictionaries

    A **dictionary** stores data as **key-value pairs**. Create one with curly braces.

    ```python
    student = {
        "name": "Alex",
        "score": 88,
        "grade": "B"
    }
    ```

    Keys are usually strings. Values can be any type. Access a value by its key using square brackets.

    ```python
    print(student["name"])   # Alex
    print(student["score"])  # 88
    ```
    """)
    return


@app.cell
def _():
    _student = {
        "name": "Alex",
        "score": 88,
        "grade": "B"
    }
    print(_student["name"])
    print(_student["score"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Adding, Updating, and Iterating

    Add a new entry or update an existing one with the same syntax:

    ```python
    student["score"] = 91   # update existing
    student["year"] = 2     # add new key
    ```

    Loop over a dictionary using `.items()` to get both key and value at once:

    ```python
    grades = {"Alex": 88, "Jordan": 72}

    for name, score in grades.items():
        print(f"{name}: {score}")
    ```

    Output:
    ```
    Alex: 88
    Jordan: 72
    ```

    You can also loop over just `.keys()` or just `.values()` if you only need one side.

    ```python
    max(grades.values())   # highest value in the dictionary
    len(grades)            # number of key-value pairs
    ```
    """)
    return


@app.cell
def _():
    _grades = {"Alex": 88, "Jordan": 72}
    for _name, _score in _grades.items():
        print(f"{_name}: {_score}")
    print(max(_grades.values()))
    print(len(_grades))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 18

    Start with the provided gradebook below. Add a new student `"Casey"` with a score of `79`, then update `"Morgan"`'s score to `91`. Loop over the updated gradebook and print each student's name, score, and letter grade (use your `letter_grade` function from Section 3).

    Name your loop variables `ex18_name` and `ex18_score`.

    Example output:
    ```
    Alex: 88 (B)
    Jordan: 72 (C)
    Morgan: 91 (A)
    Taylor: 61 (D)
    Casey: 79 (C)
    ```
    """)
    return


@app.cell
def _(letter_grade):
    ex18_grades = {"Alex": 88, "Jordan": 72, "Morgan": 95, "Taylor": 61}
    ex18_grades["Casey"] = 79
    ex18_grades["Morgan"] = 91
    for ex18_name, ex18_score in ex18_grades.items():
        print(f"{ex18_name}: {ex18_score} ({letter_grade(ex18_score)})")
    return (ex18_grades,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dictionaries with List Values

    A dictionary value can be any type, including a list. This lets you store multiple pieces of data per key.

    ```python
    gradebook = {
        "Alex": [88, 72, 95],
        "Jordan": [61, 78, 83]
    }

    print(gradebook["Alex"])       # [88, 72, 95]
    print(gradebook["Alex"][0])    # 88 (first score)
    ```

    You can iterate over the dictionary and use the inner list in the loop body:

    ```python
    for name, scores in gradebook.items():
        average = sum(scores) / len(scores)
        print(f"{name}: {average:.1f}")
    ```
    """)
    return


@app.cell
def _():
    _gradebook = {
        "Alex": [88, 72, 95],
        "Jordan": [61, 78, 83]
    }
    print(_gradebook["Alex"])
    print(_gradebook["Alex"][0])
    for _name, _scores in _gradebook.items():
        _average = sum(_scores) / len(_scores)
        print(f"{_name}: {_average:.1f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 20

    Write a function called `print_gradebook_report(gradebook)` that takes a dictionary mapping student names to a list of their assignment scores. For each student, print their name, average score (to one decimal place), and letter grade (use your `letter_grade` function from Section 3).

    Example output:
    ```
    Alex: 85.0 (B)
    Jordan: 74.0 (C)
    Morgan: 51.7 (F)
    Taylor: 90.0 (A)
    ```
    """)
    return


@app.cell
def _(letter_grade):
    def print_gradebook_report(gradebook):
        for name, scores in gradebook.items():
            average = sum(scores) / len(scores)
            print(f"{name}: {average:.1f} ({letter_grade(average)})")
    return (print_gradebook_report,)


@app.cell
def _(print_gradebook_report):
    ex20_gradebook = {
        "Alex":   [88, 72, 95],
        "Jordan": [61, 78, 83],
        "Morgan": [45, 52, 58],
        "Taylor": [90, 87, 93]
    }
    print_gradebook_report(ex20_gradebook)
    return (ex20_gradebook,)


# ── Section 7: Pandas & DataFrames ───────────────────────────────────────────

@app.cell(hide_code=True)
def _(pd):
    import pathlib
    _csv_path = pathlib.Path(__file__).parent / "gradebook.csv"
    _data = {
        "name": [
            "Alex", "Jordan", "Morgan", "Taylor", "Casey",
            "Jamie", "Dana", "Riley", "Quinn", "Blake",
            "Avery", "Cameron", "Drew", "Emery", "Finley",
            "Harper", "Hayden", "Jesse", "Kai", "Lane",
            "Logan", "Maddox", "Max", "Parker", "Peyton",
            "Reese", "River", "Sage", "Skyler", "Sydney",
        ],
        "homework": [
            88.0, 72.0, 95.0, 61.0, 83.0,
            90.0, 55.0, 78.0, 65.0, 92.0,
            80.0, 70.0, 85.0, 58.0, 96.0,
            74.0, 68.0, 87.0, 51.0, 93.0,
            77.0, 62.0, 89.0, 75.0, 84.0,
            91.0, 66.0, 79.0, 98.0, 59.0,
        ],
        "midterm": [
            82, 68, 91, 58, 77,
            85, 62, 75, 60, 94,
            78, 65, 88, 55, 98,
            71, 72, 84, 48, 90,
            80, 66, 87, 73, 82,
            89, 63, 76, 97, 57,
        ],
        "final_exam": [
            79, 74, 88, 63, 80,
            92, 58, 71, 51, 96,
            82, 68, 84, 44, 95,
            77, 70, 86, 53, 91,
            75, 60, 90, 78, 83,
            93, 65, 74, 99, 55,
        ],
        "letter": [
            "B", "C", "A", "D", "B",
            "B", "F", "C", "F", "A",
            "B", "D", "B", "F", "A",
            "C", "C", "B", "F", "A",
            "C", "D", "B", "C", "B",
            "A", "D", "C", "A", "F",
        ],
    }
    _setup_df = pd.DataFrame(_data)
    _setup_df.to_csv(_csv_path, index=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 7: Pandas & DataFrames
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What is Pandas?

    In Section 6, you grouped student data in a dictionary. That works for small hand-crafted datasets. When you have a CSV file with hundreds of rows and need to filter, sort, and aggregate, loops and dicts get tedious. Pandas handles that automatically.

    **Pandas** is a Python library for working with tabular data - data organized into rows and columns, like a spreadsheet. The core data structure is called a **DataFrame**.

    Import pandas at the top of your notebook:

    ```python
    import pandas as pd
    ```

    The `as pd` part gives pandas a shorter alias so you can write `pd.something` instead of `pandas.something`. This is standard practice.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading a CSV File

    Load a CSV file into a DataFrame using `pd.read_csv()`:

    ```python
    gradebook_df = pd.read_csv("gradebook.csv")
    ```

    The variable `gradebook_df` now holds the entire table in memory.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exploring a DataFrame

    After loading data, a few attributes and methods help you understand what you have:

    ```python
    gradebook_df.head()     # shows the first 5 rows
    gradebook_df.shape      # returns (number of rows, number of columns)
    gradebook_df.columns    # returns the column names
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 21

    Load `gradebook.csv` into a DataFrame called `gradebook_df`. Print the first 5 rows,
    the shape, and the column names.

    Example output:
    ```
         name  homework  midterm  final_exam letter
    0    Alex      88.0       82          79      B
    1  Jordan      72.0       68          74      C
    2  Morgan      95.0       91          88      A
    3  Taylor      61.0       58          63      D
    4   Casey      83.0       77          80      B

    Shape: (30, 5)
    Columns: Index(['name', 'homework', 'midterm', 'final_exam', 'letter'], dtype='object')
    ```
    """)
    return


@app.cell
def _(pd):
    gradebook_df = pd.read_csv("gradebook.csv")
    print(gradebook_df.head())
    print()
    print(f"Shape: {gradebook_df.shape}")
    print(f"Columns: {gradebook_df.columns}")
    return (gradebook_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Selecting a Column

    Select a single column by putting its name in square brackets. This returns a **Series** -
    a single column of values.

    ```python
    gradebook_df["homework"]
    ```

    You can call aggregation methods directly on a column:

    ```python
    gradebook_df["homework"].mean()    # average of all homework scores
    gradebook_df["homework"].max()     # highest homework score
    gradebook_df["homework"].min()     # lowest homework score
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 22

    Select the `homework` column from `gradebook_df`. Store the mean in `ex22_homework_mean`,
    the max in `ex22_homework_max`, and the min in `ex22_homework_min`.
    """)
    return


@app.cell
def _(gradebook_df):
    ex22_homework_mean = gradebook_df["homework"].mean()
    ex22_homework_max = gradebook_df["homework"].max()
    ex22_homework_min = gradebook_df["homework"].min()
    return (ex22_homework_mean, ex22_homework_max, ex22_homework_min)


@app.cell
def _(ex22_homework_max, ex22_homework_mean, ex22_homework_min):
    print(f"Homework mean: {ex22_homework_mean:.1f}")
    print(f"Homework max:  {ex22_homework_max:.1f}")
    print(f"Homework min:  {ex22_homework_min:.1f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Selecting Multiple Columns

    Pass a list of column names to select several columns at once. This returns a smaller DataFrame.

    ```python
    gradebook_df[["name", "final_exam"]]
    ```

    Note the double square brackets: the outer ones do the selection, and the inner ones create
    the list of column names.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Filtering Rows

    Filter rows by writing a condition inside square brackets. Only rows where the condition
    is `True` are kept.

    ```python
    gradebook_df[gradebook_df["final_exam"] >= 90]   # students who scored 90 or above
    gradebook_df[gradebook_df["homework"] < 60]      # students with homework below 60
    ```

    The condition `gradebook_df["final_exam"] >= 90` checks every row and returns `True` or
    `False` for each one. The outer `gradebook_df[...]` then keeps only the `True` rows.

    After filtering, the original row numbers are preserved in the result. A filtered DataFrame
    might show rows numbered 6, 14, 21 -- that is correct, not a mistake.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 23

    Filter `gradebook_df` to only students who scored below 60 on the final exam. Store the
    **full filtered DataFrame** in `ex23_at_risk`. Storing the full DataFrame lets you access
    any column later if needed.
    """)
    return


@app.cell
def _(gradebook_df):
    ex23_at_risk = gradebook_df[gradebook_df["final_exam"] < 60]
    return (ex23_at_risk,)


@app.cell
def _(ex23_at_risk):
    print(ex23_at_risk[["name", "final_exam"]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Adding a Computed Column

    Assign a new column to a DataFrame the same way you assign a variable, using the column
    name as a key:

    ```python
    gradebook_df["total"] = gradebook_df["midterm"] + gradebook_df["final_exam"]
    ```

    The operation runs on every row at once - no loop needed. You can use any arithmetic
    operator between columns, or between a column and a number:

    ```python
    gradebook_df["midterm"] + gradebook_df["final_exam"]   # add two columns together
    gradebook_df["homework"] * 0.3                         # multiply every value by 0.3
    ```

    When you combine two columns, pandas lines them up row by row and applies the operation
    to each pair.

    You can also chain operations together to build more complex calculations:

    ```python
    gradebook_df["weighted"] = gradebook_df["homework"] * 0.3 + gradebook_df["final_exam"] * 0.7
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 24

    Add a column called `weighted_average` to `gradebook_df`, calculated as:
    homework 30%, midterm 30%, final exam 40%.
    """)
    return


@app.cell
def _(gradebook_df):
    gradebook_df["weighted_average"] = (
        gradebook_df["homework"] * 0.3 +
        gradebook_df["midterm"] * 0.3 +
        gradebook_df["final_exam"] * 0.4
    )
    return


@app.cell
def _(gradebook_df):
    print(gradebook_df[["name", "weighted_average"]].head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sorting a DataFrame

    Use `.sort_values()` to sort a DataFrame by a column. Pass the column name with `by=`
    and set `ascending=False` to sort from highest to lowest:

    ```python
    gradebook_df.sort_values(by="final_exam", ascending=False)   # highest to lowest
    gradebook_df.sort_values(by="final_exam", ascending=True)    # lowest to highest
    ```

    This returns a new sorted DataFrame - it does not modify the original.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 25

    Create `ex25_sorted`: a DataFrame showing just `name`, `weighted_average`, and `letter`,
    sorted from highest to lowest weighted average.
    """)
    return


@app.cell
def _(gradebook_df):
    ex25_sorted = gradebook_df[["name", "weighted_average", "letter"]].sort_values(
        by="weighted_average",
        ascending=False
    )
    return (ex25_sorted,)


@app.cell
def _(ex25_sorted):
    print(ex25_sorted)
    return


# ── Section 8: Matplotlib ─────────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 8: Matplotlib

    **Matplotlib** is a Python library for creating charts and graphs. Import it like this:

    ```python
    import matplotlib.pyplot as plt
    ```

    The `as plt` alias is standard convention, just like `as pd` for pandas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Basic Plot Structure

    Every matplotlib plot follows the same pattern: call one or more functions to build the chart, then call `plt.show()` to display it.

    ```python
    plt.bar(["A", "B", "C"], [10, 20, 15])
    plt.show()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Titles and Labels

    Always add a title and axis labels to make your chart readable:

    ```python
    plt.title("My Chart Title")
    plt.xlabel("Label for the x-axis")
    plt.ylabel("Label for the y-axis")
    ```

    These should be called before `plt.show()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Figure Size

    By default, matplotlib chooses a size for your chart. You can control it with `plt.figure()` before building the plot:

    ```python
    plt.figure(figsize=(10, 5))   # width=10, height=5 (in inches)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bar Charts

    `plt.bar()` takes a list of labels and a list of values:

    ```python
    subjects = ["Math", "English", "Science"]
    scores = [85, 92, 78]

    plt.bar(subjects, scores)
    plt.title("Scores by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Score")
    plt.show()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 26

    **Instructions:** Create a bar chart showing the class average score for each assessment. Compute the mean of each column (`homework`, `midterm`, `final_exam`) from `gradebook_df`. Store them in `ex26_homework_mean`, `ex26_midterm_mean`, and `ex26_final_mean`. Store the label list in `ex26_assessments` and the mean list in `ex26_means`. Add a title and labels for both axes.

    Example output: a bar chart with three bars labeled "Homework", "Midterm", and "Final Exam".
    """)
    return


@app.cell
def _(gradebook_df, plt):
    ex26_homework_mean = gradebook_df["homework"].mean()
    ex26_midterm_mean = gradebook_df["midterm"].mean()
    ex26_final_mean = gradebook_df["final_exam"].mean()

    ex26_assessments = ["Homework", "Midterm", "Final Exam"]
    ex26_means = [ex26_homework_mean, ex26_midterm_mean, ex26_final_mean]

    plt.bar(ex26_assessments, ex26_means)
    plt.title("Class Average by Assessment")
    plt.xlabel("Assessment")
    plt.ylabel("Average Score")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Scatter Plots

    `plt.scatter()` plots one column against another, one point per row. Useful for seeing relationships between two variables.

    ```python
    plt.scatter(df["homework"], df["final_exam"])
    plt.xlabel("Homework Score")
    plt.ylabel("Final Exam Score")
    plt.show()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 27

    **Instructions:** Create a scatter plot of `homework` scores (x-axis) vs `final_exam` scores (y-axis) from `gradebook_df`. Add a title and axis labels.

    Example output: a scatter plot with one dot per student.
    """)
    return


@app.cell
def _(gradebook_df, plt):
    plt.scatter(gradebook_df["homework"], gradebook_df["final_exam"])
    plt.title("Homework vs Final Exam Scores")
    plt.xlabel("Homework Score")
    plt.ylabel("Final Exam Score")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Histograms

    A histogram shows how values are distributed - how many students scored in each range, for example. Use `plt.hist()` and pass a single column:

    ```python
    plt.hist(df["final_exam"])
    plt.show()
    ```

    The bars represent ranges of values (called "bins"), and the height of each bar shows how many students fall in that range.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 28

    **Instructions:** Create a histogram of the `weighted_average` column from `gradebook_df`. Add a title and axis labels.

    Example output: a histogram showing the distribution of weighted averages across the class.
    """)
    return


@app.cell
def _(gradebook_df, plt):
    plt.hist(gradebook_df["weighted_average"])
    plt.title("Distribution of Weighted Averages")
    plt.xlabel("Weighted Average")
    plt.ylabel("Number of Students")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Counting Values

    `.value_counts()` counts how many times each unique value appears in a column. It is useful for categorical columns like letter grades:

    ```python
    gradebook_df["letter"].value_counts()
    ```

    To sort the result alphabetically by grade (A, B, C, D, F) instead of by count, chain `.sort_index()`:

    ```python
    gradebook_df["letter"].value_counts().sort_index()
    ```

    This returns a Series where `.index` contains the labels (the letter grades) and `.values` contains the counts (how many students received each grade). You can use them separately to build a bar chart.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 29

    **Instructions:** Create a bar chart showing how many students received each letter grade. Use `.value_counts().sort_index()` on the `letter` column. Store the result in `ex29_grade_counts`. Sort the grades alphabetically (A through F). Pass `ex29_grade_counts.index` as the labels and `ex29_grade_counts.values` as the heights to `plt.bar()`. Add a title and axis labels.

    Example output: a bar chart with up to 5 bars labeled A, B, C, D, F.
    """)
    return


@app.cell
def _(gradebook_df, plt):
    ex29_grade_counts = gradebook_df["letter"].value_counts().sort_index()

    plt.bar(ex29_grade_counts.index, ex29_grade_counts.values)
    plt.title("Grade Distribution")
    plt.xlabel("Letter Grade")
    plt.ylabel("Number of Students")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reference Lines

    `plt.axhline()` draws a horizontal line across the whole chart at a given y value. This is useful for marking thresholds like a passing grade:

    ```python
    plt.axhline(y=60, color="red", linestyle="--")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Plotting by Position

    When you need to plot data that does not have natural labels - like 30 students sorted by rank - use `range(len(...))` to generate position numbers for the x-axis:

    ```python
    ex30_sorted = gradebook_df["weighted_average"].sort_values().values
    plt.bar(range(len(ex30_sorted)), ex30_sorted)
    plt.xlabel("Rank")
    plt.show()
    ```

    `.values` converts the pandas column to a plain array that matplotlib can use.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 30

    **Instructions:** Create a bar chart of all students' weighted averages, sorted from lowest to highest. Use `.sort_values().values` on the `weighted_average` column to get the sorted array. Store the result in `ex30_sorted`. Add a horizontal reference line at 60 (passing) and another at 90 (A grade). Add axis labels. Set the figure size to `(12, 5)`.

    Example output: a bar chart with 30 bars rising from left to right, with red and green reference lines at 60 and 90.
    """)
    return


@app.cell
def _(gradebook_df, plt):
    ex30_sorted = gradebook_df["weighted_average"].sort_values().values

    plt.figure(figsize=(12, 5))
    plt.bar(range(len(ex30_sorted)), ex30_sorted)
    plt.axhline(y=60, color="red", linestyle="--")
    plt.axhline(y=90, color="green", linestyle="--")
    plt.title("Student Weighted Averages - Lowest to Highest")
    plt.xlabel("Student Rank")
    plt.ylabel("Weighted Average")
    plt.show()
    return


# ── Section 9: Scikit-learn ───────────────────────────────────────────────────

@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 9: Scikit-learn

    ## What is Machine Learning?

    **Machine learning** is the practice of training a program to make predictions by learning patterns from data, rather than by following explicit rules you write yourself.

    A classic question: can we predict how well a student will do on the final exam based on their study habits? You could try to write rules by hand ("if they study more than 10 hours, predict above 80..."), but that gets complicated fast. Machine learning finds the pattern automatically from the data.

    **Scikit-learn** is Python's most widely used machine learning library. It provides a consistent interface for training and evaluating models.

    ```python
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A New Dataset

    For this section we will use a larger student dataset with information beyond just grades. The file `students.csv` has 150 rows with columns: `study_hours`, `attendance`, `homework`, `midterm`, and `final_exam`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Features and Labels

    Every supervised machine learning problem has two parts:

    - **Features:** the input columns the model uses to make a prediction
    - **Label:** the output column you want to predict

    We will use `study_hours` and `attendance` as features to predict `final_exam` scores. This is more interesting than using test scores to predict test scores - we are asking whether real-world behavior predicts academic outcomes.

    In code, features are usually stored as a DataFrame (multiple columns) and the labels as a Series (one column):

    ```python
    features = df[["study_hours", "attendance"]]
    labels = df["final_exam"]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 31

    **Instructions:** Using `ex31_df`, store the `study_hours` and `attendance` columns (use double brackets to keep it as a DataFrame) in `ex31_features`, and the `final_exam` column in `ex31_labels`.
    """)
    return


@app.cell
def _(pd):
    ex31_df = pd.read_csv("students.csv")
    ex31_features = ex31_df[["study_hours", "attendance"]]
    ex31_labels = ex31_df["final_exam"]
    return ex31_df, ex31_features, ex31_labels


@app.cell
def _(ex31_features, ex31_labels):
    print(f"Features shape: {ex31_features.shape}")
    print(f"Labels length: {len(ex31_labels)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Training and Test Sets

    A key idea in machine learning is that you should not evaluate your model on the same data you trained it on. If you do, you have no way of knowing whether it learned a real pattern or just memorized the training data.

    The standard approach is to split your data into two parts:

    - **Training set:** the model learns from this data
    - **Test set:** the model is evaluated on this data, which it has never seen

    `train_test_split` does this split randomly:

    ```python
    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )
    ```

    - `test_size=0.2` reserves 20% of the data for testing
    - `random_state=42` fixes the random seed so you get the same split every time you run the notebook
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 32

    **Instructions:** Split `ex31_features` and `ex31_labels` into training and test sets using `test_size=0.2` and `random_state=42`. Store the results in `ex32_features_train`, `ex32_features_test`, `ex32_labels_train`, and `ex32_labels_test`.
    """)
    return


@app.cell
def _(ex31_features, ex31_labels, train_test_split):
    ex32_features_train, ex32_features_test, ex32_labels_train, ex32_labels_test = train_test_split(
        ex31_features, ex31_labels, test_size=0.2, random_state=42
    )
    return ex32_features_test, ex32_features_train, ex32_labels_test, ex32_labels_train


@app.cell
def _(ex32_features_test, ex32_features_train):
    print(f"Training rows: {len(ex32_features_train)}")
    print(f"Test rows: {len(ex32_features_test)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Linear Regression

    **Linear regression** finds the relationship that best fits the data. Once trained, it can predict a label value for any new feature values.

    Create a model, train it with `.fit()`, then generate predictions with `.predict()`:

    ```python
    model = LinearRegression()
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)
    ```

    `.fit()` is where the learning happens. `.predict()` applies what was learned to new data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Evaluating the Model

    `.score()` returns the **R^2 score** (R-squared), which measures how well the model's predictions match the actual values.

    - R^2 = 1.0 means perfect predictions
    - R^2 = 0.0 means the model does no better than always predicting the mean

    ```python
    model.score(features_test, labels_test)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 33

    **Instructions:** Create a `LinearRegression` model called `ex33_model`. Train it by calling `.fit()` with `ex32_features_train` and `ex32_labels_train`. Generate predictions on the test set by calling `.predict()` with `ex32_features_test` and store them in `ex33_predictions`. Evaluate the model by calling `.score()` with `ex32_features_test` and `ex32_labels_test` and store the R^2 score in `ex33_score`.
    """)
    return


@app.cell
def _(LinearRegression, ex32_features_test, ex32_features_train, ex32_labels_test, ex32_labels_train):
    ex33_model = LinearRegression()
    ex33_model.fit(ex32_features_train, ex32_labels_train)
    ex33_predictions = ex33_model.predict(ex32_features_test)
    ex33_score = ex33_model.score(ex32_features_test, ex32_labels_test)
    return ex33_model, ex33_predictions, ex33_score


@app.cell
def _(ex32_labels_test, ex33_predictions, ex33_score):
    print("Predicted  Actual")
    for _i in range(5):
        print(f"{ex33_predictions[_i]:.1f}       {ex32_labels_test.iloc[_i]}")
    print(f"R^2 score: {ex33_score:.3f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Line Plots

    `plt.plot()` draws a line connecting a sequence of points. Pass two lists: x coordinates and y coordinates.

    ```python
    plt.plot([40, 100], [40, 100], color="red", linestyle="--")
    ```

    This draws a dashed red line from the point (40, 40) to the point (100, 100). On a chart of actual vs. predicted values, a diagonal line from corner to corner represents perfect predictions - the closer points cluster to this line, the better the model.

    You can combine `plt.scatter()` and `plt.plot()` in the same chart to overlay a line on top of scatter points.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 35

    **Instructions:** Create a scatter plot comparing the model's predictions to the actual test scores. Use `ex32_labels_test` as the x values and `ex33_predictions` as the y values. Add a dashed red diagonal line from (40, 40) to (100, 100) representing perfect predictions - points close to this line indicate accurate predictions. Add a title and axis labels.
    """)
    return


@app.cell
def _(ex32_labels_test, ex33_predictions, plt):
    plt.scatter(ex32_labels_test, ex33_predictions)
    plt.plot([40, 100], [40, 100], color="red", linestyle="--")
    plt.title("Actual vs Predicted Final Exam Scores")
    plt.xlabel("Actual Score")
    plt.ylabel("Predicted Score")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
