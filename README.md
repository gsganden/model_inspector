Model Inspector
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

`model_inspector` aims to help you train better `scikit-learn` models by
providing insights into their behavior.

## Use

To use `model_inspector`, you create an `Inspector` object from a
`scikit-learn` model, a feature DataFrame `X`, and a target Series `y`.
Typically you will want to create it on held-out data, as shown below.

``` python
import sklearn.datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from model_inspector import get_inspector
```

``` python
X, y = sklearn.datasets.load_diabetes(return_X_y=True, as_frame=True)
```

``` python
X
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>bp</th>
      <th>s1</th>
      <th>s2</th>
      <th>s3</th>
      <th>s4</th>
      <th>s5</th>
      <th>s6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.038076</td>
      <td>0.050680</td>
      <td>0.061696</td>
      <td>0.021872</td>
      <td>-0.044223</td>
      <td>-0.034821</td>
      <td>-0.043401</td>
      <td>-0.002592</td>
      <td>0.019907</td>
      <td>-0.017646</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.001882</td>
      <td>-0.044642</td>
      <td>-0.051474</td>
      <td>-0.026328</td>
      <td>-0.008449</td>
      <td>-0.019163</td>
      <td>0.074412</td>
      <td>-0.039493</td>
      <td>-0.068332</td>
      <td>-0.092204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.085299</td>
      <td>0.050680</td>
      <td>0.044451</td>
      <td>-0.005670</td>
      <td>-0.045599</td>
      <td>-0.034194</td>
      <td>-0.032356</td>
      <td>-0.002592</td>
      <td>0.002861</td>
      <td>-0.025930</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.089063</td>
      <td>-0.044642</td>
      <td>-0.011595</td>
      <td>-0.036656</td>
      <td>0.012191</td>
      <td>0.024991</td>
      <td>-0.036038</td>
      <td>0.034309</td>
      <td>0.022688</td>
      <td>-0.009362</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.005383</td>
      <td>-0.044642</td>
      <td>-0.036385</td>
      <td>0.021872</td>
      <td>0.003935</td>
      <td>0.015596</td>
      <td>0.008142</td>
      <td>-0.002592</td>
      <td>-0.031988</td>
      <td>-0.046641</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>437</th>
      <td>0.041708</td>
      <td>0.050680</td>
      <td>0.019662</td>
      <td>0.059744</td>
      <td>-0.005697</td>
      <td>-0.002566</td>
      <td>-0.028674</td>
      <td>-0.002592</td>
      <td>0.031193</td>
      <td>0.007207</td>
    </tr>
    <tr>
      <th>438</th>
      <td>-0.005515</td>
      <td>0.050680</td>
      <td>-0.015906</td>
      <td>-0.067642</td>
      <td>0.049341</td>
      <td>0.079165</td>
      <td>-0.028674</td>
      <td>0.034309</td>
      <td>-0.018114</td>
      <td>0.044485</td>
    </tr>
    <tr>
      <th>439</th>
      <td>0.041708</td>
      <td>0.050680</td>
      <td>-0.015906</td>
      <td>0.017293</td>
      <td>-0.037344</td>
      <td>-0.013840</td>
      <td>-0.024993</td>
      <td>-0.011080</td>
      <td>-0.046883</td>
      <td>0.015491</td>
    </tr>
    <tr>
      <th>440</th>
      <td>-0.045472</td>
      <td>-0.044642</td>
      <td>0.039062</td>
      <td>0.001215</td>
      <td>0.016318</td>
      <td>0.015283</td>
      <td>-0.028674</td>
      <td>0.026560</td>
      <td>0.044529</td>
      <td>-0.025930</td>
    </tr>
    <tr>
      <th>441</th>
      <td>-0.045472</td>
      <td>-0.044642</td>
      <td>-0.073030</td>
      <td>-0.081413</td>
      <td>0.083740</td>
      <td>0.027809</td>
      <td>0.173816</td>
      <td>-0.039493</td>
      <td>-0.004222</td>
      <td>0.003064</td>
    </tr>
  </tbody>
</table>
<p>442 rows × 10 columns</p>
</div>

``` python
y
```

    0      151.0
    1       75.0
    2      141.0
    3      206.0
    4      135.0
           ...  
    437    178.0
    438    104.0
    439    132.0
    440    220.0
    441     57.0
    Name: target, Length: 442, dtype: float64

``` python
X_train, X_test, y_train, y_test = train_test_split(X, y)
```

``` python
rfr = RandomForestRegressor().fit(X_train, y_train)
```

``` python
rfr.score(X_test, y_test)
```

    0.4145806969881506

``` python
inspector = get_inspector(rfr, X_test, y_test)
```

You can then use various methods of `inspector` to learn about how your
model behaves on that data.

The methods that are available for a given inspector depends on the
types of its estimator and its target `y`. An attribute called `methods`
tells you what they are:

``` python
inspector.methods
```

    ['plot_feature_clusters',
     'plot_partial_dependence',
     'permutation_importance',
     'plot_permutation_importance',
     'plot_pred_vs_act',
     'plot_residuals',
     'show_correlation']

``` python
most_important_features = inspector.permutation_importance().index[:2]
axes = inspector.plot_partial_dependence(
    features=[*most_important_features, most_important_features]
)
axes[0, 0].get_figure().set_size_inches(12, 3)
```

![](index_files/figure-commonmark/cell-11-output-1.png)

``` python
inspector.show_correlation()
```

<style type="text/css">
#T_c8180_row0_col0, #T_c8180_row1_col1, #T_c8180_row2_col2, #T_c8180_row3_col3, #T_c8180_row4_col4, #T_c8180_row5_col5, #T_c8180_row6_col6, #T_c8180_row7_col7, #T_c8180_row8_col8, #T_c8180_row9_col9, #T_c8180_row10_col10 {
  background-color: #ff0000;
  color: #f1f1f1;
}
#T_c8180_row0_col1, #T_c8180_row1_col0 {
  background-color: #ffc6c6;
  color: #000000;
}
#T_c8180_row0_col2, #T_c8180_row0_col5, #T_c8180_row2_col0, #T_c8180_row5_col0, #T_c8180_row5_col9, #T_c8180_row9_col5 {
  background-color: #ffd2d2;
  color: #000000;
}
#T_c8180_row0_col3, #T_c8180_row2_col5, #T_c8180_row3_col0, #T_c8180_row5_col2 {
  background-color: #ffd0d0;
  color: #000000;
}
#T_c8180_row0_col4, #T_c8180_row4_col0 {
  background-color: #ffc4c4;
  color: #000000;
}
#T_c8180_row0_col6, #T_c8180_row6_col0 {
  background-color: #f4f4ff;
  color: #000000;
}
#T_c8180_row0_col7, #T_c8180_row3_col7, #T_c8180_row7_col0, #T_c8180_row7_col3 {
  background-color: #ffcece;
  color: #000000;
}
#T_c8180_row0_col8, #T_c8180_row8_col0 {
  background-color: #ffb6b6;
  color: #000000;
}
#T_c8180_row0_col9, #T_c8180_row9_col0 {
  background-color: #ffaeae;
  color: #000000;
}
#T_c8180_row0_col10, #T_c8180_row1_col8, #T_c8180_row8_col1, #T_c8180_row10_col0 {
  background-color: #ffdede;
  color: #000000;
}
#T_c8180_row1_col2, #T_c8180_row1_col7, #T_c8180_row2_col1, #T_c8180_row7_col1 {
  background-color: #ffb4b4;
  color: #000000;
}
#T_c8180_row1_col3, #T_c8180_row3_col1 {
  background-color: #ffb0b0;
  color: #000000;
}
#T_c8180_row1_col4, #T_c8180_row4_col1 {
  background-color: #f2f2ff;
  color: #000000;
}
#T_c8180_row1_col5, #T_c8180_row5_col1 {
  background-color: #ffeaea;
  color: #000000;
}
#T_c8180_row1_col6, #T_c8180_row6_col1 {
  background-color: #9898ff;
  color: #f1f1f1;
}
#T_c8180_row1_col9, #T_c8180_row9_col1 {
  background-color: #ffb8b8;
  color: #000000;
}
#T_c8180_row1_col10, #T_c8180_row10_col1 {
  background-color: #ffbaba;
  color: #000000;
}
#T_c8180_row2_col3, #T_c8180_row3_col2 {
  background-color: #ff7272;
  color: #f1f1f1;
}
#T_c8180_row2_col4, #T_c8180_row4_col2 {
  background-color: #ffd8d8;
  color: #000000;
}
#T_c8180_row2_col6, #T_c8180_row6_col2 {
  background-color: #9292ff;
  color: #f1f1f1;
}
#T_c8180_row2_col7, #T_c8180_row7_col2 {
  background-color: #ff8c8c;
  color: #000000;
}
#T_c8180_row2_col8, #T_c8180_row8_col2 {
  background-color: #ff9292;
  color: #000000;
}
#T_c8180_row2_col9, #T_c8180_row9_col2 {
  background-color: #ff8282;
  color: #f1f1f1;
}
#T_c8180_row2_col10, #T_c8180_row5_col7, #T_c8180_row7_col5, #T_c8180_row10_col2 {
  background-color: #ff5656;
  color: #f1f1f1;
}
#T_c8180_row3_col4, #T_c8180_row4_col3, #T_c8180_row4_col10, #T_c8180_row5_col10, #T_c8180_row10_col4, #T_c8180_row10_col5 {
  background-color: #ffe8e8;
  color: #000000;
}
#T_c8180_row3_col5, #T_c8180_row5_col3 {
  background-color: #fff6f6;
  color: #000000;
}
#T_c8180_row3_col6, #T_c8180_row6_col3 {
  background-color: #ccccff;
  color: #000000;
}
#T_c8180_row3_col8, #T_c8180_row8_col3 {
  background-color: #ffa2a2;
  color: #000000;
}
#T_c8180_row3_col9, #T_c8180_row9_col3 {
  background-color: #ff8e8e;
  color: #000000;
}
#T_c8180_row3_col10, #T_c8180_row10_col3 {
  background-color: #ff7c7c;
  color: #f1f1f1;
}
#T_c8180_row4_col5, #T_c8180_row5_col4 {
  background-color: #ff1e1e;
  color: #f1f1f1;
}
#T_c8180_row4_col6, #T_c8180_row6_col4 {
  background-color: #ffeeee;
  color: #000000;
}
#T_c8180_row4_col7, #T_c8180_row7_col4 {
  background-color: #ff6c6c;
  color: #f1f1f1;
}
#T_c8180_row4_col8, #T_c8180_row8_col4 {
  background-color: #ff7e7e;
  color: #f1f1f1;
}
#T_c8180_row4_col9, #T_c8180_row9_col4 {
  background-color: #ffbebe;
  color: #000000;
}
#T_c8180_row5_col6, #T_c8180_row6_col5 {
  background-color: #d6d6ff;
  color: #000000;
}
#T_c8180_row5_col8, #T_c8180_row8_col5 {
  background-color: #ffc2c2;
  color: #000000;
}
#T_c8180_row6_col7, #T_c8180_row7_col6 {
  background-color: #4646ff;
  color: #f1f1f1;
}
#T_c8180_row6_col8, #T_c8180_row8_col6 {
  background-color: #a0a0ff;
  color: #f1f1f1;
}
#T_c8180_row6_col9, #T_c8180_row9_col6 {
  background-color: #b4b4ff;
  color: #000000;
}
#T_c8180_row6_col10, #T_c8180_row10_col6 {
  background-color: #8a8aff;
  color: #f1f1f1;
}
#T_c8180_row7_col8, #T_c8180_row8_col7 {
  background-color: #ff6464;
  color: #f1f1f1;
}
#T_c8180_row7_col9, #T_c8180_row7_col10, #T_c8180_row9_col7, #T_c8180_row10_col7 {
  background-color: #ff9696;
  color: #000000;
}
#T_c8180_row8_col9, #T_c8180_row9_col8 {
  background-color: #ff7a7a;
  color: #f1f1f1;
}
#T_c8180_row8_col10, #T_c8180_row10_col8 {
  background-color: #ff8888;
  color: #f1f1f1;
}
#T_c8180_row9_col10, #T_c8180_row10_col9 {
  background-color: #ffa6a6;
  color: #000000;
}
</style>
<table id="T_c8180">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_c8180_level0_col0" class="col_heading level0 col0" >age</th>
      <th id="T_c8180_level0_col1" class="col_heading level0 col1" >sex</th>
      <th id="T_c8180_level0_col2" class="col_heading level0 col2" >bmi</th>
      <th id="T_c8180_level0_col3" class="col_heading level0 col3" >bp</th>
      <th id="T_c8180_level0_col4" class="col_heading level0 col4" >s1</th>
      <th id="T_c8180_level0_col5" class="col_heading level0 col5" >s2</th>
      <th id="T_c8180_level0_col6" class="col_heading level0 col6" >s3</th>
      <th id="T_c8180_level0_col7" class="col_heading level0 col7" >s4</th>
      <th id="T_c8180_level0_col8" class="col_heading level0 col8" >s5</th>
      <th id="T_c8180_level0_col9" class="col_heading level0 col9" >s6</th>
      <th id="T_c8180_level0_col10" class="col_heading level0 col10" >target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c8180_level0_row0" class="row_heading level0 row0" >age</th>
      <td id="T_c8180_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_c8180_row0_col1" class="data row0 col1" >0.22</td>
      <td id="T_c8180_row0_col2" class="data row0 col2" >0.18</td>
      <td id="T_c8180_row0_col3" class="data row0 col3" >0.19</td>
      <td id="T_c8180_row0_col4" class="data row0 col4" >0.23</td>
      <td id="T_c8180_row0_col5" class="data row0 col5" >0.18</td>
      <td id="T_c8180_row0_col6" class="data row0 col6" >-0.04</td>
      <td id="T_c8180_row0_col7" class="data row0 col7" >0.19</td>
      <td id="T_c8180_row0_col8" class="data row0 col8" >0.28</td>
      <td id="T_c8180_row0_col9" class="data row0 col9" >0.32</td>
      <td id="T_c8180_row0_col10" class="data row0 col10" >0.13</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row1" class="row_heading level0 row1" >sex</th>
      <td id="T_c8180_row1_col0" class="data row1 col0" >0.22</td>
      <td id="T_c8180_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_c8180_row1_col2" class="data row1 col2" >0.29</td>
      <td id="T_c8180_row1_col3" class="data row1 col3" >0.31</td>
      <td id="T_c8180_row1_col4" class="data row1 col4" >-0.05</td>
      <td id="T_c8180_row1_col5" class="data row1 col5" >0.08</td>
      <td id="T_c8180_row1_col6" class="data row1 col6" >-0.41</td>
      <td id="T_c8180_row1_col7" class="data row1 col7" >0.30</td>
      <td id="T_c8180_row1_col8" class="data row1 col8" >0.13</td>
      <td id="T_c8180_row1_col9" class="data row1 col9" >0.27</td>
      <td id="T_c8180_row1_col10" class="data row1 col10" >0.27</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row2" class="row_heading level0 row2" >bmi</th>
      <td id="T_c8180_row2_col0" class="data row2 col0" >0.18</td>
      <td id="T_c8180_row2_col1" class="data row2 col1" >0.29</td>
      <td id="T_c8180_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_c8180_row2_col3" class="data row2 col3" >0.55</td>
      <td id="T_c8180_row2_col4" class="data row2 col4" >0.16</td>
      <td id="T_c8180_row2_col5" class="data row2 col5" >0.18</td>
      <td id="T_c8180_row2_col6" class="data row2 col6" >-0.43</td>
      <td id="T_c8180_row2_col7" class="data row2 col7" >0.45</td>
      <td id="T_c8180_row2_col8" class="data row2 col8" >0.43</td>
      <td id="T_c8180_row2_col9" class="data row2 col9" >0.49</td>
      <td id="T_c8180_row2_col10" class="data row2 col10" >0.66</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row3" class="row_heading level0 row3" >bp</th>
      <td id="T_c8180_row3_col0" class="data row3 col0" >0.19</td>
      <td id="T_c8180_row3_col1" class="data row3 col1" >0.31</td>
      <td id="T_c8180_row3_col2" class="data row3 col2" >0.55</td>
      <td id="T_c8180_row3_col3" class="data row3 col3" >1.00</td>
      <td id="T_c8180_row3_col4" class="data row3 col4" >0.09</td>
      <td id="T_c8180_row3_col5" class="data row3 col5" >0.04</td>
      <td id="T_c8180_row3_col6" class="data row3 col6" >-0.20</td>
      <td id="T_c8180_row3_col7" class="data row3 col7" >0.19</td>
      <td id="T_c8180_row3_col8" class="data row3 col8" >0.36</td>
      <td id="T_c8180_row3_col9" class="data row3 col9" >0.44</td>
      <td id="T_c8180_row3_col10" class="data row3 col10" >0.51</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row4" class="row_heading level0 row4" >s1</th>
      <td id="T_c8180_row4_col0" class="data row4 col0" >0.23</td>
      <td id="T_c8180_row4_col1" class="data row4 col1" >-0.05</td>
      <td id="T_c8180_row4_col2" class="data row4 col2" >0.16</td>
      <td id="T_c8180_row4_col3" class="data row4 col3" >0.09</td>
      <td id="T_c8180_row4_col4" class="data row4 col4" >1.00</td>
      <td id="T_c8180_row4_col5" class="data row4 col5" >0.88</td>
      <td id="T_c8180_row4_col6" class="data row4 col6" >0.07</td>
      <td id="T_c8180_row4_col7" class="data row4 col7" >0.57</td>
      <td id="T_c8180_row4_col8" class="data row4 col8" >0.50</td>
      <td id="T_c8180_row4_col9" class="data row4 col9" >0.26</td>
      <td id="T_c8180_row4_col10" class="data row4 col10" >0.09</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row5" class="row_heading level0 row5" >s2</th>
      <td id="T_c8180_row5_col0" class="data row5 col0" >0.18</td>
      <td id="T_c8180_row5_col1" class="data row5 col1" >0.08</td>
      <td id="T_c8180_row5_col2" class="data row5 col2" >0.18</td>
      <td id="T_c8180_row5_col3" class="data row5 col3" >0.04</td>
      <td id="T_c8180_row5_col4" class="data row5 col4" >0.88</td>
      <td id="T_c8180_row5_col5" class="data row5 col5" >1.00</td>
      <td id="T_c8180_row5_col6" class="data row5 col6" >-0.16</td>
      <td id="T_c8180_row5_col7" class="data row5 col7" >0.66</td>
      <td id="T_c8180_row5_col8" class="data row5 col8" >0.23</td>
      <td id="T_c8180_row5_col9" class="data row5 col9" >0.18</td>
      <td id="T_c8180_row5_col10" class="data row5 col10" >0.09</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row6" class="row_heading level0 row6" >s3</th>
      <td id="T_c8180_row6_col0" class="data row6 col0" >-0.04</td>
      <td id="T_c8180_row6_col1" class="data row6 col1" >-0.41</td>
      <td id="T_c8180_row6_col2" class="data row6 col2" >-0.43</td>
      <td id="T_c8180_row6_col3" class="data row6 col3" >-0.20</td>
      <td id="T_c8180_row6_col4" class="data row6 col4" >0.07</td>
      <td id="T_c8180_row6_col5" class="data row6 col5" >-0.16</td>
      <td id="T_c8180_row6_col6" class="data row6 col6" >1.00</td>
      <td id="T_c8180_row6_col7" class="data row6 col7" >-0.72</td>
      <td id="T_c8180_row6_col8" class="data row6 col8" >-0.37</td>
      <td id="T_c8180_row6_col9" class="data row6 col9" >-0.30</td>
      <td id="T_c8180_row6_col10" class="data row6 col10" >-0.46</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row7" class="row_heading level0 row7" >s4</th>
      <td id="T_c8180_row7_col0" class="data row7 col0" >0.19</td>
      <td id="T_c8180_row7_col1" class="data row7 col1" >0.30</td>
      <td id="T_c8180_row7_col2" class="data row7 col2" >0.45</td>
      <td id="T_c8180_row7_col3" class="data row7 col3" >0.19</td>
      <td id="T_c8180_row7_col4" class="data row7 col4" >0.57</td>
      <td id="T_c8180_row7_col5" class="data row7 col5" >0.66</td>
      <td id="T_c8180_row7_col6" class="data row7 col6" >-0.72</td>
      <td id="T_c8180_row7_col7" class="data row7 col7" >1.00</td>
      <td id="T_c8180_row7_col8" class="data row7 col8" >0.60</td>
      <td id="T_c8180_row7_col9" class="data row7 col9" >0.41</td>
      <td id="T_c8180_row7_col10" class="data row7 col10" >0.41</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row8" class="row_heading level0 row8" >s5</th>
      <td id="T_c8180_row8_col0" class="data row8 col0" >0.28</td>
      <td id="T_c8180_row8_col1" class="data row8 col1" >0.13</td>
      <td id="T_c8180_row8_col2" class="data row8 col2" >0.43</td>
      <td id="T_c8180_row8_col3" class="data row8 col3" >0.36</td>
      <td id="T_c8180_row8_col4" class="data row8 col4" >0.50</td>
      <td id="T_c8180_row8_col5" class="data row8 col5" >0.23</td>
      <td id="T_c8180_row8_col6" class="data row8 col6" >-0.37</td>
      <td id="T_c8180_row8_col7" class="data row8 col7" >0.60</td>
      <td id="T_c8180_row8_col8" class="data row8 col8" >1.00</td>
      <td id="T_c8180_row8_col9" class="data row8 col9" >0.52</td>
      <td id="T_c8180_row8_col10" class="data row8 col10" >0.46</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row9" class="row_heading level0 row9" >s6</th>
      <td id="T_c8180_row9_col0" class="data row9 col0" >0.32</td>
      <td id="T_c8180_row9_col1" class="data row9 col1" >0.27</td>
      <td id="T_c8180_row9_col2" class="data row9 col2" >0.49</td>
      <td id="T_c8180_row9_col3" class="data row9 col3" >0.44</td>
      <td id="T_c8180_row9_col4" class="data row9 col4" >0.26</td>
      <td id="T_c8180_row9_col5" class="data row9 col5" >0.18</td>
      <td id="T_c8180_row9_col6" class="data row9 col6" >-0.30</td>
      <td id="T_c8180_row9_col7" class="data row9 col7" >0.41</td>
      <td id="T_c8180_row9_col8" class="data row9 col8" >0.52</td>
      <td id="T_c8180_row9_col9" class="data row9 col9" >1.00</td>
      <td id="T_c8180_row9_col10" class="data row9 col10" >0.35</td>
    </tr>
    <tr>
      <th id="T_c8180_level0_row10" class="row_heading level0 row10" >target</th>
      <td id="T_c8180_row10_col0" class="data row10 col0" >0.13</td>
      <td id="T_c8180_row10_col1" class="data row10 col1" >0.27</td>
      <td id="T_c8180_row10_col2" class="data row10 col2" >0.66</td>
      <td id="T_c8180_row10_col3" class="data row10 col3" >0.51</td>
      <td id="T_c8180_row10_col4" class="data row10 col4" >0.09</td>
      <td id="T_c8180_row10_col5" class="data row10 col5" >0.09</td>
      <td id="T_c8180_row10_col6" class="data row10 col6" >-0.46</td>
      <td id="T_c8180_row10_col7" class="data row10 col7" >0.41</td>
      <td id="T_c8180_row10_col8" class="data row10 col8" >0.46</td>
      <td id="T_c8180_row10_col9" class="data row10 col9" >0.35</td>
      <td id="T_c8180_row10_col10" class="data row10 col10" >1.00</td>
    </tr>
  </tbody>
</table>

``` python
inspector.permutation_importance()
```

    bmi    0.241886
    s5     0.153085
    sex    0.003250
    s3     0.000734
    bp     0.000461
    s4    -0.002687
    s2    -0.004366
    s1    -0.008953
    s6    -0.018925
    age   -0.022768
    dtype: float64

``` python
ax = inspector.plot_permutation_importance()
```

![](index_files/figure-commonmark/cell-14-output-1.png)

``` python
ax = inspector.plot_feature_clusters()
```

![](index_files/figure-commonmark/cell-15-output-1.png)

``` python
ax = inspector.plot_pred_vs_act()
```

![](index_files/figure-commonmark/cell-16-output-1.png)

``` python
axes = inspector.plot_residuals()
```

![](index_files/figure-commonmark/cell-17-output-1.png)

## Install

`pip install model_inspector`

## Alternatives

## Yellowbrick

[Yellowbrick](https://www.scikit-yb.org/en/latest/) is similar to Model
Inspector in that it provides tools for visualizing the behavior of
`scikit-learn` models.

The two libraries have different designs. Yellowbrick uses `Visualizer`
objects, each class of which corresponds to a single type of
visualization. The `Visualizer` interface is similar to the
`scikit-learn` transformer and estimator interfaces. In constrast,
`model_inspector` uses `Inspector` objects that bundle together a
`scikit-learn` model, an `X` feature DataFrame, and a `y` target Series.
The `Inspector` object does the work of identifying appropriate
visualization types for the specific model and dataset in question and
exposing corresponding methods, making it easy to visualize a given
model for a given dataset in a variety of ways.

Another fundamental difference is that Yellowbrick is framed as a
machine learning *visualization* library, while Model Inspector treats
visualization as just one approach to inspecting the behavior of machine
learning models.

## SHAP

[SHAP](https://github.com/slundberg/shap) is another library that
provides a set of tools for understanding the behavior of machine
learning models. It has a somewhat similar design to Model Inspector in
that it uses `Explainer` objects to provide access to methods that are
appropriate for a given model. It has broader scope than Model Inspector
in that it supports models from frameworks such as PyTorch and
TensorFlow. It has narrower scope in that it only implements methods
based on Shapley values.

## Acknowledgments

Many aspects of this library were inspired by [FastAI
courses](https://course.fast.ai/), including bundling together a model
with data in a class and providing certain specific visualization
methods such as feature importance bar plots, feature clusters
dendrograms, tree diagrams, waterfall plots, and partial dependence
plots. Its primary contribution is to make all of these methods
available in a single convenient interface.
