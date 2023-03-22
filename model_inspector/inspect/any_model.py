# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00_any_model.ipynb.

# %% auto 0
__all__ = ['_Inspector']

# %% ../../nbs/00_any_model.ipynb 3
from typing import Optional
import warnings

import pandas as pd
from fastcore.basics import basic_repr, store_attr
from matplotlib.axes import Axes
from numpy.typing import NDArray
from sklearn.base import BaseEstimator
import sklearn.inspection
from sklearn.utils import check_X_y
from sklearn.utils.validation import check_is_fitted

from ..delegate import delegates
from ..explore import plot_column_clusters, show_correlation

# %% ../../nbs/00_any_model.ipynb 4
class _Inspector:
    """Model inspector base class.

    Users should use `get_inspector` to generate appropriate
    `_Inspector` objects rather than instantiating this class or its
    subclasses directly.
    """

    def __init__(
        self,
        # We aim to support estimators with `scikit-learn`-compatible
        # interfaces from popular libraries such as `xgboost` and
        # `catboost` even if they do not inherit from `BaseEstimator`,
        # but I do not know of a simple way to include them in this type
        # hint without adding those libraries as dependencies, which I
        # would like to avoid if possible.
        model: BaseEstimator,
        X: pd.DataFrame,
        y: pd.Series,
    ):
        check_is_fitted(model)
        check_X_y(X, y)
        self._check_cols(model, X)

        store_attr()

    __repr__ = basic_repr(["model"])

    def _check_cols(self, model, X):
        try:
            if not model.feature_names_in_.equals(X.columns):
                raise ValueError("`model.feature_names_in_` should match `X.columns`")
        except AttributeError:
            warnings.warn(
                """`model` does not have the `feature_names_in_`
                attribute, so we cannot confirm that `model`'s feature
                names match `X`'s column names. Proceed at your own
                risk!
                """
            )
            try:
                if not model.n_features_in_ == len(X.columns):
                    raise ValueError(
                        "`model.n_features_in_` must equal `len(X.columns)`."
                    )
            except AttributeError:
                warnings.warn(
                    """`model` does not have the `n_features_in_`
                    attribute, so we cannot confirm that `X` has as many
                    columns as `model` has features. Proceed at your own
                    risk!"""
                )

    @delegates(sklearn.inspection.PartialDependenceDisplay.from_estimator)
    def plot_partial_dependence(self, **kwargs) -> NDArray[Axes]:
        """Plot partial dependence."""
        return sklearn.inspection.PartialDependenceDisplay.from_estimator(
            estimator=self.model, X=self.X, **kwargs
        ).axes_

    @delegates(sklearn.inspection.permutation_importance)
    def permutation_importance(
        self,
        sort: bool = True,
        **kwargs,
    ) -> pd.Series:
        """Calculate permutation importance.

        Parameters:

        - `sort`: Sort features by decreasing importance.
        """
        if kwargs is None:
            kwargs = {}
        kwargs = {**{"n_jobs": -1}, **kwargs}

        importances = pd.Series(
            sklearn.inspection.permutation_importance(
                self.model, self.X, self.y, **kwargs
            )["importances_mean"],
            index=self.X.columns,
        )
        if sort:
            importances = importances.sort_values(ascending=False)
        return importances

    def plot_permutation_importance(
        self,
        ax: Optional[Axes] = None,
        importance_kwargs: Optional[dict] = None,
        plot_kwargs: Optional[dict] = None,
    ) -> Axes:
        """Plot a correlation matrix for `self.X` and `self.y`.

        Parameters:

        - `ax`: Matplotlib `Axes` object. Plot will be added to this object
        if provided; otherwise a new `Axes` object will be generated.
        - `importance_kwargs`: kwargs to pass to
        `sklearn.inspection.permutation_importance`
        - `plot_kwargs`: kwargs to pass to `pd.Series.plot.barh`
        """
        if importance_kwargs is None:
            importance_kwargs = {}
        # reversing the order to compensate for `barh` reversing it
        importance = self.permutation_importance(**importance_kwargs).iloc[::-1]

        if plot_kwargs is None:
            plot_kwargs = {}
        ax = importance.plot.barh(**plot_kwargs)
        ax.set(title="Feature importances")
        ax.bar_label(ax.containers[0], fmt="%.2f")
        # extending plot on the right to accommodate labels
        ax.set_xlim((ax.get_xlim()[0], ax.get_xlim()[1] * 1.05))
        return ax

    @delegates(show_correlation)
    def show_correlation(self, **kwargs):
        """Show a correlation matrix for `self.X` and `self.y`.

        If output is not rendering properly when you reopen a notebook,
        make sure the notebook is trusted.
        """
        return show_correlation(
            df=pd.concat((self.X, self.y), axis="columns"),
            **kwargs,
        )

    @delegates(plot_column_clusters)
    def plot_feature_clusters(self, **kwargs) -> Axes:
        """Plot a dendrogram based on feature correlations.

        Parameters:

        - `corr_method`: Method of correlation to pass to `df.corr()`
        - `ax`: Matplotlib `Axes` object. Plot will be added to this object
        if provided; otherwise a new `Axes` object will be generated.
        """
        return plot_column_clusters(self.X, **kwargs)

    @property
    def methods(self):
        """Show available methods."""
        return [
            i
            for i in dir(self)
            if not i.startswith("__")
            and i not in self.__stored_args__
            and i != "methods"
        ]

# %% ../../nbs/00_any_model.ipynb 5
_all_ = ["_Inspector"]
