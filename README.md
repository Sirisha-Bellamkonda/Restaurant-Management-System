# Restaurant-Management-System
A Python-based console application that manages restaurant orders, calculates bills with GST, validates user input, and generates itemized receipts using dictionaries, loops, and conditional logic.
# 🍽️ Restaurant Management System

A simple **Python console-based Restaurant Management System** that allows customers to place food orders, calculates the total bill with GST, and generates a formatted receipt. This project was built to strengthen core Python programming concepts through a real-world application.

## 📌 Features

* Interactive restaurant menu
* Customer name input
* Order multiple food items
* Specify item quantities
* Automatic subtotal calculation
* 5% GST calculation
* Itemized bill generation
* Input validation for invalid items and quantities
* Clean and user-friendly console interface

## 🛠️ Technologies Used

* Python 3

## 📂 Project Structure

```text
Restaurant-Management-System/
│── restaurant.py
└── README.md
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Restaurant-Management-System.git
```

2. Navigate to the project folder:

```bash
cd Restaurant-Management-System
```

3. Run the program:

```bash
python restaurant.py
```

## 📖 Concepts Covered

* Variables
* Dictionaries
* Loops (`for`, `while`)
* Conditional Statements (`if`, `else`)
* User Input
* Type Casting
* Dictionary Operations
* String Methods
* Formatted Output (f-strings)
* Arithmetic Operations

## 📷 Sample Output

```text
========================================
     WELCOME TO BELLA'S RESTAURANT
========================================

----------- MENU -----------

Pizza           ₹250
Burger          ₹120
Pasta           ₹180
Coffee          ₹80

Enter Customer Name: John

Enter item name (or type 'done' to finish): Pizza
Enter quantity: 2

Enter item name (or type 'done' to finish): Coffee
Enter quantity: 1

Enter item name (or type 'done' to finish): done

========================================
             BILL RECEIPT
========================================

Customer Name: John

Items Ordered:

Pizza           x 2 = ₹500
Coffee          x 1 = ₹80

----------------------------
Subtotal: ₹580
GST (5%): ₹29.00
Total Payable: ₹609.00
========================================

THANK YOU FOR VISITING! 😊
```

## 🚀 Future Enhancements

* Store order history in a database
* Add an admin panel to manage the menu
* Generate PDF bills

## 👨‍💻 Author

Developed as a Python practice project to apply programming fundamentals in a practical restaurant billing system.
