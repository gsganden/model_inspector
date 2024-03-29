# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_explore.ipynb.

# %% auto 0
__all__ = ['show_correlation', 'plot_column_clusters']

# %% ../nbs/02_explore.ipynb 3
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as hc
from matplotlib.axes import Axes
from .delegate import delegates

# %% ../nbs/02_explore.ipynb 4
@delegates(pd.DataFrame().style.background_gradient)
def show_correlation(df: pd.DataFrame, method="pearson", **kwargs):
    """Show correlation heatmap

    If output is not rendering properly when you reopen a notebook, make
    sure the notebook is trusted.

    Parameters:

    - `df`: DataFrame
    - `method`: Method of correlation to pass to `df.corr()`
    """
    kwargs = {**{"cmap": "bwr", "vmin": -1, "vmax": 1}, **kwargs}
    return df.corr(method=method).style.background_gradient(**kwargs).format("{0:,.2f}")

# %% ../nbs/02_explore.ipynb 10
@delegates(hc.dendrogram)
def plot_column_clusters(
    df, corr_method: str = "spearman", ax: Axes = None, **kwargs
) -> Axes:
    """Plot a dendrogram based on column correlations

    If output is not rendering properly when you reopen a notebook, make
    sure the notebook is trusted.

    Adapted from
    [https://github.com/fastai/book_nbs/blob/master/utils.py#L58-L64](https://github.com/fastai/book_nbs/blob/master/utils.py#L58-L64)

    Parameters:

    - `df`: DataFrame
    - `corr_method`: Method of correlation to pass to `df.corr()`
    - `ax`: Matplotlib `Axes` object. Plot will be added to this object
    if provided; otherwise a new `Axes` object will be generated.
    """
    corr_matrix = df.corr(method=corr_method)
    # For the purpose of evaluating redundancy of features in a
    # predictive model, variables that are perfectly correlated or
    # anti-correlated should count as maximally close.
    # As of 2021-08-03,
    # https://github.com/fastai/book_nbs/blob/master/utils.py#L58-L64
    # does not take an absolute value, which I think is a mistake; see
    # https://forums.fast.ai/t/should-cluster-columns-use-absolute-value/90413
    distance_matrix = 1 - abs(corr_matrix)
    corr_squareform = hc.distance.squareform(distance_matrix)
    z = hc.linkage(corr_squareform, method="average")

    if ax is None:
        _, ax = plt.subplots()
    if kwargs is None:
        kwargs = {}
    kwargs = {**kwargs, **{"orientation": "left", "leaf_font_size": 12}}

    hc.dendrogram(z, labels=df.columns, ax=ax, **kwargs)
    return ax
