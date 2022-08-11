Model Inspector
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

`model_inspector` aims to help you train better `scikit-learn` models by
providing insights into their behavior.

## Use

To use `model_inspector`, you create an `Inspector` object from a
`scikit-learn` model, a feature DataFrame `X`, and a target Series `y`,
as illustrated below.

``` python
import sklearn.datasets

X, y = sklearn.datasets.load_diabetes(return_X_y=True, as_frame=True)
```

``` python
from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor().fit(X, y)
```

``` python
from model_inspector import get_inspector

inspector = get_inspector(rfr, X, y)
```

You can then use various methods of `inspector` to learn about your
model.

``` python
inspector.permutation_importance()
```

    bmi    0.468172
    s5     0.449829
    bp     0.156328
    s6     0.087825
    s3     0.076583
    age    0.073492
    s1     0.050940
    s2     0.050413
    s4     0.023325
    sex    0.021515
    dtype: float64

``` python
ax = inspector.plot_permutation_importance()
```

![](index_files/figure-gfm/cell-6-output-1.png)

``` python
most_important_features = inspector.permutation_importance().index[:2]
axes = inspector.plot_dependence(
    features=[*most_important_features, most_important_features]
)
axes[0, 0].get_figure().set_size_inches(12, 3)
```

![](index_files/figure-gfm/cell-7-output-1.png)

``` python
inspector.show_correlation()
```

<style type="text/css">
#T_f1cee_row0_col0, #T_f1cee_row1_col1, #T_f1cee_row2_col2, #T_f1cee_row3_col3, #T_f1cee_row4_col4, #T_f1cee_row5_col5, #T_f1cee_row6_col6, #T_f1cee_row7_col7, #T_f1cee_row8_col8, #T_f1cee_row9_col9, #T_f1cee_row10_col10 {
  background-color: #ff0000;
  color: #f1f1f1;
}
#T_f1cee_row0_col1, #T_f1cee_row1_col0, #T_f1cee_row5_col10, #T_f1cee_row10_col5 {
  background-color: #ffd2d2;
  color: #000000;
}
#T_f1cee_row0_col2, #T_f1cee_row2_col0, #T_f1cee_row3_col5, #T_f1cee_row5_col3 {
  background-color: #ffd0d0;
  color: #000000;
}
#T_f1cee_row0_col3, #T_f1cee_row1_col7, #T_f1cee_row3_col0, #T_f1cee_row7_col1 {
  background-color: #ffaaaa;
  color: #000000;
}
#T_f1cee_row0_col4, #T_f1cee_row2_col5, #T_f1cee_row4_col0, #T_f1cee_row5_col2 {
  background-color: #ffbcbc;
  color: #000000;
}
#T_f1cee_row0_col5, #T_f1cee_row5_col0 {
  background-color: #ffc6c6;
  color: #000000;
}
#T_f1cee_row0_col6, #T_f1cee_row6_col0 {
  background-color: #ececff;
  color: #000000;
}
#T_f1cee_row0_col7, #T_f1cee_row1_col9, #T_f1cee_row7_col0, #T_f1cee_row9_col1 {
  background-color: #ffcaca;
  color: #000000;
}
#T_f1cee_row0_col8, #T_f1cee_row8_col0 {
  background-color: #ffbaba;
  color: #000000;
}
#T_f1cee_row0_col9, #T_f1cee_row9_col0 {
  background-color: #ffb2b2;
  color: #000000;
}
#T_f1cee_row0_col10, #T_f1cee_row10_col0 {
  background-color: #ffcece;
  color: #000000;
}
#T_f1cee_row1_col2, #T_f1cee_row2_col1 {
  background-color: #ffe8e8;
  color: #000000;
}
#T_f1cee_row1_col3, #T_f1cee_row3_col1 {
  background-color: #ffc2c2;
  color: #000000;
}
#T_f1cee_row1_col4, #T_f1cee_row4_col1 {
  background-color: #fff6f6;
  color: #000000;
}
#T_f1cee_row1_col5, #T_f1cee_row5_col1 {
  background-color: #ffdada;
  color: #000000;
}
#T_f1cee_row1_col6, #T_f1cee_row6_col1 {
  background-color: #9e9eff;
  color: #f1f1f1;
}
#T_f1cee_row1_col8, #T_f1cee_row8_col1 {
  background-color: #ffd8d8;
  color: #000000;
}
#T_f1cee_row1_col10, #T_f1cee_row10_col1 {
  background-color: #fff4f4;
  color: #000000;
}
#T_f1cee_row2_col3, #T_f1cee_row3_col2, #T_f1cee_row3_col8, #T_f1cee_row8_col3 {
  background-color: #ff9a9a;
  color: #000000;
}
#T_f1cee_row2_col4, #T_f1cee_row3_col4, #T_f1cee_row4_col2, #T_f1cee_row4_col3 {
  background-color: #ffc0c0;
  color: #000000;
}
#T_f1cee_row2_col6, #T_f1cee_row6_col2 {
  background-color: #a2a2ff;
  color: #f1f1f1;
}
#T_f1cee_row2_col7, #T_f1cee_row7_col2 {
  background-color: #ff9696;
  color: #000000;
}
#T_f1cee_row2_col8, #T_f1cee_row8_col2 {
  background-color: #ff8c8c;
  color: #000000;
}
#T_f1cee_row2_col9, #T_f1cee_row3_col9, #T_f1cee_row9_col2, #T_f1cee_row9_col3 {
  background-color: #ff9c9c;
  color: #000000;
}
#T_f1cee_row2_col10, #T_f1cee_row10_col2 {
  background-color: #ff6868;
  color: #f1f1f1;
}
#T_f1cee_row3_col6, #T_f1cee_row6_col3 {
  background-color: #d2d2ff;
  color: #000000;
}
#T_f1cee_row3_col7, #T_f1cee_row7_col3 {
  background-color: #ffbebe;
  color: #000000;
}
#T_f1cee_row3_col10, #T_f1cee_row10_col3 {
  background-color: #ff8e8e;
  color: #000000;
}
#T_f1cee_row4_col5, #T_f1cee_row5_col4 {
  background-color: #ff1a1a;
  color: #f1f1f1;
}
#T_f1cee_row4_col6, #T_f1cee_row6_col4 {
  background-color: #fff2f2;
  color: #000000;
}
#T_f1cee_row4_col7, #T_f1cee_row7_col4 {
  background-color: #ff7474;
  color: #f1f1f1;
}
#T_f1cee_row4_col8, #T_f1cee_row8_col4 {
  background-color: #ff7c7c;
  color: #f1f1f1;
}
#T_f1cee_row4_col9, #T_f1cee_row9_col4 {
  background-color: #ffacac;
  color: #000000;
}
#T_f1cee_row4_col10, #T_f1cee_row10_col4 {
  background-color: #ffc8c8;
  color: #000000;
}
#T_f1cee_row5_col6, #T_f1cee_row6_col5 {
  background-color: #ccccff;
  color: #000000;
}
#T_f1cee_row5_col7, #T_f1cee_row7_col5 {
  background-color: #ff5656;
  color: #f1f1f1;
}
#T_f1cee_row5_col8, #T_f1cee_row8_col5 {
  background-color: #ffaeae;
  color: #000000;
}
#T_f1cee_row5_col9, #T_f1cee_row9_col5 {
  background-color: #ffb4b4;
  color: #000000;
}
#T_f1cee_row6_col7, #T_f1cee_row7_col6 {
  background-color: #4242ff;
  color: #f1f1f1;
}
#T_f1cee_row6_col8, #T_f1cee_row8_col6 {
  background-color: #9898ff;
  color: #f1f1f1;
}
#T_f1cee_row6_col9, #T_f1cee_row9_col6 {
  background-color: #b8b8ff;
  color: #000000;
}
#T_f1cee_row6_col10, #T_f1cee_row10_col6 {
  background-color: #9a9aff;
  color: #f1f1f1;
}
#T_f1cee_row7_col8, #T_f1cee_row8_col7 {
  background-color: #ff6060;
  color: #f1f1f1;
}
#T_f1cee_row7_col9, #T_f1cee_row9_col7 {
  background-color: #ff9494;
  color: #000000;
}
#T_f1cee_row7_col10, #T_f1cee_row10_col7 {
  background-color: #ff9090;
  color: #000000;
}
#T_f1cee_row8_col9, #T_f1cee_row9_col8 {
  background-color: #ff8888;
  color: #f1f1f1;
}
#T_f1cee_row8_col10, #T_f1cee_row10_col8 {
  background-color: #ff6e6e;
  color: #f1f1f1;
}
#T_f1cee_row9_col10, #T_f1cee_row10_col9 {
  background-color: #ff9e9e;
  color: #000000;
}
</style>
<table id="T_f1cee">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_f1cee_level0_col0" class="col_heading level0 col0" >age</th>
      <th id="T_f1cee_level0_col1" class="col_heading level0 col1" >sex</th>
      <th id="T_f1cee_level0_col2" class="col_heading level0 col2" >bmi</th>
      <th id="T_f1cee_level0_col3" class="col_heading level0 col3" >bp</th>
      <th id="T_f1cee_level0_col4" class="col_heading level0 col4" >s1</th>
      <th id="T_f1cee_level0_col5" class="col_heading level0 col5" >s2</th>
      <th id="T_f1cee_level0_col6" class="col_heading level0 col6" >s3</th>
      <th id="T_f1cee_level0_col7" class="col_heading level0 col7" >s4</th>
      <th id="T_f1cee_level0_col8" class="col_heading level0 col8" >s5</th>
      <th id="T_f1cee_level0_col9" class="col_heading level0 col9" >s6</th>
      <th id="T_f1cee_level0_col10" class="col_heading level0 col10" >target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f1cee_level0_row0" class="row_heading level0 row0" >age</th>
      <td id="T_f1cee_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_f1cee_row0_col1" class="data row0 col1" >0.17</td>
      <td id="T_f1cee_row0_col2" class="data row0 col2" >0.19</td>
      <td id="T_f1cee_row0_col3" class="data row0 col3" >0.34</td>
      <td id="T_f1cee_row0_col4" class="data row0 col4" >0.26</td>
      <td id="T_f1cee_row0_col5" class="data row0 col5" >0.22</td>
      <td id="T_f1cee_row0_col6" class="data row0 col6" >-0.08</td>
      <td id="T_f1cee_row0_col7" class="data row0 col7" >0.20</td>
      <td id="T_f1cee_row0_col8" class="data row0 col8" >0.27</td>
      <td id="T_f1cee_row0_col9" class="data row0 col9" >0.30</td>
      <td id="T_f1cee_row0_col10" class="data row0 col10" >0.19</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row1" class="row_heading level0 row1" >sex</th>
      <td id="T_f1cee_row1_col0" class="data row1 col0" >0.17</td>
      <td id="T_f1cee_row1_col1" class="data row1 col1" >1.00</td>
      <td id="T_f1cee_row1_col2" class="data row1 col2" >0.09</td>
      <td id="T_f1cee_row1_col3" class="data row1 col3" >0.24</td>
      <td id="T_f1cee_row1_col4" class="data row1 col4" >0.04</td>
      <td id="T_f1cee_row1_col5" class="data row1 col5" >0.14</td>
      <td id="T_f1cee_row1_col6" class="data row1 col6" >-0.38</td>
      <td id="T_f1cee_row1_col7" class="data row1 col7" >0.33</td>
      <td id="T_f1cee_row1_col8" class="data row1 col8" >0.15</td>
      <td id="T_f1cee_row1_col9" class="data row1 col9" >0.21</td>
      <td id="T_f1cee_row1_col10" class="data row1 col10" >0.04</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row2" class="row_heading level0 row2" >bmi</th>
      <td id="T_f1cee_row2_col0" class="data row2 col0" >0.19</td>
      <td id="T_f1cee_row2_col1" class="data row2 col1" >0.09</td>
      <td id="T_f1cee_row2_col2" class="data row2 col2" >1.00</td>
      <td id="T_f1cee_row2_col3" class="data row2 col3" >0.40</td>
      <td id="T_f1cee_row2_col4" class="data row2 col4" >0.25</td>
      <td id="T_f1cee_row2_col5" class="data row2 col5" >0.26</td>
      <td id="T_f1cee_row2_col6" class="data row2 col6" >-0.37</td>
      <td id="T_f1cee_row2_col7" class="data row2 col7" >0.41</td>
      <td id="T_f1cee_row2_col8" class="data row2 col8" >0.45</td>
      <td id="T_f1cee_row2_col9" class="data row2 col9" >0.39</td>
      <td id="T_f1cee_row2_col10" class="data row2 col10" >0.59</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row3" class="row_heading level0 row3" >bp</th>
      <td id="T_f1cee_row3_col0" class="data row3 col0" >0.34</td>
      <td id="T_f1cee_row3_col1" class="data row3 col1" >0.24</td>
      <td id="T_f1cee_row3_col2" class="data row3 col2" >0.40</td>
      <td id="T_f1cee_row3_col3" class="data row3 col3" >1.00</td>
      <td id="T_f1cee_row3_col4" class="data row3 col4" >0.24</td>
      <td id="T_f1cee_row3_col5" class="data row3 col5" >0.19</td>
      <td id="T_f1cee_row3_col6" class="data row3 col6" >-0.18</td>
      <td id="T_f1cee_row3_col7" class="data row3 col7" >0.26</td>
      <td id="T_f1cee_row3_col8" class="data row3 col8" >0.39</td>
      <td id="T_f1cee_row3_col9" class="data row3 col9" >0.39</td>
      <td id="T_f1cee_row3_col10" class="data row3 col10" >0.44</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row4" class="row_heading level0 row4" >s1</th>
      <td id="T_f1cee_row4_col0" class="data row4 col0" >0.26</td>
      <td id="T_f1cee_row4_col1" class="data row4 col1" >0.04</td>
      <td id="T_f1cee_row4_col2" class="data row4 col2" >0.25</td>
      <td id="T_f1cee_row4_col3" class="data row4 col3" >0.24</td>
      <td id="T_f1cee_row4_col4" class="data row4 col4" >1.00</td>
      <td id="T_f1cee_row4_col5" class="data row4 col5" >0.90</td>
      <td id="T_f1cee_row4_col6" class="data row4 col6" >0.05</td>
      <td id="T_f1cee_row4_col7" class="data row4 col7" >0.54</td>
      <td id="T_f1cee_row4_col8" class="data row4 col8" >0.52</td>
      <td id="T_f1cee_row4_col9" class="data row4 col9" >0.33</td>
      <td id="T_f1cee_row4_col10" class="data row4 col10" >0.21</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row5" class="row_heading level0 row5" >s2</th>
      <td id="T_f1cee_row5_col0" class="data row5 col0" >0.22</td>
      <td id="T_f1cee_row5_col1" class="data row5 col1" >0.14</td>
      <td id="T_f1cee_row5_col2" class="data row5 col2" >0.26</td>
      <td id="T_f1cee_row5_col3" class="data row5 col3" >0.19</td>
      <td id="T_f1cee_row5_col4" class="data row5 col4" >0.90</td>
      <td id="T_f1cee_row5_col5" class="data row5 col5" >1.00</td>
      <td id="T_f1cee_row5_col6" class="data row5 col6" >-0.20</td>
      <td id="T_f1cee_row5_col7" class="data row5 col7" >0.66</td>
      <td id="T_f1cee_row5_col8" class="data row5 col8" >0.32</td>
      <td id="T_f1cee_row5_col9" class="data row5 col9" >0.29</td>
      <td id="T_f1cee_row5_col10" class="data row5 col10" >0.17</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row6" class="row_heading level0 row6" >s3</th>
      <td id="T_f1cee_row6_col0" class="data row6 col0" >-0.08</td>
      <td id="T_f1cee_row6_col1" class="data row6 col1" >-0.38</td>
      <td id="T_f1cee_row6_col2" class="data row6 col2" >-0.37</td>
      <td id="T_f1cee_row6_col3" class="data row6 col3" >-0.18</td>
      <td id="T_f1cee_row6_col4" class="data row6 col4" >0.05</td>
      <td id="T_f1cee_row6_col5" class="data row6 col5" >-0.20</td>
      <td id="T_f1cee_row6_col6" class="data row6 col6" >1.00</td>
      <td id="T_f1cee_row6_col7" class="data row6 col7" >-0.74</td>
      <td id="T_f1cee_row6_col8" class="data row6 col8" >-0.40</td>
      <td id="T_f1cee_row6_col9" class="data row6 col9" >-0.27</td>
      <td id="T_f1cee_row6_col10" class="data row6 col10" >-0.39</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row7" class="row_heading level0 row7" >s4</th>
      <td id="T_f1cee_row7_col0" class="data row7 col0" >0.20</td>
      <td id="T_f1cee_row7_col1" class="data row7 col1" >0.33</td>
      <td id="T_f1cee_row7_col2" class="data row7 col2" >0.41</td>
      <td id="T_f1cee_row7_col3" class="data row7 col3" >0.26</td>
      <td id="T_f1cee_row7_col4" class="data row7 col4" >0.54</td>
      <td id="T_f1cee_row7_col5" class="data row7 col5" >0.66</td>
      <td id="T_f1cee_row7_col6" class="data row7 col6" >-0.74</td>
      <td id="T_f1cee_row7_col7" class="data row7 col7" >1.00</td>
      <td id="T_f1cee_row7_col8" class="data row7 col8" >0.62</td>
      <td id="T_f1cee_row7_col9" class="data row7 col9" >0.42</td>
      <td id="T_f1cee_row7_col10" class="data row7 col10" >0.43</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row8" class="row_heading level0 row8" >s5</th>
      <td id="T_f1cee_row8_col0" class="data row8 col0" >0.27</td>
      <td id="T_f1cee_row8_col1" class="data row8 col1" >0.15</td>
      <td id="T_f1cee_row8_col2" class="data row8 col2" >0.45</td>
      <td id="T_f1cee_row8_col3" class="data row8 col3" >0.39</td>
      <td id="T_f1cee_row8_col4" class="data row8 col4" >0.52</td>
      <td id="T_f1cee_row8_col5" class="data row8 col5" >0.32</td>
      <td id="T_f1cee_row8_col6" class="data row8 col6" >-0.40</td>
      <td id="T_f1cee_row8_col7" class="data row8 col7" >0.62</td>
      <td id="T_f1cee_row8_col8" class="data row8 col8" >1.00</td>
      <td id="T_f1cee_row8_col9" class="data row8 col9" >0.46</td>
      <td id="T_f1cee_row8_col10" class="data row8 col10" >0.57</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row9" class="row_heading level0 row9" >s6</th>
      <td id="T_f1cee_row9_col0" class="data row9 col0" >0.30</td>
      <td id="T_f1cee_row9_col1" class="data row9 col1" >0.21</td>
      <td id="T_f1cee_row9_col2" class="data row9 col2" >0.39</td>
      <td id="T_f1cee_row9_col3" class="data row9 col3" >0.39</td>
      <td id="T_f1cee_row9_col4" class="data row9 col4" >0.33</td>
      <td id="T_f1cee_row9_col5" class="data row9 col5" >0.29</td>
      <td id="T_f1cee_row9_col6" class="data row9 col6" >-0.27</td>
      <td id="T_f1cee_row9_col7" class="data row9 col7" >0.42</td>
      <td id="T_f1cee_row9_col8" class="data row9 col8" >0.46</td>
      <td id="T_f1cee_row9_col9" class="data row9 col9" >1.00</td>
      <td id="T_f1cee_row9_col10" class="data row9 col10" >0.38</td>
    </tr>
    <tr>
      <th id="T_f1cee_level0_row10" class="row_heading level0 row10" >target</th>
      <td id="T_f1cee_row10_col0" class="data row10 col0" >0.19</td>
      <td id="T_f1cee_row10_col1" class="data row10 col1" >0.04</td>
      <td id="T_f1cee_row10_col2" class="data row10 col2" >0.59</td>
      <td id="T_f1cee_row10_col3" class="data row10 col3" >0.44</td>
      <td id="T_f1cee_row10_col4" class="data row10 col4" >0.21</td>
      <td id="T_f1cee_row10_col5" class="data row10 col5" >0.17</td>
      <td id="T_f1cee_row10_col6" class="data row10 col6" >-0.39</td>
      <td id="T_f1cee_row10_col7" class="data row10 col7" >0.43</td>
      <td id="T_f1cee_row10_col8" class="data row10 col8" >0.57</td>
      <td id="T_f1cee_row10_col9" class="data row10 col9" >0.38</td>
      <td id="T_f1cee_row10_col10" class="data row10 col10" >1.00</td>
    </tr>
  </tbody>
</table>

``` python
ax = inspector.plot_feature_clusters()
```

![](index_files/figure-gfm/cell-9-output-1.png)

The methods that are available for a given inspector depends on the
types of its estimator and its target `y`. An attribute called `methods`
tells you what they are:

``` python
inspector.methods
```

    ['permutation_importance',
     'plot_dependence',
     'plot_feature_clusters',
     'plot_permutation_importance',
     'show_correlation']

## Install

`pip install model_inspector`
