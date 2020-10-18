# AUTOGENERATED! DO NOT EDIT! File to edit: 01_tune.ipynb (unless otherwise specified).

__all__ = ['calculate_metrics_by_thresh', 'coverage', 'calculate_metric_ignoring_nan', 'fbeta']

# Cell
from collections import defaultdict
from functools import partial
from typing import Callable, Iterable, Optional, Sequence, Union

import numpy as np
import pandas as pd
from sklearn import metrics

# Cell
def calculate_metrics_by_thresh(
    y_true: np.array,
    y_prob: np.array,
    prob_to_pred: Union[str, Callable],
    metrics: Union[Callable, Sequence[Callable]],
) -> pd.DataFrame:
    """Calculate classification metrics as a function of threshold

    Parameters:
    - `y_true`: Ground-truth values
    - `y_prob`: Probability distributions
    - `prob_to_pred`: Callable that takes `y_prob` and `thresh` as positional
    arguments and returns `y_pred`
    - `metrics`: Callables that take `y_true`, `y_pred` as positional arguments
    and return a number. Must have a `__name__` attribute.

    Returns: DataFrame with one column "thresh" indicating the
    thresholds used, which is 0 and the sorted set of values that occur in
    `y_prob`, and an additional column for each input metric giving
    the value of that metric at that threshold.
    """
    if callable(metrics):
        metrics = [metrics]

    results = defaultdict(list)
    results["thresh"] = sorted(np.hstack([0, np.unique(y_prob)]))
    for thresh in results["thresh"]:
        y_pred = prob_to_pred(y_prob=y_prob, thresh=thresh)
        for metric in metrics:
            results[metric.__name__].append(metric(y_true, y_pred))

    return pd.DataFrame(results)

# Cell
def coverage(y_true: np.array, y_pred: np.array):
    """How often the model makes a prediction, where `np.nan` indicates
    abstaining from predicting.

    Parameters:
    - `y_true`: Ground-truth values
    - `y_pred`: Predicted values, possibly including `np.nan` to
    indicate abstraining from predicting
    """
    return (~np.isnan(y_pred)).mean()

# Cell
def calculate_metric_ignoring_nan(
    y_true: np.array, y_pred: np.array, metric: Callable, *args, **kwargs
):
    """Calculate `metric` ignoring `np.nan` predictions

    Parameters:
    - `y_true`: Ground-truth values
    - `y_pred`: Predicted values, possibly including `np.nan` to
    indicate abstraining from predicting
    - `metric`: Function that takes `y_true`, `y_pred` as keyword
    arguments

    Any additional arguments will be passed to `metric`
    """
    return metric(
        y_true=y_true[~np.isnan(y_pred)],
        y_pred=y_pred[~np.isnan(y_pred)],
        *args,
        **kwargs
    )

# Cell
def fbeta(precision: float, recall: float, beta: float = 1):
    weighted_mean_of_inverses = (
        1 / (1 + beta ** 2) * (1 / precision + beta ** 2 * 1 / recall)
    )
    weighted_harmonic_mean = 1 / weighted_mean_of_inverses
    return weighted_harmonic_mean