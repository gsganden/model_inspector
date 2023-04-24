# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/06_classifier.ipynb.

# %% auto 0
__all__ = ['_BinInspector', '_MultiInspector']

# %% ../../nbs/06_classifier.ipynb 3
from typing import Callable, Optional, Sequence, Union

import numpy as np
import pandas as pd
import sklearn

from matplotlib.axes import Axes
from ..delegate import delegates
from .any_model import _Inspector
from model_inspector.tune import (
    calculate_metrics_by_thresh_binary,
    calculate_metrics_by_thresh_multi,
    calculate_pr_curve,
    plot_pr_curve,
    confusion_matrix,
)

# %% ../../nbs/06_classifier.ipynb 4
class _ClasInspector(_Inspector):
    """Abstract class for classification model inspectors"""

    def calculate_metrics_by_thresh(*args, **kwargs):
        raise NotImplementedError()

    def confusion_matrix(*args, **kwargs):
        raise NotImplementedError()

# %% ../../nbs/06_classifier.ipynb 6
class _BinInspector(_ClasInspector):
    """Binary classification model inspector"""

    def calculate_metrics_by_thresh(
        self,
        metrics: Union[Callable, Sequence[Callable]],
        thresholds: Optional[Sequence] = None,
    ) -> pd.DataFrame:
        """Calculate classification metrics as a function of threshold

        Assumes that `self.model` has a `.predict_proba()` method. Uses
        `self.y` as ground-truth values,
        `self.model.predict_proba(self.X)[:, 1] > thresh` as
        predictions.

        Parameters:

        - `metrics`: Callables that take `y_true`, `y_pred` as
        positional arguments and return a number. Must have a `__name__`
        attribute.
        - `thresholds`: `Sequence` of `float` threshold values to use. By
        default uses `0` and the values that appear in `y_prob[:, 1]`, which
        is a minimal set that covers all of the relevant possibilities. One
        reason to override that default would be to save time with a large
        dataset.

        Returns: `DataFrame` with one column "thresh" indicating the
        thresholds used and an additional column for each input metric
        giving the value of that metric at that threshold.
        """
        return calculate_metrics_by_thresh_binary(
            y_true=self.y,
            y_prob=self.model.predict_proba(self.X),
            metrics=metrics,
            thresholds=thresholds,
        )

    def calculate_pr_curve(
        self,
        thresholds: Optional[Sequence] = None,
    ) -> pd.DataFrame:
        """Compute the precision-recall curve for a binary classification
        problem.

        Assumes that `self.model` has a `.predict_proba()` method. Uses
        `self.y` as ground-truth values,
        `self.model.predict_proba(self.X)[:, 1] > thresh` as
        predictions.

        Parameters:

        - `thresholds`: `Sequence` of `float` threshold values to use. By
        default uses the values that appear in `y_prob[:, 1]`, which is a
        minimal set that covers all of the relevant possibilities. One
        reason to override that default would be to save time with a large
        dataset.

        Returns: Pandas DataFrame with two columns: `recall_score` and
        `precision_score`. Each row represents a point on the
        precision-recall curve, and the DataFrame is sorted by increasing
        `recall_score`.

        Raises:

        - `ValueError`: If the shapes of y_true and y_prob do not match.
        """
        return calculate_pr_curve(
            y_true=self.y,
            y_prob=self.model.predict_proba(self.X),
            thresholds=thresholds,
        )

    def plot_pr_curve(
        self,
        thresholds: Optional[Sequence] = None,
        ax: Optional[Axes] = None,
    ) -> Axes:
        """
        Compute and plot the precision-recall curve for a binary classification
        problem.

        Parameters:

        - `thresholds`: `Sequence` of `float` threshold values to use. By
        default uses the values that appear in `y_prob[:, 1]`, which is a
        minimal set that covers all of the relevant possibilities. One
        reason to override that default would be to save time with a large
        dataset.
        - `ax`: Matplotlib `Axes` object. Plot will be added to this object
        if provided; otherwise a new `Axes` object will be generated.

        Returns: Matplotlib `Axes` object.
        """
        return plot_pr_curve(
            y_true=self.y,
            y_prob=self.model.predict_proba(self.X),
            thresholds=thresholds,
            ax=ax,
        )

    @delegates(sklearn.metrics.confusion_matrix)
    def confusion_matrix(
        self,
        thresh: float = 0.5,
        **kwargs,
    ) -> pd.DataFrame:
        """Get confusion matrix

        Assumes that `self.model` has a `.predict_proba()` method. Uses
        `self.y` as ground-truth values,
        `self.model.predict_proba(self.X)[:, 1] > thresh` as
        predictions.

        If output is not rendering properly when you reopen a notebook,
        make sure the notebook is trusted.

        Parameters:

        - `thresh`: Probability threshold for counting a prediction as
        positive
        """
        labels = np.unique(self.y)
        return confusion_matrix(
            y_true=self.y,
            y_pred=np.where(
                self.model.predict_proba(self.X)[:, 1] > thresh, labels[1], labels[0]
            ),
            **kwargs,
        )

# %% ../../nbs/06_classifier.ipynb 26
class _MultiInspector(_ClasInspector):
    """Multiclass model inspector"""

    def calculate_metrics_by_thresh(
        self,
        metrics: Union[Callable, Sequence[Callable]],
        thresholds: Optional[Sequence] = None,
    ) -> pd.DataFrame:
        """Calculate classification metrics as a function of threshold

        Assumes that `self.model` has a `.predict_proba()` method. Uses
        `self.y` as ground-truth values, uses the value with the highest
        probability as the prediction if that probability exceeds the
        threshold, `np.nan` otherwise.

        Parameters:

        - `metrics`: Callables that take `y_true`, `y_pred` as
        positional arguments and return a number. Must have a `__name__`
        attribute and must be able to handle `np.nan` values.
        - `thresholds`: `Sequence` of `float` threshold values to use. By
        default uses 0 and all values that appear in `y_prob`, which is a
        minimal set that covers all of the relevant possibilities. One
        reason to override that default would be to save time with a large
        dataset.

        Returns: DataFrame with one column "thresh" indicating the
        thresholds used and an additional column for each input metric
        giving the value of that metric at that threshold.
        """
        return calculate_metrics_by_thresh_multi(
            y_true=self.y,
            y_prob=self.model.predict_proba(self.X),
            metrics=metrics,
        )

    @delegates(pd.DataFrame().style.background_gradient)
    def confusion_matrix(
        self,
        **kwargs,
    ) -> pd.DataFrame:
        """Get confusion matrix

        Uses `self.y` as ground-truth values,
        `self.model.predict(self.X)` as predictions.

        If output is not rendering properly when you reopen a notebook,
        make sure the notebook is trusted.
        """

        return confusion_matrix(
            y_true=self.y,
            y_pred=self.model.predict(self.X),
            **kwargs,
        )

# %% ../../nbs/06_classifier.ipynb 35
_all_ = ["_BinInspector", "_MultiInspector"]
