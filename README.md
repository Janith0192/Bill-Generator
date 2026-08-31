# Bill-Generator
A GUI-based Supermarket Billing System built with Python and Tkinter that manages item entries, calculates totals with tax, and automatically exports bills as text files.


# Supermarket Billing System

A desktop billing application built using Python's Tkinter GUI toolkit[cite: 5]. This application allows users to add items dynamically, specify quantities and units, calculate subtotal and tax automatically, and auto-save the generated bill to a `.txt` file[cite: 5].

## Features

- **Item Management:** Add items with unit prices, custom quantities, and measurement units (`g`, `kg`, `ml`, `l`, `pc`)[cite: 5].
- **Interactive Data Table:** Uses Tkinter `Treeview` to display added items with a scrollbar[cite: 5].
- **Automated Bill Calculation:** Computes total price per item, subtotal, 10% tax, and final amount automatically[cite: 5].
- **Receipt Generation:** Displays formatted receipt text in real-time[cite: 5].
- **Auto-Save:** Saves generated receipts as text files (`bill_1000.txt`, etc.) in the project directory[cite: 5].

## Requirements

- Python 3.x
- `tkinter` (Pre-installed with standard Python distributions on Windows and macOS)[cite: 5].

> **Note:** No additional external libraries (`pip install`) are required as standard modules (`tkinter`, `datetime`, `os`) are used[cite: 5].

## Usage

1. Enter the **Item Name**, **Quantity**, select the **Unit**, and enter the **Price/Unit**[cite: 5].
2. Click **Add Item** to insert the item into the transaction list[cite: 5].
3. Click **Generate Bill** to display the calculated invoice and auto-save it as a `.txt` file[cite: 5].
4. Use **Clear All** to start a new transaction[cite: 5].
