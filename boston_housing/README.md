# Model Evaluation and Validation
## Project: Predicting Boston Housing Prices

## Description

The Boston housing market is highly competitive and building a machine learning model would be beneficial for the best real estate agents in the area. Luckily, there is the Boston Housing dataset which contains aggregated data on various features for houses in Greater Boston communities, including the median value of homes for each of those areas. This model will then be used to estimate the best selling price for the clients\' homes.

## Project Overview
In this project, basic machine learning concepts (mainly using NumPy and Scikit-Learn) were applied on data collected for housing prices in the Boston, Massachusetts area to predict the selling price of a new home. First the data was explored to obtain important features and descriptive statistics about the dataset. Next, the data was split into testing and training subsets and a suitable performance metric for this problem was determined. Then the performance graphs of of a learning algorithm with varying parameters and training set sizes were analyzed. It enabled us to pick the optimal model that best generalized for unseen data. Finally, the optimal model was tested on a new sample and the predicted selling price was compared to our statistics.

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. 

### Code

The code is provided in the `boston_housing.ipynb` notebook file. `visuals.py` contains supplementary functions for data visualisation and the data is in the `housing.csv` file.

### Run

In a terminal or command window, navigate to the the project's directory `boston_housing/` (that contains this README) and run one of the following commands:

```bash
ipython notebook boston_housing.ipynb
```  
or
```bash
jupyter notebook boston_housing.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing).

**Features**
1.  `RM`: average number of rooms per dwelling
2. `LSTAT`: percentage of population considered lower status
3. `PTRATIO`: pupil-teacher ratio by town

**Target Variable**
4. `MEDV`: median value of owner-occupied homes