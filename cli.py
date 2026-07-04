import requests

BASE_URL = "http://127.0.0.1:5000"


def view_all_items():
    response = requests.get(f"{BASE_URL}/inventory")
    if response.status_code != 200:
        print("Error: Could not fetch inventory.")
        return

    items = response.json().get('inventory', [])
    print("\n--- Inventory ---")
    for item in items:
        print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}")
    print("-----------------\n")


def view_one_item():
    item_id = input("Enter item id: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    if response.status_code == 404:
        print("Item not found.")
        return
    if response.status_code != 200:
        print("Error: Could not fetch item.")
        return

    item = response.json()
    print("\n--- Inventory Item ---")
    print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}")
    print("----------------------\n")


def update_item():
    item_id = input("Enter item id: ")
    field = input("Which field do you want to update? (price/quantity): ").strip().lower()
    if field not in {"price", "quantity"}:
        print("Invalid field. Use 'price' or 'quantity'.")
        return

    new_value = input("Enter new value: ").strip()
    if field == "price":
        try:
            update_data = {"price": float(new_value)}
        except ValueError:
            print("Invalid price value.")
            return
    else:
        try:
            update_data = {"quantity": int(new_value)}
        except ValueError:
            print("Invalid quantity value.")
            return

    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=update_data)
    if response.status_code == 404:
        print("Item not found.")
        return
    if response.status_code != 200:
        print("Error: Could not update item.")
        return

    item = response.json()
    print("\nItem updated successfully.")
    print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}\n")


def main_menu():
    while True:
        print("=== Inventory Management CLI ===")
        print("1. View all items")
        print("2. View one item by id")
        print("3. Update an item")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_all_items()
        elif choice == "2":
            view_one_item()
        elif choice == "3":
            update_item()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main_menu()
