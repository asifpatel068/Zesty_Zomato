import json
from tkinter import Tk, Label, Entry, Button, messagebox

# Step 1: Load the menu data from the JSON file

def load_menu():
    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)
            return menu
    except FileNotFoundError:
        return []

# Step 2: Load the order data from the JSON file

def load_orders():
    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)
            return orders
    except FileNotFoundError:
        return []

# Step 3: Save the menu data to the JSON file

def save_menu(menu):
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=4)

# Step 4: Save the order data to the JSON file

def save_orders(orders):
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=4)

# Step 5: Create a window to add a new dish

def add_dish():
    dish_window = Tk()
    dish_window.title("Add New Dish")

    # Create labels and entry fields for dish details using Tkinter
    dish_id_label = Label(dish_window, text="Dish ID:")
    dish_id_entry = Entry(dish_window)
    dish_id_label.pack()
    dish_id_entry.pack()

    dish_name_label = Label(dish_window, text="Dish Name:")
    dish_name_entry = Entry(dish_window)
    dish_name_label.pack()
    dish_name_entry.pack()

    price_label = Label(dish_window, text="Price:")
    price_entry = Entry(dish_window)
    price_label.pack()
    price_entry.pack()

    availability_label = Label(dish_window, text="Availability:")
    availability_entry = Entry(dish_window)
    availability_label.pack()
    availability_entry.pack()

    def add_dish_to_menu():
        dish_id = dish_id_entry.get()
        dish_name = dish_name_entry.get()
        price = price_entry.get()
        availability = availability_entry.get()

        new_dish = {
            "dish_id": dish_id,
            "dish_name": dish_name,
            "price": price,
            "availability": availability
        }

        menu.append(new_dish)
        save_menu(menu)

        dish_window.destroy()

        messagebox.showinfo("Zesty Zomato", "Dish added to the menu successfully!")

    add_button = Button(dish_window, text="Add Dish", command=add_dish_to_menu)
    add_button.pack()

    dish_window.mainloop()

# Step 6: Remove a dish from the menu

def remove_dish():
    dish_window = Tk()
    dish_window.title("Remove Dish")

    dish_id_label = Label(dish_window, text="Dish ID:")
    dish_id_entry = Entry(dish_window)
    dish_id_label.pack()
    dish_id_entry.pack()

    def remove_dish_from_menu():
        dish_id = dish_id_entry.get()

        for dish in menu:
            if dish['dish_id'] == dish_id:
                menu.remove(dish)
                save_menu(menu)

                dish_window.destroy()

                messagebox.showinfo("Zesty Zomato", "Dish removed from the menu successfully!")
                return

        messagebox.showwarning("Zesty Zomato", "Dish not found in the menu!")

    remove_button = Button(dish_window, text="Remove Dish", command=remove_dish_from_menu)
    remove_button.pack()

    dish_window.mainloop()

# Step 7: Update the availability of a dish

def update_availability():
    dish_window = Tk()
    dish_window.title("Update Dish Availability")

    dish_id_label = Label(dish_window, text="Dish ID:")
    dish_id_entry = Entry(dish_window)
    dish_id_label.pack()
    dish_id_entry.pack()

    availability_label = Label(dish_window, text="Availability (yes/no):")
    availability_entry = Entry(dish_window)
    availability_label.pack()
    availability_entry.pack()

    def update_dish_availability():
        dish_id = dish_id_entry.get()
        availability = availability_entry.get().lower()

        for dish in menu:
            if dish['dish_id'] == dish_id:
                if availability == 'yes':
                    dish['availability'] = True
                elif availability == 'no':
                    dish['availability'] = False

                save_menu(menu)

                dish_window.destroy()

                messagebox.showinfo("Zesty Zomato", "Availability updated successfully!")
                return

        messagebox.showwarning("Zesty Zomato", "Dish not found in the menu!")

    update_button = Button(dish_window, text="Update Availability", command=update_dish_availability)
    update_button.pack()

    dish_window.mainloop()


# Step 8: Create the Tkinter window

window = Tk()
window.title("Zesty Zomato")

# Step 9: Create labels, entry fields, and buttons using Tkinter
menu_label = Label(window, text="Menu:")
menu_label.pack()

menu = load_menu()

for dish in menu:
    dish_label = Label(window, text=f"ID: {dish['dish_id']} - Name: {dish['dish_name']} - Price: {dish['price']} - Availability: {'Available' if dish['availability'] else 'Not Available'}")
    dish_label.pack()

add_dish_button = Button(window, text="Add Dish", command=add_dish)
add_dish_button.pack()

remove_dish_button = Button(window, text="Remove Dish", command=remove_dish)
remove_dish_button.pack()

update_availability_button = Button(window, text="Update Availability", command=update_availability)
update_availability_button.pack()

# Step 10: Define the functions for each button

def take_order():
    order_window = Tk()
    order_window.title("Take New Order")

    # Create labels and entry fields for order details using Tkinter
    customer_label = Label(order_window, text="Customer Name:")
    customer_entry = Entry(order_window)
    customer_label.pack()
    customer_entry.pack()

    dish_ids_label = Label(order_window, text="Dish IDs (comma-separated):")
    dish_ids_entry = Entry(order_window)
    dish_ids_label.pack()
    dish_ids_entry.pack()

    def process_order():
        customer_name = customer_entry.get()
        dish_ids = dish_ids_entry.get().split(",")

        ordered_dishes = []
        for dish_id in dish_ids:
            for dish in menu:
                if dish['dish_id'] == dish_id.strip() and dish['availability']:
                    ordered_dishes.append(dish)

        if ordered_dishes:
            order_data = {
                "customer_name": customer_name,
                "dishes": ordered_dishes,
                "status": "received"
            }

            orders.append(order_data)
            save_orders(orders)

            order_window.destroy()

            messagebox.showinfo("Zesty Zomato", "Order placed successfully!")
        else:
            messagebox.showwarning("Zesty Zomato", "No dishes available for the order!")

    process_order_button = Button(order_window, text="Process Order", command=process_order)
    process_order_button.pack()

    order_window.mainloop()

# Step 11: Update the status of an order

def update_order_status():
    order_window = Tk()
    order_window.title("Update Order Status")

    order_id_label = Label(order_window, text="Order ID:")
    order_id_entry = Entry(order_window)
    order_id_label.pack()
    order_id_entry.pack()

    status_label = Label(order_window, text="New Status:")
    status_entry = Entry(order_window)
    status_label.pack()
    status_entry.pack()

    def update_order():
        order_id = order_id_entry.get()
        new_status = status_entry.get()

        for order in orders:
            if order['order_id'] == order_id:
                order['status'] = new_status
                save_orders(orders)

                order_window.destroy()

                messagebox.showinfo("Zesty Zomato", "Order status updated successfully!")
                return

        messagebox.showwarning("Zesty Zomato", "Order not found!")

    update_button = Button(order_window, text="Update Order", command=update_order)
    update_button.pack()

    order_window.mainloop()


def review_orders():
    orders_window = Tk()
    orders_window.title("Review Orders")

    orders_label = Label(orders_window, text="Orders:")
    orders_label.pack()

    orders = load_orders()

    for order in orders:
        order_label = Label(orders_window, text=f"Order ID: {order['order_id']} - Customer:{order['customer_name']} - Status: {order['status']}")
        order_label.pack()

    orders_window.mainloop()

# Step 12: Bind the functions to the buttons using Tkinter

take_order_button = Button(window, text="Take Order", command=take_order)
take_order_button.pack()

update_order_status_button = Button(window, text="Update Order Status", command=update_order_status)
update_order_status_button.pack()

review_orders_button = Button(window, text="Review Orders", command=review_orders)
review_orders_button.pack()

# Step 13: Run the Tkinter event loop

window.mainloop()
