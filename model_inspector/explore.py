# AUTOGENERATED! DO NOT EDIT! File to edit: 02_explore.ipynb (unless otherwise specified).

__all__ = ['plot_correlation']

# Cell
from typing import Optional

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cell
def plot_correlation(df: pd.DataFrame, heatmap_kwargs=None, ax: Optional[Axes] = None):
    """Plot correlation heatmap

    Parameters:
    - `df`: DataFrame
    - `heatmap_kwargs`: kwargs to pass to `sns.heatmap`
    - `ax`: Matplotlib `Axes` object. Plot will be added to this object
    if provided; otherwise a new `Axes` object will be generated.
    """
    if ax is None:
        _, ax = plt.subplots()
    if heatmap_kwargs is None:
        kwargs = {
            "cmap": sns.diverging_palette(h_neg=220, h_pos=10, n=21),
            "annot": True,
        }
    return sns.heatmap(
        df.corr(),
        vmin=-1,
        vmax=1,
        ax=ax,
        **kwargs,
    )