import tkinter as tk
from tkinter import ttk
import requests

# Function to convert currency
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rates = data['rates']
        conversion_rate = rates.get(to_currency)
        if conversion_rate:
            converted_amount = amount * conversion_rate
            result_label.config(text=f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Conversion rate not found.")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create and place widgets
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "PKR"])  # Add more currencies as needed
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
from_currency_combobox.set("USD")  # Default value

tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "PKR"])  # Add more currencies as needed
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
to_currency_combobox.set("PKR")  # Default value

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
