# Preprocessing data - scaling

### Why Scale Features?
 
- Features with larger magnitudes can dominate features with smaller values, leading to, for example, biased coefficients in linear/logistic regression or the principal components (in PCA). 
- Distance-based models (like k-NN) are sensitive to scale differences. A feature with large values (e.g., molecular weight in thousands) will dominate features with smaller values (e.g., logS).   
- Some models, e.g. logistic regression, uses gradient-based optimisation. Large differences in feature scales can slow convergence.
- Helps avoid issues with very large or small values leading to numerical instability.

:::{seealso}
[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#sphx-glr-auto-examples-preprocessing-plot-scaling-importance-py) in scikit-learn examples.
:::

---

### Two Common Scaling Methods

#### Normalisation (min-max scaling)

- Rescales features to a **fixed range** (typically [0,1] or [-1,1]).  
- Formula:  
  $$
  X' = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
  $$
- Best when data is **not normally distributed** and you want to keep all values within a bounded range.  


#### Standardisation (Z-score scaling)
- Centers data to **mean = 0** and scales to **standard deviation = 1**.  
- Formula:  
  $$
  X' = \frac{X - \mu}{\sigma}
  $$
- Best when data follows a **normal distribution** or when dealing with **PCA, linear models**.  


---

### How to scale features using [`scikit-learn`](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling)

#### Import scalers from scikit-learn

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
```

#### Apply scaling

- **Normalisation** (Min-max scaling)
  ```python
  min_max_scaler = MinMaxScaler()
  features_scaled = min_max_scaler.fit_transform(features)
  ```

- **Standardisation (Z-score scaling)**  
  ```python
  standard_scaler = StandardScaler()
  features_standardized = standard_scaler.fit_transform(features)
  ```

#### Preprocessing data for ML

**It is important to scale *after* `train_test_split`**

If the full data is scaled **before** splitting, information from the test set (its mean and standard deviation) will "leak" into the training process, leading to [**data leakage**](https://www.ibm.com/think/topics/data-leakage-machine-learning). 

Instead:
1. Fit the scaler **only on the training set** (`scaler.fit(X_train)`).  

2. Transform **both** the training and test sets, but separately.(`scaler.transform(X_train)` and `scaler.transform(X_test)`).  

</br>

Following this order:

- Prevents **data leakage** by ensuring the model only sees training data during fitting.  
 
- **Maintains independence** of train and test sets, ensuring a fair evaluation. 

- Makes real-world predictions more reliable, since real test data does not influence earlier preprocessing steps.


