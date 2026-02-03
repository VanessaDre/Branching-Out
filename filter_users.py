import json


def load_users(file_path="users.json"):
    """Load and return the list of users from the given JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_users(users):
    """Print each user dictionary from a list."""
    for user in users:
        print(user)


def filter_users_by_name(users, name):
    """Return users whose name matches the input name (case-insensitive)."""
    return [
        user
        for user in users
        if user.get("name", "").lower() == name.lower()
    ]


def filter_users_by_age(users, age):
    """Return users whose age matches the given age (exact integer match)."""
    return [user for user in users if user.get("age") == age]


def filter_users_by_email(users, email):
    """Return users whose email matches the input email (case-insensitive)."""
    return [
        user
        for user in users
        if user.get("email", "").lower() == email.lower()
    ]


def main():
    """Run the CLI flow: ask filter option, collect input, print results."""
    users = load_users()

    filter_option = input(
        "Filter by: name, age, or email? "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name: ").strip()
        results = filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        age_input = input("Enter an age (number): ").strip()
        try:
            age_to_search = int(age_input)
        except ValueError:
            print("Invalid age input. Please enter a whole number.")
            return
        results = filter_users_by_age(users, age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email: ").strip()
        results = filter_users_by_email(users, email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
        return

    if not results:
        print("No matching users found.")
        return

    print_users(results)


if __name__ == "__main__":
    main()
