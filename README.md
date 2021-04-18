# Model Inspector
> Inspect machine learning models


See the [docs](https://gsganden.github.io/model_inspector/), especially for the [inspect module](https://gsganden.github.io/model_inspector/inspect.html), for API details and examples.

The most similar alternative to `model_inspector` that I am aware of is [`yellowbrick`](https://www.scikit-yb.org/en/latest/). Both are machine learning visualization libraries that work well with scikit-learn.

`yellowbrick` is designed around Visualizer objects. Each Visualizer corresponds to a single type of visualization. They have a similar interface to scikit-learn transformers and estimators.

`model_inspector` takes a different approach. It is designed around Inspector objects that bundle together a scikit-learn model, an `X` feature DataFrame, and a `y` target Series. The Inspector object does the work of identifying appropriate visualization types for the specific model and dataset in question and exposing corresponding methods, making it easy to visualize a given model for a given dataset in a variety of ways.

## Install

`pip install model_inspector`
