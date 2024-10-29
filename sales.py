# 1. Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

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

# 6. GUI Design using Tkinter
def predict_sales():
    try:
        price = float(entry_price.get())
        if price < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid non-negative price in rupees.")
        return
    
    promotion = promotion_var.get()  # Get selected promotion value
    
    try:
        temperature = float(entry_temperature.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature.")
        return
    
    holiday = holiday_var.get()  # Get selected holiday value

    # Predict sales
    try:
        prediction = model.predict([[price, promotion, temperature, holiday]])
    except ValueError:
        messagebox.showerror("Error", "Error predicting sales quantity.")
        return
        
    messagebox.showinfo("Prediction", f"Predicted Sales Quantity: {prediction[0]:.2f}")

# Create GUI window
window = tk.Tk()
window.title("Sales Volume Predictor")

# Set window size with increased length
window.geometry("400x600")

# Setting text color and background color
window.configure(bg="lavender")

# Increase text size
text_size = 20

# Questions and Entry fields
tk.Label(window, text="Price In Rupees :", fg="teal", bg="lavender", font=("Arial", text_size)).pack()
entry_price = tk.Entry(window, width=40)  # Increase width
entry_price.pack()

tk.Label(window, text="Advertisement :", fg="teal", bg="lavender", font=("Arial", text_size)).pack()
promotion_var = tk.IntVar()
promotion_var.set(0)  # Default value
tk.Radiobutton(window, text="No", variable=promotion_var, value=0, bg="lavender", font=("Arial", text_size)).pack(anchor=tk.CENTER)
tk.Radiobutton(window, text="Yes", variable=promotion_var, value=1, bg="lavender", font=("Arial", text_size)).pack(anchor=tk.CENTER)

tk.Label(window, text="Current Temperature :", fg="teal", bg="lavender", font=("Arial", text_size)).pack()
entry_temperature = tk.Entry(window, width=40)  # Increase width
entry_temperature.pack()

tk.Label(window, text="Holiday:", fg="teal", bg="lavender", font=("Arial", text_size)).pack()
holiday_var = tk.IntVar()
holiday_var.set(0)  # Default value
tk.Radiobutton(window, text="No", variable=holiday_var, value=0, bg="lavender", font=("Arial", text_size)).pack(anchor=tk.CENTER)
tk.Radiobutton(window, text="Yes", variable=holiday_var, value=1, bg="lavender", font=("Arial", text_size)).pack(anchor=tk.CENTER)

# Add predict button
predict_button = tk.Button(window, text="Predict Sales", command=predict_sales, bg="lavender", font=("Arial", text_size))
predict_button.pack()

# Run GUI
window.mainloop()
