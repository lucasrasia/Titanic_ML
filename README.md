# Titanic Survival Prediction

This project aims to predict the survival of passengers on the Titanic using various machine learning techniques. The dataset used is the classic Titanic survival dataset, which includes passenger demographics, ticket information, and survival status.

## Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Technologies Used](#technologies-used)

## About the Project

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, resulting in the deaths of 1502 out of 2224 passengers and crew. This project delves into the factors that contributed to survival, building a predictive model to determine whether a passenger would survive or not.

## Dataset

The dataset used is the `titanic.csv` from the Data Science Dojo's GitHub repository. It contains various information about each passenger, including:
- `PassengerId`: Unique identifier for each passenger.
- `Survived`: Survival status (0 = No, 1 = Yes).
- `Pclass`: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
- `Name`: Passenger's name.
- `Sex`: Passenger's gender.
- `Age`: Passenger's age.
- `SibSp`: Number of siblings/spouses aboard the Titanic.
- `Parch`: Number of parents/children aboard the Titanic.
- `Ticket`: Ticket number.
- `Fare`: Passenger fare.
- `Cabin`: Cabin number.
- `Embarked`: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Features

- **Data Cleaning and Preprocessing**: Handling missing values, dropping irrelevant columns, and encoding categorical features.
- **Feature Engineering**: Creating new features like `Total_family`.
- **Model Training**: Utilizing `RandomForestClassifier` for survival prediction.
- **Model Evaluation**: Assessing the model's performance using accuracy score.

## Installation

To run this project, you'll need to have Python installed. It's recommended to use a virtual environment.

## Usage

The main script for this project is provided as a Jupyter Notebook/Colab Notebook. You can open and run it directly.

Open the notebook in Google Colab or your local Jupyter environment.
Run all cells to execute the data loading, preprocessing, model training, and evaluation steps.
The notebook will output the accuracy of the trained model.

### Example of how to load and process data (from the notebook)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

### ... (rest of the preprocessing and model training code)
``` bash
print(acerto) # This will print the accuracy score
```
## Model Evaluation
The model's performance is evaluated using the accuracy score. The current model achieves an accuracy of approximately 82.12% on the test set.

## Technologies Used
Python 3
Pandas (for data manipulation)
Scikit-learn (for machine learning models and utilities)
Jupyter/Google Colab (for development environment)
