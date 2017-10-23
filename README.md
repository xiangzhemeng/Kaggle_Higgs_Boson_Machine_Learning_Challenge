
 
# EPFL Machine Learning CS-433 Porject1

### `Team member`:
- Süha Kagan Köse
- Sung Lin Chan
- Xiangzhe Meng


This project held a private contest in [Kaggle competition](https://www.kaggle.com/c/epfml-higgs) and it is similar to the [Higgs Boson Machine Learning Challenge - 2014](https://www.kaggle.com/c/Higgs-boson). For more details about this project requirement,go to [project1_description](#) in this repository.

The following below are the brief overviews of the python scripts we used in this project. To see more information and detail about our project, go to [PDF report](#) in this repository.


## Auxiliary modules
### `proj1_helpers.py`
Contains the helper functions that are used to load data, generate the predictions and output the result to csv file as submission file in Kaggle's format

### `tool.py`
Contain the hepler functions for main regression models and finding-hyperparameter methods  .
- **`build_polynomial_features`, `standardize`, `replace_missing_data_by_frequent_value`, `process_data` and `group_features_by_jet`**: Pre-process the raw dataset to generate desired features for training and prediction steps. 
- **`compute_accuracy`, `build_k_indices`**: Computes the accuracy for cross validation step
- **`compute_gradient`**: Computes the gradient for gradient descent and stochastic gradient descent
- **`batch_iter`**: Generate a minibatch iterator for a dataset

### `costs.py`
Contain 3 auxiliary function and 2 different cost functions
- **`calculate_mse`**: Compute mean square error, an auxiliary function of compute_loss
- **`calculate_mae`**: Compute mean absolute error, an auxiliary function of compute_loss
- **`compute_loss`**: Compute loss for regression model
- **`sigmoid`**:  An auxiliary function of compute_loss_neg_log_likelihood
- **`compute_loss_neg_log_likelihood`**:  Compute negative log likelihood for logistic regression

## Algorithms for Regression 
### `implementations.py`
Contain the mandatory implementations of  6 regression models for this project
- **`least_squares_GD`**: Linear regression using gradient descent
- **`least_squares_SDG`**: Linear regression using stochastic gradient descent
- **`least_squares`**: Least squares regression using normal equations
- **`ridge_regression`**: Ridge regression using normal equations
- **`logistic_regression`**: using stochastic gradient descent
- **`regularized_logistic_regression`**: Regularized logistic regression

### `main.py`
Script that generates the exact CSV file submitted on Kaggle.

## Others 
### `grid_search_for_param.ipynb`
An python notebook used for finding the best hyperparameters by running cross-validation
### `ML_Project1_Analysis_Notebook.ipynb`
An python notebook used for doing some feature engineering tests and finding the best method to do the final prediction by implementing cross validation for all 6 methods and comparing the average test accuracy



