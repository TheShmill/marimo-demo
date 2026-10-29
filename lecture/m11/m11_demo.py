# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.24.2",
#     "matplotlib==3.11.2",
#     "pandas==3.0.5",
#     "scikit-learn>=1.5",
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
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from sklearn.inspection import DecisionBoundaryDisplay
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier, plot_tree

    return (
        DecisionBoundaryDisplay,
        DecisionTreeClassifier,
        KNeighborsClassifier,
        LogisticRegression,
        accuracy_score,
        confusion_matrix,
        mo,
        np,
        pd,
        plot_tree,
        plt,
        roc_auc_score,
        roc_curve,
        sns,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Research Question
    Can we tell which adults have heart disease from their cholesterol and blood pressure?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # The Dataset
    We will look at a synthesized dataset. Each row represents an adult seen at a heart health clinic with the following details:
    - total cholesterol in mg/dL
    - systolic blood pressure in mmHg
    - heart disease, 1 if testing confirmed heart disease and 0 if not
    """)
    return


@app.cell
def _(pd):
    # Load the dataset
    df = pd.read_csv("m11_demo.csv")
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Predictor and Response
    Cholesterol and systolic blood pressure are the **predictors** and heart disease is the **response**.
    """)
    return


@app.cell
def _(df):
    # Predictor (X) and response (y)
    X = df[["cholesterol", "systolic_bp"]]
    y = df["heart_disease"]
    return X, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Training and Test Sets
    """)
    return


@app.cell
def _(X, train_test_split, y):
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=37
    )
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A New Patient
    A new patient comes to the clinic with a cholesterol of 220 mg/dL and a systolic blood pressure of 150 mmHg, both raised. We will ask each model whether this patient has heart disease. *As in the regression demo, a model needs the patient as **a table with one row and the same columns as `X`**.*
    """)
    return


@app.cell
def _(pd):
    # The new patient as a one-row table
    new_patient = pd.DataFrame({"cholesterol": [220], "systolic_bp": [150]})
    new_patient
    return (new_patient,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Logistic Regression
    *A **logistic regression** model works like the regression line from the last demo: it multiplies each predictor by a coefficient and adds them up. It then **squeezes that total into a probability between 0 and 1**, and predicts heart disease when the probability is above 0.5, a cutoff called the **threshold**.*
    """)
    return


@app.cell
def _(LogisticRegression, X_train, y_train):
    # Create the model and fit it to the training set
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    return (logreg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Coefficients
    As in the regression demo, the learned coefficients (cholesterol, blood pressure) and the intercept are stored on the model.
    """)
    return


@app.cell
def _(logreg):
    # Coefficients and intercept
    logreg.coef_, logreg.intercept_
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Both coefficients are positive**, so higher cholesterol and higher blood pressure both raise the predicted chance of heart disease. They are about the same size (0.062 and 0.069), so 1 mg/dL of cholesterol counts about as much as 1 mmHg of blood pressure. *Unlike in the regression demo, the coefficients are not in the units of the response: they change the probability through the squeeze, so they only tell us **the direction and the relative strength of each predictor**.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Decision Boundary
    *To see what the model is doing, we ask it to predict for every combination of cholesterol and blood pressure on the plot.* `DecisionBoundaryDisplay.from_estimator` does this and shades each area by the probability of heart disease: deep blue near 0, deep red near 1, and white around 0.5. The model predicts heart disease above 0.5, so the **decision boundary** runs through the white band. The dots are the training patients, colored by whether they actually have heart disease.
    """)
    return


@app.cell
def _(DecisionBoundaryDisplay, X_train, logreg, plt, sns, y_train):
    # Shade the model's probability for every cholesterol and blood pressure, then add the training patients
    DecisionBoundaryDisplay.from_estimator(
        logreg, X_train, response_method="predict_proba", cmap="bwr", alpha=0.5
    )
    sns.scatterplot(
        X_train,
        x="cholesterol",
        y="systolic_bp",
        hue=y_train,
        palette={0: "blue", 1: "red"},
    )
    plt.xlabel("Cholesterol (mg/dL)")
    plt.ylabel("Systolic blood pressure (mmHg)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Predicting for the New Patient
    `predict` gives 1 (heart disease) or 0 (no heart disease) for the new patient.
    """)
    return


@app.cell
def _(logreg, new_patient):
    # Predict heart disease for the new patient
    logreg.predict(new_patient)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Logistic regression predicts heart disease for this patient. At a cholesterol of 220, the boundary line sits at a blood pressure of about 135, and this patient's 150 is above it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Where the Prediction Comes From
    The 1 comes from a probability. `predict_proba` gives the patient's probability of each outcome: the first column is no heart disease (0) and the second is heart disease (1).
    """)
    return


@app.cell
def _(logreg, new_patient):
    # Probability of no heart disease and of heart disease for the new patient
    logreg.predict_proba(new_patient)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The model gives this patient a **0.74 chance of heart disease**. Since that is above 0.5, it predicts 1.

    We can calculate the 0.74 ourselves in two steps. First, the intercept plus each coefficient times the patient's value, as with the regression line. `coef_` is a table with one row, so `coef_[0][0]` is the cholesterol coefficient and `coef_[0][1]` the blood pressure one.
    """)
    return


@app.cell
def _(logreg):
    # Step 1: the weighted sum for cholesterol 220 and blood pressure 150
    total = logreg.intercept_[0] + logreg.coef_[0][0] * 220 + logreg.coef_[0][1] * 150
    total
    return (total,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *The weighted sum can be any number, so the second step squeezes it into a probability between 0 and 1 with the **logistic function**, $\frac{1}{1 + e^{-\text{total}}}$. A total of 0 gives exactly 0.5, **the boundary line**; positive totals give more than 0.5 and negative totals less.* `np.exp` calculates $e$ to a power.
    """)
    return


@app.cell
def _(np, total):
    # Step 2: squeeze the total into a probability
    1 / (1 + np.exp(-total))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # k Nearest Neighbors
    *A **k nearest neighbors (kNN)** model predicts for a new patient by finding the k patients in the training set whose cholesterol and blood pressure are closest to theirs. The prediction is **the outcome most of those neighbors have**.*

    We create the model with `n_neighbors=5`, so it looks at the 5 closest patients, then call `.fit` with the training predictors and response.
    """)
    return


@app.cell
def _(KNeighborsClassifier, X_train, y_train):
    # Create the model and fit it to the training set
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    return (knn,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # kNN Decision Boundary
    The same plot as for logistic regression, now shaded by how many of the 5 nearest neighbors have heart disease: deep blue where none do, deep red where all do, and white in between, where 2 or 3 of the 5 do. The model predicts heart disease when 3 or more do, so the **decision boundary** runs through the white band.
    """)
    return


@app.cell
def _(DecisionBoundaryDisplay, X_train, knn, plt, sns, y_train):
    # Shade the model's prediction for every cholesterol and blood pressure, then add the training patients
    DecisionBoundaryDisplay.from_estimator(
        knn, X_train, response_method="predict_proba", cmap="bwr", alpha=0.5
    )
    sns.scatterplot(
        X_train,
        x="cholesterol",
        y="systolic_bp",
        hue=y_train,
        palette={0: "blue", 1: "red"},
    )
    plt.xlabel("Cholesterol (mg/dL)")
    plt.ylabel("Systolic blood pressure (mmHg)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Predicting for the Same Patient
    We predict for the same new patient as before, with a cholesterol of 220 and a blood pressure of 150.
    """)
    return


@app.cell
def _(knn, new_patient):
    # Predict heart disease for the new patient
    knn.predict(new_patient)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # The 5 Nearest Neighbors
    To see where that prediction came from, `knn.kneighbors` finds the 5 training patients closest to the new patient. It returns two things: their distances (the straight line distance on the scatter plot) and their row positions in the training set. Both come back with one row per new patient, so `[0]` takes the row for our one patient, and `.iloc` picks those rows out of `X_train` and `y_train`.
    """)
    return


@app.cell
def _(X_train, knn, new_patient, y_train):
    # The 5 nearest training patients, with their outcome and distance, nearest first
    distances, indices = knn.kneighbors(new_patient)
    neighbors = X_train.iloc[indices[0]]
    neighbors["heart_disease"] = y_train.iloc[indices[0]]
    neighbors["distance"] = distances[0]
    neighbors
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **3 of the 5 nearest patients have heart disease**, so the model will predict heart disease.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Choosing k
    *The number of neighbors, k, is **the main setting of a kNN model**. With a small k, each prediction depends on only a few nearby patients, so the boundary bends around single patients and **follows the training set closely**. With a large k, each prediction is a vote among many patients, so the boundary is **smoother but can blur over small groups**.* Use the slider to change k.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Slider for the number of neighbors
    k_slider = mo.ui.slider(start=1, stop=50, value=1, label="Number of neighbors, k", show_value=True)
    k_slider
    return (k_slider,)


@app.cell
def _(
    DecisionBoundaryDisplay,
    KNeighborsClassifier,
    X_train,
    k_slider,
    plt,
    sns,
    y_train,
):
    # kNN with the number of neighbors chosen on the slider
    knn_k = KNeighborsClassifier(n_neighbors=k_slider.value)
    knn_k.fit(X_train, y_train)
    DecisionBoundaryDisplay.from_estimator(
        knn_k, X_train, response_method="predict_proba", cmap="bwr", alpha=0.5
    )
    sns.scatterplot(
        X_train,
        x="cholesterol",
        y="systolic_bp",
        hue=y_train,
        palette={0: "blue", 1: "red"},
    )
    plt.xlabel("Cholesterol (mg/dL)")
    plt.ylabel("Systolic blood pressure (mmHg)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Decision Tree
    *A **decision tree** predicts by asking **a series of yes or no questions** about the predictors, such as "is cholesterol at most 219.5?". Each answer leads to another question until the patient reaches a final group, called a **leaf**. The prediction is the outcome most of the training patients in that leaf have.*

    *`.fit` chooses **the questions that best separate** the training patients with and without heart disease.* `max_depth=3` allows at most three questions in a row, and `random_state` makes every run choose the same questions.
    """)
    return


@app.cell
def _(DecisionTreeClassifier, X_train, y_train):
    # Create the model and fit it to the training set
    tree = DecisionTreeClassifier(max_depth=3, random_state=37)
    tree.fit(X_train, y_train)
    return (tree,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Inspecting the Tree
    `plot_tree` draws the tree so that we can inspect it. Each box shows its question, then two measurements:
    - `samples`: the number of training patients who reach the box
    - `value`: two counts, the patients without heart disease and the patients with heart disease

    Patients who answer yes go left (True) and patients who answer no go right (False). The row at the bottom contains the final boxes that the values are divided into.
    """)
    return


@app.cell
def _(plot_tree, plt, tree):
    plt.figure(figsize=(12, 5))
    plot_tree(
        tree,
        feature_names=["cholesterol", "systolic_bp"],
        label="root",
        impurity=False,
        fontsize=9,
    )
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Decision Tree Boundary
    """)
    return


@app.cell
def _(DecisionBoundaryDisplay, X_train, plt, sns, tree, y_train):
    # Shade the model's probability for every cholesterol and blood pressure, then add the training patients
    DecisionBoundaryDisplay.from_estimator(
        tree, X_train, response_method="predict_proba", cmap="bwr", alpha=0.5
    )
    sns.scatterplot(X_train, x="cholesterol", y="systolic_bp", hue=y_train, palette={0: "blue", 1: "red"})
    plt.xlabel("Cholesterol (mg/dL)")
    plt.ylabel("Systolic blood pressure (mmHg)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Predicting for the New Patient
    `predict` gives 1 (heart disease) or 0 (no heart disease) for the new patient.
    """)
    return


@app.cell
def _(new_patient, tree):
    # Predict heart disease for the new patient
    tree.predict(new_patient)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Following the Questions
    The new patient's cholesterol of 220 is above 219.5, so they go right. Their blood pressure of 150 is above 132.5, so they go right again. Their cholesterol of 220 is at most 222.5, so they go left, into a leaf of 7 training patients, 4 of whom have heart disease. `predict_proba` gives that share as a probability.
    """)
    return


@app.cell
def _(new_patient, tree):
    # Probability of no heart disease and of heart disease for the new patient
    tree.predict_proba(new_patient)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **4 of 7 is 0.57**, above 0.5, so the tree predicts heart disease.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Choosing max_depth
    *The maximum depth is **the main setting of a decision tree**. Each extra level of questions can **split every box** in the decision boundary plot into two smaller boxes.* Use the slider to change the maximum depth and watch how the boundary changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Slider for the maximum depth
    depth_slider = mo.ui.slider(start=1, stop=14, step=1, value=1, label="Maximum depth", show_value=True)
    depth_slider
    return (depth_slider,)


@app.cell
def _(
    DecisionBoundaryDisplay,
    DecisionTreeClassifier,
    X_train,
    depth_slider,
    plt,
    sns,
    y_train,
):
    # Decision tree with the maximum depth chosen on the slider
    tree_d = DecisionTreeClassifier(max_depth=depth_slider.value, random_state=37)
    tree_d.fit(X_train, y_train)
    DecisionBoundaryDisplay.from_estimator(
        tree_d, X_train, response_method="predict_proba", cmap="bwr", alpha=0.5
    )
    sns.scatterplot(
        X_train,
        x="cholesterol",
        y="systolic_bp",
        hue=y_train,
        palette={0: "blue", 1: "red"},
    )
    plt.xlabel("Cholesterol (mg/dL)")
    plt.ylabel("Systolic blood pressure (mmHg)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Testing the Model
    *To see how well a model predicts **patients it has not seen**, we use the **test set**.* We start with the logistic regression model and predict heart disease for every patient in the test set.
    """)
    return


@app.cell
def _(X_test, logreg):
    # Predict heart disease for every test patient
    logreg_pred = logreg.predict(X_test)
    logreg_pred
    return (logreg_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Accuracy
    ***Accuracy** is the share of test patients whose prediction matches their actual outcome.* `accuracy_score` compares the actual outcomes, `y_test`, with the predictions.
    """)
    return


@app.cell
def _(accuracy_score, logreg_pred, y_test):
    # Share of test patients the model gets right
    accuracy_score(y_test, logreg_pred)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The model's prediction is right for **82 of the 100 test patients**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Confusion Matrix
    Heart disease is the **positive** outcome and no heart disease is the **negative** one. *Accuracy **does not distinguish between false positives and false negatives**. A **confusion matrix** splits the test patients into four groups by their actual outcome and the model's prediction.*
    """)
    return


@app.cell
def _(confusion_matrix, logreg_pred, y_test):
    # Actual outcomes (rows) against predictions (columns)
    confusion = confusion_matrix(y_test, logreg_pred)
    confusion
    return (confusion,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | | Predicted no | Predicted yes |
    |---|---|---|
    | **Actually no** | 62 true negatives | 8 false positives |
    | **Actually yes** | 10 false negatives | 20 true positives |

    *Each metric below divides one of these counts by **a different group of patients**.* As with `coef_`, `confusion[0][1]` means row 0, column 1, counting from 0.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sensitivity
    ***Sensitivity**, also called recall or the true positive rate (TPR), answers: of the patients who actually have heart disease, **how many did the model catch?*** It is the true positives divided by the bottom row.
    """)
    return


@app.cell
def _(confusion):
    # Sensitivity: true positives out of everyone with heart disease
    confusion[1][1] / (confusion[1][0] + confusion[1][1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The model catches **20 of the 30** test patients with heart disease.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Specificity
    ***Specificity** answers: of the patients without heart disease, **how many did the model correctly clear?*** It is the true negatives divided by the top row.
    """)
    return


@app.cell
def _(confusion):
    # Specificity: true negatives out of everyone without heart disease
    confusion[0][0] / (confusion[0][0] + confusion[0][1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The model correctly clears **62 of the 70** test patients without heart disease.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Precision
    ***Precision**, also called the positive predictive value (PPV), answers: of the patients the model flagged, **how many actually have heart disease?*** It is the true positives divided by the right column.
    """)
    return


@app.cell
def _(confusion):
    # Precision: true positives out of everyone predicted to have heart disease
    confusion[1][1] / (confusion[0][1] + confusion[1][1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of the 28 test patients the model flagged, **20** actually have heart disease.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # False Positive Rate
    *The **false positive rate (FPR)** answers: of the patients without heart disease, **what share got a false alarm?*** It is the false positives divided by the top row, which makes it *1 minus the specificity*.
    """)
    return


@app.cell
def _(confusion):
    # False positive rate: false positives out of everyone without heart disease
    confusion[0][1] / (confusion[0][0] + confusion[0][1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **8 of the 70** test patients without heart disease got a false alarm.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Changing the Threshold
    *`predict` flags a patient when their probability of heart disease is above 0.5. That cutoff is called the **threshold**. Moving it changes which patients are flagged, **without fitting a new model**.* We start from the probability of heart disease for every test patient; `[:, 1]` keeps the second column of `predict_proba`.
    """)
    return


@app.cell
def _(X_test, logreg):
    # Probability of heart disease for every test patient
    logreg_prob = logreg.predict_proba(X_test)[:, 1]
    logreg_prob
    return (logreg_prob,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *A lower threshold flags more patients, so it **catches more heart disease but raises more false alarms**. A higher threshold does the opposite.* Use the slider to choose a threshold; at 0.5 the results match the ones above.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Slider for the threshold
    threshold_slider = mo.ui.slider(steps=[round(0.05 * i, 2) for i in range(1, 20)], value=0.5, label="Threshold", show_value=True)
    threshold_slider
    return (threshold_slider,)


@app.cell
def _(confusion_matrix, logreg_prob, threshold_slider, y_test):
    # Flag every test patient whose probability is at least the threshold, then count the four groups
    threshold_pred = logreg_prob >= threshold_slider.value
    threshold_confusion = confusion_matrix(y_test, threshold_pred)
    return (threshold_confusion,)


@app.cell(hide_code=True)
def _(mo, threshold_confusion):
    mo.md(rf"""
    | | Predicted no | Predicted yes |
    |---|---|---|
    | **Actually no** | {threshold_confusion[0][0]} true negatives | {threshold_confusion[0][1]} false positives |
    | **Actually yes** | {threshold_confusion[1][0]} false negatives | {threshold_confusion[1][1]} true positives |
    """)
    return


@app.cell
def _(threshold_confusion):
    # The four metrics at this threshold
    threshold_sensitivity = threshold_confusion[1][1] / (threshold_confusion[1][0] + threshold_confusion[1][1])
    threshold_specificity = threshold_confusion[0][0] / (threshold_confusion[0][0] + threshold_confusion[0][1])
    threshold_precision = threshold_confusion[1][1] / (threshold_confusion[0][1] + threshold_confusion[1][1])
    threshold_fpr = threshold_confusion[0][1] / (threshold_confusion[0][0] + threshold_confusion[0][1])
    return (
        threshold_fpr,
        threshold_precision,
        threshold_sensitivity,
        threshold_specificity,
    )


@app.cell(hide_code=True)
def _(
    mo,
    threshold_fpr,
    threshold_precision,
    threshold_sensitivity,
    threshold_specificity,
):
    mo.md(rf"""
    | Metric | Value |
    |---|---|
    | Sensitivity | {threshold_sensitivity:.2f} |
    | Specificity | {threshold_specificity:.2f} |
    | Precision | {threshold_precision:.2f} |
    | False positive rate | {threshold_fpr:.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ROC Curve
    *The **ROC curve** shows **every threshold at once**. Each threshold gives one point: its false positive rate across and its sensitivity (true positive rate) up.* `roc_curve` calculates both rates for every threshold.
    """)
    return


@app.cell
def _(logreg_prob, roc_curve, y_test):
    # False positive rate and sensitivity for every threshold
    roc_fpr, roc_tpr, roc_thresholds = roc_curve(y_test, logreg_prob)
    return roc_fpr, roc_tpr


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *The curve joins the points. The dashed diagonal is **a model that guesses at random**,* and the red dot is the threshold chosen on the slider, which is the same slider as above.
    """)
    return


@app.cell(hide_code=True)
def _(threshold_slider):
    # The threshold slider again, next to the ROC curve
    threshold_slider
    return


@app.cell
def _(plt, roc_fpr, roc_tpr, sns, threshold_fpr, threshold_sensitivity):
    # ROC curve, the random-guessing diagonal, and the slider's threshold
    sns.lineplot(x=roc_fpr, y=roc_tpr, estimator=None)
    sns.lineplot(x=[0, 1], y=[0, 1], linestyle="--", color="gray")
    sns.scatterplot(x=[threshold_fpr], y=[threshold_sensitivity], color="red", s=80, zorder=3)
    plt.xlabel("False positive rate")
    plt.ylabel("Sensitivity (true positive rate)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # AUROC
    *The **area under the ROC curve (AUROC)** sums up the whole curve in one number, from 0.5 for random guessing to 1 for a perfect model. It is **the chance that the model gives a randomly chosen patient with heart disease a higher probability** than a randomly chosen patient without.* `roc_auc_score` calculates it.
    """)
    return


@app.cell
def _(logreg_prob, roc_auc_score, y_test):
    # Area under the ROC curve
    roc_auc_score(y_test, logreg_prob)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For **about 90%** of the pairs of one test patient with heart disease and one without, the model gives the patient with heart disease the higher probability.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Comparing the Models
    *To compare models fairly, we score every model on **the same test patients in the same way**.* We predict with kNN and the decision tree as we did with logistic regression.
    """)
    return


@app.cell
def _(X_test, knn, tree):
    # Predictions and probabilities of heart disease for every test patient
    knn_pred = knn.predict(X_test)
    knn_prob = knn.predict_proba(X_test)[:, 1]
    tree_pred = tree.predict(X_test)
    tree_prob = tree.predict_proba(X_test)[:, 1]
    return knn_pred, knn_prob, tree_pred, tree_prob


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Each model's confusion matrix gives its metrics at the default threshold of 0.5.
    """)
    return


@app.cell
def _(confusion_matrix, knn_pred, tree_pred, y_test):
    # Confusion matrices for kNN and the decision tree
    knn_confusion = confusion_matrix(y_test, knn_pred)
    tree_confusion = confusion_matrix(y_test, tree_pred)
    return knn_confusion, tree_confusion


@app.cell(hide_code=True)
def _(confusion, knn_confusion, mo, tree_confusion):
    def _row(name, c):
        return (
            f"| {name} | {(c[0][0] + c[1][1]) / c.sum():.2f} | {c[1][1] / (c[1][0] + c[1][1]):.2f} | "
            f"{c[0][0] / (c[0][0] + c[0][1]):.2f} | {c[1][1] / (c[0][1] + c[1][1]):.2f} | {c[0][1] / (c[0][0] + c[0][1]):.2f} |"
        )

    mo.md(
        "| Model | Accuracy | Sensitivity | Specificity | Precision | False positive rate |\n"
        "|---|---|---|---|---|---|\n"
        + _row("Logistic regression", confusion) + "\n"
        + _row("kNN", knn_confusion) + "\n"
        + _row("Decision tree", tree_confusion)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All three models get 81 or 82 of the 100 test patients right, but **they catch different numbers of the 30 patients with heart disease**: 20 for logistic regression, 16 for kNN and 18 for the decision tree.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ROC Curves for Each Model
    These metrics use one threshold. *Drawing each model's ROC curve on the same plot compares them **across every threshold**.*
    """)
    return


@app.cell
def _(knn_prob, plt, roc_curve, roc_fpr, roc_tpr, sns, tree_prob, y_test):
    # One ROC curve per model, plus the random-guessing diagonal
    knn_fpr, knn_tpr, knn_thresholds = roc_curve(y_test, knn_prob)
    tree_fpr, tree_tpr, tree_thresholds = roc_curve(y_test, tree_prob)
    sns.lineplot(x=roc_fpr, y=roc_tpr, estimator=None, label="Logistic regression")
    sns.lineplot(x=knn_fpr, y=knn_tpr, estimator=None, label="kNN")
    sns.lineplot(x=tree_fpr, y=tree_tpr, estimator=None, label="Decision tree")
    sns.lineplot(x=[0, 1], y=[0, 1], linestyle="--", color="gray")
    plt.xlabel("False positive rate")
    plt.ylabel("Sensitivity (true positive rate)")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *A curve **closer to the top left corner is better**: at the same false positive rate, it catches more patients with heart disease.* All three curves are well above the dashed diagonal, so every model does much better than guessing. At the lowest false positive rates the curves are close, so there the choice of model matters little. Once we want to catch most patients with heart disease, **logistic regression's curve is highest**, so it gets there with the fewest false alarms: to catch 80% of the patients with heart disease, it raises a false alarm for 19% of the patients without it, compared with 47% for kNN and 31% for the decision tree.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # AUROC for Each Model
    """)
    return


@app.cell(hide_code=True)
def _(knn_prob, logreg_prob, mo, roc_auc_score, tree_prob, y_test):
    mo.md(rf"""
    | Model | AUROC |
    |---|---|
    | Logistic regression | {roc_auc_score(y_test, logreg_prob):.2f} |
    | kNN | {roc_auc_score(y_test, knn_prob):.2f} |
    | Decision tree | {roc_auc_score(y_test, tree_prob):.2f} |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Logistic regression has the highest AUROC, 0.90**, so it ranks the test patients best, followed by the decision tree at 0.84 and kNN at 0.82. The order matches the ROC curves: *the higher a curve, the larger the area under it*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Choosing a Model
    *Each model suits different situations. On a new problem, it is worth trying more than one and **comparing them fairly on the same test patients**.*

    - ***Logistic regression** is a good first choice. It works well when the chance of the outcome **rises or falls steadily** with each predictor, it needs little data, and its coefficients show **the direction and strength of each predictor**. It cannot follow a boundary that curves or has islands.*
    - ***kNN** suits a boundary with **curves or small groups**, as long as there are plenty of training patients. Because it measures distance, it needs the predictors on **similar scales**, and the choice of k matters. It gives no simple summary of why it made a prediction.*
    - ***A decision tree** gives **rules a person can follow**, such as "cholesterol above 219.5 and blood pressure above 132.5", and handles predictors on any scale. A deep tree **memorizes the training set**, so its depth needs to be limited.*

    On these patients, logistic regression ranked the test patients best, because the chance of heart disease rises steadily with cholesterol and blood pressure.
    """)
    return


if __name__ == "__main__":
    app.run()
