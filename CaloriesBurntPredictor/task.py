# -*- coding: utf-8 -*-
"""Task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mFWhJ_9E2UfAxJwCZfhCkl5e_msvFl2u
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("pcb.csv")
df.head(5)

#different exercies/sports
activities = df['Activity, Exercise or Sport (1 hour)'].value_counts()
activities

describe = df.describe()
describe

dtypes = df.dtypes
dtypes

#finding activity/sport in which most calories are burnt per kg
max_calories = df.sort_values(['Calories per kg'], ascending=False)
max_calories.head(1)

#finding activity/sport in which least calories are burnt per kg
least_calories = max_calories.tail(1)
least_calories

#from the below plot we can assume, the calories burnt increase on increase of weight 
plt.scatter(df.index, df["130 lb"], color = 'blue') 
plt.xlabel("Exercises")
plt.ylabel("Calories burned")
plt.scatter(df.index, df["155 lb"], color = 'green')
plt.xlabel("Exercises")
plt.ylabel("Calories burned")
plt.scatter(df.index, df["180 lb"], color = 'red')
plt.xlabel("Exercises")
plt.ylabel("Calories burned")
plt.scatter(df.index, df["205 lb"], color = 'orange')
plt.xlabel("Exercises")
plt.ylabel("Calories burned")
plt.legend(["130 lb", "155 lb", "180 lb", "205 lb"])
plt.show()

#As DataSet above had no proper feature variables to predict on I tried another dataset which was specifed in the examples of the DataSet

exercise = pd.read_csv('exercise.csv')
calories = pd.read_csv('calories.csv')
df2 = pd.merge(exercise, calories, on = 'User_ID')
df2.head(5)

# Calories Burned vs Exercise Duration 
plt.figure(figsize=(6, 6))
plt.scatter(df2['Duration'], df2['Calories']);
plt.xlabel('Duration in mins'); plt.ylabel('Calories'); 
plt.title('Calories burned vs Duration of Exercise');

#Taking our Feature Variables X and Y
X = df2.Duration
y = df2.Calories

class LinearRegression:

    def __init__(self):
        self.b0 = None
        self.b1 = None
    
    def fit(self, X, y): #Calculating the slope and Intercept
        numerator = np.sum((X - np.mean(X)) * (y - np.mean(y)))
        denominator = np.sum((X - np.mean(X)) ** 2)
        self.b1 = numerator / denominator
        self.b0 = np.mean(y) - self.b1 * np.mean(X)
        
    def predict(self, X): #Prediction 
      
       
        return self.b0 + self.b1 * X #Returns Linear Regression Formula

#Trainnig the DataSet
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regr = LinearRegression()
regr.fit(X,y)

pred = regr.predict(60)
print("Total Calories Burnt in 1 hr of Exercise is :", pred)