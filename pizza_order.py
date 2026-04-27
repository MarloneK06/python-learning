# ============================================
# PIZZA ORDER SYSTEM — Complete Program
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]

topping_names = [
    "Pepperoni",
    "Mushrooms",
    "Green Peppers",
    "Onions",
    "Sausage",
    "Bacon",
    "Extra Cheese",
    "Pineapple"
]

topping_price = 1.50

# ----- Order Storage -----
order_descriptions = []
order_prices = []

print("Welcome to the CS 1300 Pizza Shop!\n")

# ===== ORDERING LOOP =====
while True:

    # ----- Display Size Menu -----
    print("==============================")
    print(" PIZZA SIZES")
    print("==============================")

    for i in range(len(sizes)):
        print(f" {i + 1}. {sizes[i]} ${size_prices[i]:>5.2f}")

    print("==============================")

    # ----- Get Valid Size -----
    while True:
        choice = input("Pick a size (1-4): ")

        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        if choice < 1 or choice > 4:
            print("Choose 1-4.")
            continue

        size_choice = choice - 1
        base_price = size_prices[size_choice]
        break

    # ----- Select Toppings -----
    selected_toppings = []

    print("\nAvailable toppings ($1.50 each):")

    for i in range(len(topping_names)):
        print(f" {i + 1}. {topping_names[i]}")

    while True:
        topping = input("Add topping # (or 'done'): ").lower()

        if topping == "done":
            break

        if not topping.isdigit():
            print("Please enter a number or done.")
            continue

        topping = int(topping)

        if topping < 1 or topping > len(topping_names):
            print("Invalid topping number.")
            continue

        topping_name = topping_names[topping - 1]

        if topping_name in selected_toppings:
            print("Already added", topping_name + "!")
            continue

        selected_toppings.append(topping_name)
        print("Added", topping_name)

    # ----- Calculate Price -----
    pizza_price = base_price + (len(selected_toppings) * topping_price)

    if len(selected_toppings) == 0:
        topping_text = "Cheese"
    else:
        topping_text = ", ".join(selected_toppings)

    description = sizes[size_choice] + " " + topping_text

    order_descriptions.append(description)
    order_prices.append(pizza_price)

    # ----- Order Another Pizza -----
    while True:
        again = input("\nOrder another pizza? (yes/no): ").lower()

        if again == "yes" or again == "y":
            print()
            break

        elif again == "no" or again == "n":
            again = "no"
            break

        else:
            print("Please enter yes or no.")

    if again == "no":
        break


# ===== POST ORDER =====

if len(order_descriptions) == 0:
    print("\nNo pizzas ordered. See you next time!")

else:
    # ----- Discount Code -----
    discount = 0

    print("\nDiscount Codes:")
    print("STUDENT10 = 10% off")
    print("HALFOFF = 50% off")

    attempts = 0

    while attempts < 3:
        code = input("Enter discount code (or none): ").upper()

        if code == "NONE":
            break

        elif code == "STUDENT10":
            discount = 0.10
            print("10% discount applied!")
            break

        elif code == "HALFOFF":
            discount = 0.50
            print("50% discount applied!")
            break

        else:
            attempts += 1
            print("Invalid code.")

    if attempts == 3 and discount == 0:
        print("No discount applied.")

    # ----- Print Receipt -----
    print("\n====================================")
    print(" YOUR ORDER RECEIPT")
    print("====================================")

    subtotal = 0

    for i in range(len(order_descriptions)):
        print(f"{i + 1}. {order_descriptions[i]}")
        print(f"   ${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    discount_amount = subtotal * discount
    new_subtotal = subtotal - discount_amount
    tax = new_subtotal * 0.07
    total = new_subtotal + tax

    print("------------------------------------")
    print(f"Subtotal: ${subtotal:>6.2f}")

    if discount > 0:
        print(f"Discount: -${discount_amount:>5.2f}")

    print(f"Tax (7%): ${tax:>6.2f}")
    print(f"Total:    ${total:>6.2f}")
    print("====================================")

    # ----- Most Expensive Pizza -----
    max_price = order_prices[0]
    max_pizza = order_descriptions[0]

    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_pizza = order_descriptions[i]

    print("\nMost Expensive Pizza:")
    print(max_pizza, "-", f"${max_price:.2f}")

    # ----- Count Pizzas by Size -----
    print("\nPizza Size Summary:")

    for size in sizes:
        count = 0

        for item in order_descriptions:
            if size in item:
                count += 1

        print(size + ":", count)

    print("\nThank you for your order!")
