# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/10_testing.ipynb.

# %% auto 0
__all__ = []

# %% ../../nbs/10_testing.ipynb 3
from typing import Any, Optional

import pandas as pd
import sklearn.inspection
from fastcore.basics import basic_repr, store_attr
from matplotlib.axes import Axes
from ..delegate import delegates
from ..explore import plot_column_clusters, show_correlation
from sklearn.base import BaseEstimator
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.utils import check_X_y
from sklearn.utils.validation import check_is_fitted

# %% ../../nbs/10_testing.ipynb 4
class _Test:

    def foo(self, x: Any) -> Any:
        """Foo.
        
        Parameters:
        
        - `x`: An x
        """
        return x