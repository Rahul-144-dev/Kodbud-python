contacts = []


def show_menu():
    print("\n=== Contact Book ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search by name")
    print("4. Delete contact")
    print("5. Exit")


def get_choice():
    while True:
        choice = input("Choose (1-5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice
        print("Invalid choice. Enter a number 1-5.")


def add_contact():
    print("\n--- Add Contact ---")
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"Contact '{name}' already exists.")
            return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"✅ Added '{name}'.")


def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts yet.")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def search_contact():
    print("\n--- Search Contact ---")
    if not contacts:
        print("No contacts to search.")
        return

    query = input("Search name: ").strip().lower()
    if not query:
        print("Empty search.")
        return

    matches = [c for c in contacts if query in c["name"].lower()]

    if not matches:
        print(f"No contact found matching '{query}'.")
        return

    print(f"Found {len(matches)} match(es):")
    for c in matches:
        print(f"  {c['name']} | {c['phone']} | {c['email']}")


def delete_contact():
    print("\n--- Delete Contact ---")
    if not contacts:
        print("No contacts to delete.")
        return

    name = input("Name to delete: ").strip().lower()
    if not name:
        print("Empty name.")
        return

    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            confirm = input(f"Delete '{c['name']}'? (y/n): ").lower().strip()
            if confirm == "y":
                contacts.pop(i)
                print(f"🗑️  Deleted '{c['name']}'.")
            else:
                print("Cancelled.")
            return

    print(f"No contact named '{name}'.")


def main():
    print("Welcome to your Contact Book!")

    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
