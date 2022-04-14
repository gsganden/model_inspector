# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_get_inspector.ipynb (unless otherwise specified).

__all__ = ['get_inspector']

# Cell
import pandas as pd
from .inspect.any_model import *
from .inspect.classifier import *
from .inspect.linear_model import *
from .inspect.regressor import *
from .inspect.searchcv_estimator import *
from .inspect.tree import *
from sklearn.base import BaseEstimator
from sklearn.linear_model._base import (
    LinearClassifierMixin,
    LinearModel,
    RegressorMixin,
)
from sklearn.model_selection._search import BaseSearchCV
from sklearn.tree import BaseDecisionTree
from sklearn.utils.multiclass import type_of_target

# Cell
def get_inspector(model: BaseEstimator, X: pd.DataFrame, y: pd.Series) -> _Inspector:
    """Get an appropriate inspector for your model and data

    Parameters:
    - `model`: Fitted sklearn model
    - `X`: Matrix with the same features `model` was trained on
    - `y`: Series with same length as `X` and same meaning as target
    values `model` was trained on
    """
    if isinstance(model, LinearModel):
        return _LinRegInspector(model, X, y)
    elif isinstance(model, LinearClassifierMixin):
        if type_of_target(y) == "binary":
            return _LinBinInspector(model, X, y)
        elif type_of_target(y) == "multiclass":
            return _LinMultiInspector(model, X, y)
    elif isinstance(model, BaseDecisionTree):
        # `type_of_target` can't reliably distinguish between continuous
        # and multiclass
        if isinstance(model, RegressorMixin):
            return _TreeRegInspector(model, X, y)
        elif type_of_target(y) == "binary":
            return _TreeBinInspector(model, X, y)
        elif type_of_target(y) == "multiclass":
            return _TreeMultiInspector(model, X, y)
    elif isinstance(model, BaseSearchCV):
        return _SearchCVInspector(model, X, y)
    # `type_of_target` can't reliably distinguish between continuous and
    # multiclass
    if isinstance(model, RegressorMixin):
        return _RegInspector(model, X, y)
    elif type_of_target(y) == "binary":
        return _BinInspector(model, X, y)
    elif type_of_target(y) == "multiclass":
        return _MultiInspector(model, X, y)
    else:
        return _Inspector(model, X, y)