# 1. Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox
import pickle

# 2. Load dataset and preprocess
try:
    df = pd.read_csv('sales_data.csv')
except FileNotFoundError:
    messagebox.showerror("Error", "Dataset file not found. Please ensure 'sales_data.csv' exists.")
    exit()

# 3. Select features and target
try:
    X = df[['Price', 'Promotion', 'Temperature', 'Holiday']]
    y = df['SalesQuantity']
except KeyError:
    messagebox.showerror("Error", "Dataset columns are missing or incorrectly named.")
    exit()

# 4. Train-test split
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
except ValueError:
    messagebox.showerror("Error", "Error splitting dataset into train and test sets.")
    exit()

# 5. Train the model
model = LinearRegression()
try:
    model.fit(X_train, y_train)
except ValueError:
    messagebox.showerror("Error", "Error training the model.")
    exit()

# 6. Save the trained model using pickle
with open('linear_regression_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# 7. GUI Design using Tkinter
# Remaining GUI code...

