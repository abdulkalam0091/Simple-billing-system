import tkinter as tk
from tkinter import ttk

def calculator():
    try:
        quantity = float(qty_text.get())
        price = float(price_text.get())
        total = quantity * price
        total_text.delete(0, tk.END)
        total_text.insert(0, total)
    except ValueError:
        total_text.delete(0, tk.END)
        total_text.insert(0, "Invalid Input")


def add():
    try:
        item = item_text.get()
        qty = qty_text.get()
        price = price_text.get()
        total = float(total_text.get())

        # Check if any of the fields are empty
        if not item or not qty or not price or not total:
            raise ValueError("All fields must be filled out!")

        table.insert("", tk.END, values=(item, qty, price, total))

        # Clear the entry fields after adding the item
        item_text.delete(0, tk.END)
        qty_text.delete(0, tk.END)
        price_text.delete(0, tk.END)
        total_text.delete(0, tk.END)

        # Calculate the grand total
        grand_total = 0
        for item in table.get_children():
            values = table.item(item, "values")
            grand_total += float(values[3])
        
        g_total.config(text=f"Grand Total: {grand_total:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

# Create the main window
window = tk.Tk()
window.title("Billing System")
window.geometry("820x500")

# Adjust column sizes
for col in range(4):
    window.columnconfigure(col, minsize=150)

# Heading
heading = tk.Label(window, text="Billing System", font=("Arial", 30), fg='white', bg='black')
heading.pack(pady=20)

# Item details frame
item_details = tk.Frame(window)
item_details.pack(pady=10)

# Item Name Label
item_name = tk.Label(item_details, text="Item Name", font=("Arial", 15))
item_name.grid(row=0, column=0, padx=10, pady=5)

# Quantity Label
qty_label = tk.Label(item_details, text="Quantity", font=("Arial", 15))
qty_label.grid(row=0, column=1, padx=10, pady=5)

# Price Label
price_label = tk.Label(item_details, text="Price", font=("Arial", 15))
price_label.grid(row=0, column=2, padx=10, pady=5)

# Total Label
total_label = tk.Label(item_details, text="Total", font=("Arial", 15))
total_label.grid(row=0, column=3, padx=10, pady=5)

# Item Entry Box
item_text = tk.Entry(item_details, font=("Arial", 15), width=15)
item_text.grid(row=1, column=0, padx=10, pady=5)

# Quantity Entry Box
qty_text = tk.Entry(item_details, font=("Arial", 15), width=15)
qty_text.grid(row=1, column=1, padx=10, pady=5)

# Price Entry Box
price_text = tk.Entry(item_details, font=("Arial", 15), width=15)
price_text.grid(row=1, column=2, padx=10, pady=5)

# Total Entry Box
total_text = tk.Entry(item_details, font=("Arial", 15), width=15)
total_text.grid(row=1, column=3, padx=10, pady=5)

# Calculate Button
calc_btn = tk.Button(item_details, text="Calculate", font=("Arial", 15), bg="blue", fg='white', command=calculator)
calc_btn.grid(row=2, column=2, padx=10, pady=10)

# Add to Table Button
add_btn = tk.Button(item_details, text="Add to Table", font=("Arial", 15), bg="blue", fg='white', command=add)
add_btn.grid(row=2, column=3, padx=10, pady=10)

# Create the table for displaying items
table = ttk.Treeview(window, columns=('item', 'qty', 'price', 'total'), show="headings")
table.pack(pady=10)

# Define table headings
table.heading("#1", text="Item Name")
table.heading("#2", text="Quantity")
table.heading("#3", text="Price")
table.heading("#4", text="Total")

# Grand Total Label
g_total = tk.Label(window, text="Grand Total: 0", fg='green', font=("Arial", 18))
g_total.pack(pady=5)

# Run the main event loop
window.mainloop()
