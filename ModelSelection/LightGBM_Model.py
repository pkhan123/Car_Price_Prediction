# %% [markdown]
# # LightGBM Model

# %% [markdown]
# ### Importing the libraries

# %%
# Base libraries
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import os.path
import pickle

# %%
# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %%
# Othe libraries
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import lightgbm as lgb
from sklearn.model_selection import RandomizedSearchCV

# %%
# import general custom data preprocessing functions
from General_Custom_Functions import *
General_Custom_Functions()

# %% [markdown]
# ### Importing the dataset

# %%
dataset = pd.read_csv('Cleaned_Dataset.csv')

# %%
imported_dataset = dataset.copy()

# %%
imported_dataset.head()

# %%
imported_dataset.shape

# %%
Check_Missing_Values(imported_dataset)

# %%
# convert Zip_Code to object
imported_dataset['Zip_Code'] = imported_dataset['Zip_Code'].astype(str)

# %% [markdown]
# ### Split the dataset into training and test dataset

# %%
# decoupling the dependent and independent variables
X = imported_dataset.iloc[:, :-1]
y = imported_dataset.iloc[:, -1]

# %%
# Train, Test split
# from now on till the model training we will only use X_train, y_train
# X_test and y_test will only be used during model testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# backup copy the dataset for feature reference
backup_X_train = X_train.copy()
backup_X_test = X_test.copy()

# %%
X_train.head()

# %%
X_test.head()

# %%
print(X_train.shape)
print(X_test.shape)

# %% [markdown]
# ### Dealing with missing categorical features

# %%
Check_Missing_Values(X_train)

# %%
# replace missing categorical variables with the object Missing_Value_XYZ
X_train['Exterior_Color'] = X_train['Exterior_Color'].fillna('Missing_Value_EC')
X_train['Interior_Color'] = X_train['Interior_Color'].fillna('Missing_Value_IC')
X_train['Transmission_Type'] = X_train['Transmission_Type'].fillna('Missing_Value_TT')

# %% [markdown]
# ### Dealing with missing numerical features

# %%
Check_Missing_Values(X_train)

# %%
# for Cylinder_Number, Wheel_Drive_Number we will replace the missing 
# values by mode (most_frequent), as they can have certain specific values
imputer_frequent = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer_frequent.fit(X_train[['Cylinder_Number', 'Wheel_Drive_Number']])
X_train[['Cylinder_Number', 'Wheel_Drive_Number']] = imputer_frequent.transform(X_train[['Cylinder_Number', 'Wheel_Drive_Number']])

# %%
# for MPG_City, MPG_Highway we will replace the missing values by median, 
# as the mileage per gallon for cars varies in some range
# we could have also taken the mean here
imputer_median = SimpleImputer(missing_values=np.nan, strategy='median')
imputer_median.fit(X_train[['MPG_City', 'MPG_Highway']])
X_train[['MPG_City', 'MPG_Highway']] = imputer_median.transform(X_train[['MPG_City', 'MPG_Highway']])

# %%
# for Mileage/Price we will replace the missing values by mean
imputer_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer_mean.fit(X_train[['Mileage']])
X_train[['Mileage']] = imputer_mean.transform(X_train[['Mileage']])

# %% [markdown]
# ### Get dummies for the categorical features

# %%
X_train.shape

# %%
# get dummies for the categorical variables
X_train = pd.get_dummies(X_train, drop_first=True)

# %%
X_train.shape

# %% [markdown]
# ### Rearrange features by importance

# %%
X_train.head()

# %%
if not os.path.exists('rearranged_feature_list.txt'):
    Rearrange_Features(X_train, y_train)

# %%
with open('rearranged_feature_list.txt') as f:
    rearranged_feature_list = f.read().splitlines()

# %%
rearranged_feature_X_train = X_train[rearranged_feature_list].copy()
X_train = rearranged_feature_X_train.copy()

# %%
X_train.head()

# %% [markdown]
# ### Get correlation qualified training dataset

# %%
if not os.path.exists('correlation_qualified_feature_list.txt'):
    Check_Correlation(X_train)

# %%
with open('correlation_qualified_feature_list.txt') as f:
    correlation_qualified_feature_list = f.read().splitlines()

# %%
correlation_qualified_X_train = X_train[correlation_qualified_feature_list].copy()

# %%
X_train = correlation_qualified_X_train.copy()
X_train.shape

# %% [markdown]
# ### Get multicollinearity qualified training dataset

# %%
# numerical feature list
numerical_feature_list_X_train = list(X_train.select_dtypes(include=['int64', 'float64']).columns)
print(numerical_feature_list_X_train)

# %%
if not os.path.exists('multicollinearity_qualified_feature_list.txt'):
    Check_Multicollinearity(X_train, numerical_feature_list_X_train)

# %%
with open('multicollinearity_qualified_feature_list.txt') as f:
    multicollinearity_qualified_feature_list = f.read().splitlines()

# %%
multicollinearity_qualified_X_train = X_train[multicollinearity_qualified_feature_list].copy()

# %%
X_train = multicollinearity_qualified_X_train.copy()
X_train.shape

# %% [markdown]
# ### Feature selection

# %%
# now there are lot of features, let's rduce them to only important features
# create feature selected dataset from general custom function
# Runtime around 15 min to 70 min (for 0.99), 107 min (for 0.95)
if not os.path.exists('selected_feature_list.txt'):
    # define parameters for feature selection
    max_validation_round = 10 # Range: 2-10, Default 10
    Make_Feature_Selection(X_train, y_train, max_validation_round)

# %%
with open('selected_feature_list.txt') as f:
    selected_feature_list = f.read().splitlines()

# %%
feature_selected_X_train = X_train[selected_feature_list].copy()

# %%
X_train = feature_selected_X_train.copy()
X_train.shape

# %% [markdown]
# ### Training the LightGBM model on the training dataset

# %%
print(X_train.columns)

# %%
# LightGBM Model
model_LGBMR = lgb.LGBMRegressor(silent=True)

# %%
# Randomized Search CV param_distributions for LightGBM

# max_depth: int -> 2–10 
max_depth = [int(x) for x in np.linspace(2, 10, num = 5)]
# n_estimators: int -> 100-1000
n_estimators = [int(x) for x in np.linspace(100, 1000, num = 5)]
# learning_rate: float -> 0.01–0.30
learning_rate = [round(x, 2) for x in np.linspace(0.01, 0.30, num = 5)]
# num_leaves: int -> 10-100
num_leaves = [int(x) for x in np.linspace(10, 100, num = 5)]
# min_child_samples: int -> 5-20
min_child_samples = [int(x) for x in np.linspace(5, 20, num = 5)]


# %%
# Create the random grid
random_param_distributions = {
                            'max_depth': max_depth,
                            'n_estimators': n_estimators,
                            'learning_rate': learning_rate,
                            'num_leaves': num_leaves,
                            'min_child_samples': min_child_samples
                            }
print(random_param_distributions)

# %%
# max_cross_validation
max_cross_validation = 10 # Test Value: 2, Default Value 10

# %%
# RandomizedSearchCV
randomized_search_cv = RandomizedSearchCV(
                                        estimator = model_LGBMR,
                                        param_distributions = random_param_distributions,
                                        n_iter = 20,
                                        cv = max_cross_validation, 
                                        random_state = 0,
                                        verbose = 1, 
                                        n_jobs = 1
                                        )

# %%
if not os.path.exists('lightgbm_regression_model.pkl'):
    # Run time: 9 min
    randomized_search_cv.fit(X_train, y_train)
    # Pickle the model
    with open('lightgbm_regression_model.pkl', 'wb') as file:
        pickle.dump(randomized_search_cv, file)

# %%
# load the pickle files
randomized_search_cv = pickle.load(open('lightgbm_regression_model.pkl','rb'))

# %%
model_best_score = randomized_search_cv.best_score_
print('Best score of the model: ', model_best_score)

# %%
randomized_search_cv.best_params_

# %% [markdown]
# ### Model performance metrics for training dataset

# %%
y_hat = randomized_search_cv.predict(X_train)

# %%
# R-Square is a good measure to determine how well the model fits the dependent variables. 
# However, it does not take into consideration of overfitting problem.
# High R-Squre value means better fitting.
r2 = randomized_search_cv.score(X_train, y_train)
print('R2:', r2)

# %%
# If regression model has many independent variables, it may fit very well to the training dataset 
# but performs badly for testing dataset. Adjusted R Square penalizes additional independent variables 
# added to the model and adjust the metric to prevent overfitting issues.
# High Adjusted R-Squre value means better fitting.
r2 = randomized_search_cv.score(X_train, y_train)
n = X_train.shape[0]
p = X_train.shape[1]
adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
print('Adjusted R2:', adjusted_r2)

# %%
# useful check of our model is a residual plot
# We can plot the PDF of the residuals and check for anomalies
sns.histplot(y_train - y_hat)
plt.title('Residuals PDF On Train Dataset', size=18)
# In the best case scenario this plot should be normally distributed
# long left tail means over predition
# long right tail implies under prediction

# %%
# The simplest way to compare the targets (y_train) and the predictions (y_hat) is to plot them on a scatter plot
# The closer the points to the 45-degree line, the better the prediction
plt.scatter(y_train, y_hat, alpha=0.2)
plt.xlabel('y_train')
plt.ylabel('y_hat')
plt.plot([0, 100000], [0, 100000], color = 'r', linewidth = 2)
plt.show()

# %%
# construct model performance evaluation dataframe
performance_train_dataset = backup_X_train.copy()
y_train_difference_percentage = abs(y_train - y_hat)*100/y_train
performance_train_dataset['y_train'] = y_train
performance_train_dataset['y_hat'] = y_hat
performance_train_dataset['y_train_difference(%)'] = y_train_difference_percentage

# %%
performance_train_dataset.head()

# %%
# check data for which model fitting is poor
performance_train_dataset.sort_values(by=['y_train_difference(%)'], ascending=False).head()

# %%
rmse_train = np.sqrt(metrics.mean_squared_error(y_train, y_hat))
nrmse_train = rmse_train/abs(y_train.max() - y_train.min())
print('Normalized RMSE (NRMSE) of trained dataset: {:.3f}'.format(nrmse_train))

# %% [markdown]
# ### Model performance metrics for test dataset

# %%
# Before Testing
# X_test and X_train should be of same data format
# dealing with missing categorical features in X_test
# dealing with missing numerical features in X_test using transform method
# get dummies for categorical features of X_test
# feature scale the numerical features of X_test using the transform method
# keep only thore columns in X_test as that of X_train

# %%
X_test.head()

# %%
Check_Missing_Values(X_test)

# %%
# replace missing categorical variables with the object Missing_Value_XYZ
X_test['Exterior_Color'] = X_test['Exterior_Color'].fillna('Missing_Value_EC')
X_test['Interior_Color'] = X_test['Interior_Color'].fillna('Missing_Value_IC')
X_test['Transmission_Type'] = X_test['Transmission_Type'].fillna('Missing_Value_TT')

# %%
# now impute the X_test with the same model that was used to impute the X_train
X_test[['Cylinder_Number', 'Wheel_Drive_Number']] = imputer_frequent.transform(X_test[['Cylinder_Number', 'Wheel_Drive_Number']])
X_test[['MPG_City', 'MPG_Highway']] = imputer_median.transform(X_test[['MPG_City', 'MPG_Highway']])
X_test[['Mileage']] = imputer_mean.transform(X_test[['Mileage']])

# %%
# get dummies for the categorical variables
X_test = pd.get_dummies(X_test, drop_first=True)

# %%
print(X_train.shape)
print(X_test.shape)

# %%
# only keep the columns same as X_train in X_test
X_train_feature_list = X_train.columns.values.tolist()
X_test = X_test[X_train_feature_list]

# %%
print(X_train.shape)
print(X_test.shape)

# %%
X_test.head()

# %%
y_pred = randomized_search_cv.predict(X_test)

# %%
# useful check of our model is a residual plot
# We can plot the PDF of the residuals and check for anomalies
sns.histplot(y_test - y_pred)
plt.title('Residuals PDF On Test Dataset', size=18)
# In the best case scenario this plot should be normally distributed
# long left tail means over predition
# long right tail implies under prediction

# %%
# The simplest way to compare the targets (y_train) and the predictions (y_hat) is to plot them on a scatter plot
# The closer the points to the 45-degree line, the better the prediction
plt.scatter(y_test, y_pred, alpha=0.2)
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.plot([0, 100000], [0, 100000], color = 'r', linewidth = 2)
plt.show()

# %%
# construct model performance evaluation dataframe
performance_test_dataset = backup_X_test.copy()
y_test_difference_percentage = abs(y_test - y_pred)*100/y_test
performance_test_dataset['y_test'] = y_test
performance_test_dataset['y_pred'] = y_pred
performance_test_dataset['y_test_difference(%)'] = y_test_difference_percentage

# %%
performance_test_dataset.head()

# %%
# check data for which model fitting is poor
performance_test_dataset.sort_values(by=['y_test_difference(%)'], ascending=False).head()

# %%
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
nrmse_test = rmse_test/abs(y_test.max() - y_test.min())
print('Normalized RMSE (NRMSE) of test dataset: {:.3f}'.format(nrmse_test))

# %%
# difference between nrmse_train and nrmse_test
nrmse_difference = (nrmse_test - nrmse_train)*100/nrmse_train
print('Best score of the model on training dataset: {:.3f}'.format(model_best_score))
print('Normalized RMSE (NRMSE) of trained dataset: {:.3f}'.format(nrmse_train))
print('Normalized RMSE (NRMSE) of test dataset: {:.3f}'.format(nrmse_test))
print('Difference between nrmse_train and nrmse_test: {:.2f} %'.format(nrmse_difference))

# %%



