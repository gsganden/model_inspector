# AUTOGENERATED! DO NOT EDIT! File to edit: 00_inspect.ipynb (unless otherwise specified).

__all__ = ['generate_linear_model_html', 'generate_logistic_model_html']

# Cell
from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np

# Cell
def generate_linear_model_html(
    model,
    feature_names: Iterable[str],
    target_name: str,
    intercept_formatter: str = ".2f",
    coef_formatter: str = ".2f",
):
    """Generate an HTML equation that characterizes a linear model.

    Model components are color-coded as follows:
    - target: red
    - intercept: purple
    - coefficients: green
    - features: blue

    Parameters:
    - `model`: fitted scikit-learn linear model of the form
    `y = b0 + b1 * x1 + ...`.
    - `feature_names`: feature names in the order in which they were
    given to the model.
    - `target_name` : Name of target variable `y`
    - `intercept_formatter`: Format specifier for model intercept
    - `coef_formatter`: Format specifier for model coefficients
    """
    if len(model.coef_) != len(feature_names):
        raise ValueError("len(model.coef_) != len(feature_cols)")
    model_string = f"""
        <span style='color:red'>{target_name}</span>
        = <span style='color:purple'>{model.intercept_:{intercept_formatter}}</span>
    """
    for coef, feature_col in zip(model.coef_, feature_names):
        model_string += f"""
            <span style='color:green'>{"+" if coef >= 0 else "-"} {abs(coef):{coef_formatter}}</span>
            * <span style='color:blue'>{feature_col}</span>
        """
    return model_string

# Cell
def generate_logistic_model_html(
    model,
    feature_names: Iterable[str],
    target_val_names: Iterable[str],
    intercept_formatter: str = ".2f",
    coef_formatter: str = ".2f",
):
    """Generate an HTML equation that characterizes a logistic
    regression model.

    Model components are color-coded as follows:
    - target: red
    - intercept: purple
    - coefficients: green
    - features: blue

    Parameters:
    - `model`: fitted scikit-learn linear model of the form
    `log-odds(y) = b0 + b1 * x1 + ...`.
    - `feature_names`: feature names in the order in which they were
    given to the model.
    - `target_val_names`: Names of the values of the target variable
    - `intercept_formatter`: Format specifier for model intercept
    - `coef_formatter`: Format specifier for model coefficients
    """
    for coefs in model.coef_:
        if len(coefs) != len(feature_names):
            raise ValueError("len(model.coef_) != len(feature_cols)")
    model_string = "<p>"
    for target_name, coefs, intercept in zip(
        target_val_names, model.coef_, model.intercept_
    ):
        model_string += f"""
            <span style='color:red'>log-odds({target_name})</span>
            = <span style='color:purple'>{intercept:{intercept_formatter}}</span>
        """
        for coef, feature_col in zip(coefs, feature_names):
            model_string += f"""
                <span style='color:green'>{"+" if coef >= 0 else "-"} {abs(coef):{coef_formatter}}</span>
                * <span style='color:blue'>{feature_col}</span>
            """
        model_string += "</p>"
    return model_string