# AUTOGENERATED! DO NOT EDIT! File to edit: 02_explore.ipynb (unless otherwise specified).

__all__ = ['show_correlation', 'plot_column_clusters']

# Cell
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd
import scipy
import scipy.cluster.hierarchy as hc

from .delegate import delegates

# Cell
@delegates(pd.DataFrame().style.background_gradient)
def show_correlation(df: pd.DataFrame, method="pearson", **kwargs):
    """Show correlation heatmap

    Parameters:
    - `df`: DataFrame
    - `method`: Method of correlation to pass to `df.corr()`
    """
    kwargs = {**{"cmap": "bwr", "vmin": -1, "vmax": 1}, **kwargs}
    return df.corr(method=method).style.background_gradient(**kwargs).format("{0:,.2f}")

# Cell
@delegates(hc.dendrogram)
def plot_column_clusters(
    df, corr_method: str = "spearman", ax: Axes = None, **kwargs
) -> Axes:
    """Plot a dendrogram based on column correlations

    Parameters:
    - `df`: DataFrame
    - `corr_method`: Method of correlation to pass to `df.corr()`
    - `ax`: Matplotlib `Axes` object. Plot will be added to this object
    if provided; otherwise a new `Axes` object will be generated.

    Adapted from https://github.com/fastai/book_nbs/blob/master/utils.py
    """
    corr_matrix = df.corr(method=corr_method)
    corr_squareform = hc.distance.squareform(1 - corr_matrix)
    z = hc.linkage(corr_squareform, method="average")

    if ax is None:
        fig, ax = plt.subplots()
    if kwargs is None:
        kwargs = {}
    kwargs = {**kwargs, **{"orientation": "left", "leaf_font_size": 12}}

    hc.dendrogram(z, labels=df.columns, ax=ax, **kwargs)
    return ax