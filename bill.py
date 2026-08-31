import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
from datetime import datetime
import os

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermarket Billing System")
        self.root.geometry("900x700")  # Increased window size for better display

        # Store Info
        self.store_name = "SUPER MARKET"
        self.store_address = "123 Market Street"
        self.phone = "(555) 555-5555"
        
        # Bill number initialization
        self.bill_number = 1000
        
        # Item List
        self.items = []

        # Header Frame
        header_frame = tk.Frame(self.root, bg="#4CAF50", pady=20)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text=self.store_name, font=("Arial", 20, "bold"), bg="#4CAF50", fg="white").pack()
        tk.Label(header_frame, text=self.store_address, font=("Arial", 12), bg="#4CAF50", fg="white").pack()
        tk.Label(header_frame, text=f"Phone: {self.phone}", font=("Arial", 12), bg="#4CAF50", fg="white").pack()

        # Input Section (Item Entry)
        input_frame = tk.Frame(self.root, pady=10)
        input_frame.pack(fill=tk.X)

        tk.Label(input_frame, text="Item Name", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        self.item_name_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.item_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Unit", font=("Arial", 10)).grid(row=0, column=4, padx=5, pady=5)
        self.unit_var = tk.StringVar(value="pc")
        unit_dropdown = ttk.Combobox(input_frame, textvariable=self.unit_var, values=["g", "kg", "ml", "l", "pc"], state="readonly", font=("Arial", 10))
        unit_dropdown.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(input_frame, text="Price/Unit", font=("Arial", 10)).grid(row=0, column=6, padx=5, pady=5)
        self.price_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.price_entry.grid(row=0, column=7, padx=5, pady=5)

        add_button = tk.Button(input_frame, text="Add Item", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.add_item)
        add_button.grid(row=0, column=8, padx=5, pady=5)

        # Items Table with Scrollbar
        tree_frame = tk.Frame(self.root, pady=10)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("Item", "Qty", "Unit", "Price", "Total"), show='headings', height=8)
        self.tree.heading("Item", text="Item", anchor="w")
        self.tree.heading("Qty", text="Qty", anchor="w")
        self.tree.heading("Unit", text="Unit", anchor="w")
        self.tree.heading("Price", text="Price/Unit", anchor="w")
        self.tree.heading("Total", text="Total", anchor="w")

        self.tree.column("Item", width=200, anchor="w")
        self.tree.column("Qty", width=80, anchor="center")
        self.tree.column("Unit", width=80, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Total", width=100, anchor="center")

        tree_scroll = tk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Action Buttons
        action_frame = tk.Frame(self.root, pady=20)
        action_frame.pack(fill=tk.X)

        generate_button = tk.Button(action_frame, text="Generate Bill", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.generate_bill)
        generate_button.pack(side=tk.LEFT, padx=10)

        clear_button = tk.Button(action_frame, text="Clear All", font=("Arial", 12), bg="#f44336", fg="white", command=self.clear_all)
        clear_button.pack(side=tk.LEFT, padx=10)

        print_button = tk.Button(action_frame, text="Print Bill", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.print_bill)
        print_button.pack(side=tk.LEFT, padx=10)

        # Bill Output
        self.bill_text = tk.Text(self.root, height=15, wrap=tk.WORD, font=("Arial", 12))
        self.bill_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_item(self):
        name = self.item_name_entry.get()
        qty = self.quantity_entry.get()
        unit = self.unit_var.get()
        price = self.price_entry.get()

        try:
            qty = float(qty)
            price = float(price)
            total = qty * price
            self.items.append({"name": name, "qty": qty, "unit": unit, "price": price, "total": total})
            self.tree.insert("", tk.END, values=(name, qty, unit, price, total))
            self.clear_inputs()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid quantity and price.")

    def generate_bill(self):
        if not self.items:
            messagebox.showwarning("No Items", "Please add items to generate a bill.")
            return

        bill_number = self.bill_number
        bill = [f"{'='*40}\n"]
        bill.append(f"{self.store_name.center(40)}\n")
        bill.append(f"{self.store_address.center(40)}\n")
        bill.append(f"Phone: {self.phone.center(40)}\n")
        bill.append(f"{'='*40}\n")
        bill.append(f"Bill Number: {bill_number}".ljust(20) + f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        bill.append(f"{'-'*40}\n")
        bill.append(f"{'Item':<12}{'Qty':>6}{'Unit':>6}{'Price':>8}{'Total':>10}\n")
        bill.append(f"{'-'*40}\n")

        subtotal = 0
        for item in self.items:
            subtotal += item['total']
            bill.append(f"{item['name']:<12}{item['qty']:>6.2f}{item['unit']:>6}{item['price']:>8.2f}{item['total']:>10.2f}\n")

        tax = subtotal * 0.10
        final_total = subtotal + tax
        bill.append(f"{'-'*40}\n")
        bill.append(f"{'Subtotal:':<30}{subtotal:>10.2f}\n")
        bill.append(f"{'Tax (10%):':<30}{tax:>10.2f}\n")
        bill.append(f"{'Total:':<30}{final_total:>10.2f}\n")
        bill.append(f"{'='*40}\n")
        bill.append(f"{'Thank You for Shopping with Us!'.center(40)}\n")
        bill.append(f"{'='*40}\n")

        # Update the bill text box
        self.bill_text.delete(1.0, tk.END)
        self.bill_text.insert(tk.END, "".join(bill))

        # Auto-save the bill
        self.save_bill("\n".join(bill))

    def save_bill(self, bill):
        file_path = f"bill_{self.bill_number}.txt"
        with open(file_path, "w") as file:
            file.write(bill)
        self.bill_number += 1  # Increment the bill number for the next bill

    def clear_all(self):
        self.items.clear()
        self.tree.delete(*self.tree.get_children())
        self.bill_text.delete(1.0, tk.END)
        self.clear_inputs()

    def clear_inputs(self):
        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def print_bill(self):
        # You can implement print functionality here if needed.
        messagebox.showinfo("Print", "This is a placeholder for the print functionality.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
