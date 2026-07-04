# =========================
# RESTAURANT MANAGEMENT SYSTEM
# =========================

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "French Fries": 100,
    "Sandwich": 150,
    "Coffee": 80,
    "Coke": 40,
    "Ice Cream": 90
}

order = {}
total = 0

# =========================
# WELCOME MESSAGE
# =========================
print("=" * 40)
print("    WELCOME TO BELLA'S RESTAURANT")
print("=" * 40)

# =========================
# DISPLAY MENU
# =========================
print("\n----------- MENU -----------\n")

for item, price in menu.items():
    print(f"{item:15} ₹{price}")

print("\n----------------------------")

customer_name = input("\nEnter Customer Name: ")

# =========================
# ORDER TAKING LOOP
# =========================
while True:
    item = input("\nEnter item name (or type 'done' to finish): ").title()

    if item.lower() == "done":
        break

    if item in menu:
        qty = int(input("Enter quantity: "))

        if qty <= 0:
            print("Invalid quantity!")
            continue

        if item in order:
            order[item] += qty
        else:
            order[item] = qty

        print(f"{qty} {item} added to your order.")

    else:
        print("Item not found in menu!")

# =========================
# BILL GENERATION
# =========================
print("\n\n" + "=" * 40)
print("             BILL RECEIPT")
print("=" * 40)

print(f"Customer Name: {customer_name}")
print("\nItems Ordered:\n")

for item, qty in order.items():
    price = menu[item] * qty
    total += price
    print(f"{item:15} x {qty} = ₹{price}")

# GST Calculation (5%)
gst = total * 0.05
final_amount = total + gst

print("\n----------------------------")
print(f"Subtotal: ₹{total}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{final_amount:.2f}")
print("=" * 40)

print("\nTHANK YOU FOR VISITING! 😊")
print("=" * 40)