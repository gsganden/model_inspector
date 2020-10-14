# Model Inspector
> Inspect machine learning models


## Install

`pip install model_inspector`

## How to Use

Example:

```python
from IPython.display import HTML
import sklearn.datasets
from sklearn.linear_model import LinearRegression

from model_inspector.sklearn import generate_linear_model_html
```

```python
diabetes = sklearn.datasets.load_diabetes()
X, y = diabetes["data"], diabetes["target"]

HTML(
    generate_linear_model_html(
        model=LinearRegression().fit(X, y),
        feature_names=diabetes["feature_names"],
        target_name="progression",
    )
)
```





<span style='color:red'>progression</span>
= <span style='color:purple'>152.13</span>

    <span style='color:green'>- 10.01</span>
    * <span style='color:blue'>age</span>

    <span style='color:green'>- 239.82</span>
    * <span style='color:blue'>sex</span>

    <span style='color:green'>+ 519.84</span>
    * <span style='color:blue'>bmi</span>

    <span style='color:green'>+ 324.39</span>
    * <span style='color:blue'>bp</span>

    <span style='color:green'>- 792.18</span>
    * <span style='color:blue'>s1</span>

    <span style='color:green'>+ 476.75</span>
    * <span style='color:blue'>s2</span>

    <span style='color:green'>+ 101.04</span>
    * <span style='color:blue'>s3</span>

    <span style='color:green'>+ 177.06</span>
    * <span style='color:blue'>s4</span>

    <span style='color:green'>+ 751.28</span>
    * <span style='color:blue'>s5</span>

    <span style='color:green'>+ 67.63</span>
    * <span style='color:blue'>s6</span>




```python
HTML(
    generate_linear_model_html(
        LinearRegression().fit(X, y), diabetes["feature_names"], "progression"
    )
)
```





<span style='color:red'>progression</span>
= <span style='color:purple'>152.13</span>

    <span style='color:green'>- 10.01</span>
    * <span style='color:blue'>age</span>

    <span style='color:green'>- 239.82</span>
    * <span style='color:blue'>sex</span>

    <span style='color:green'>+ 519.84</span>
    * <span style='color:blue'>bmi</span>

    <span style='color:green'>+ 324.39</span>
    * <span style='color:blue'>bp</span>

    <span style='color:green'>- 792.18</span>
    * <span style='color:blue'>s1</span>

    <span style='color:green'>+ 476.75</span>
    * <span style='color:blue'>s2</span>

    <span style='color:green'>+ 101.04</span>
    * <span style='color:blue'>s3</span>

    <span style='color:green'>+ 177.06</span>
    * <span style='color:blue'>s4</span>

    <span style='color:green'>+ 751.28</span>
    * <span style='color:blue'>s5</span>

    <span style='color:green'>+ 67.63</span>
    * <span style='color:blue'>s6</span>




The library also supports logistic regression with `model_inspector.sklearn.generate_logistic_model_html`.
