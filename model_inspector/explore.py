# AUTOGENERATED! DO NOT EDIT! File to edit: 02_explore.ipynb (unless otherwise specified).

__all__ = ['plot_correlation']

# Cell
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .delegate import delegates

# Cell
@delegates(sns.heatmap)
def plot_correlation(
    df: pd.DataFrame,
    cmap=sns.diverging_palette(h_neg=220, h_pos=10, n=21),
    annot=True,
    **kwargs
):
    """Plot correlation heatmap

    Parameters:
    - `df`: DataFrame
    """
    return sns.heatmap(
        df.corr(),
        vmin=-1,
        vmax=1,
        cmap=cmap,
        annot=annot,
        **kwargs,
    )