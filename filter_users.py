import json


def filter_users_by_name(name):
    """Loads the full users list from the JSON file.
    Then prints only users whose name matches (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)

    # Filter list: keep users where the "name" matches the input name.
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    # Print each matching user (as a dictionary).
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Loads users from JSON and prints only those with the exact given age."""
    with open("users.json", "r") as file:
        users = json.load(file)

    # Using user.get("age") avoids a KeyError if a user has no "age" field.
    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Loads users from JSON and prints only users whose email matches
    (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    """Ask the user what they want to filter by, then route to the correct function."""
    filter_option = input(
        "What would you like to filter by? (Currently, name, age, email are supported): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        # Convert input to int because ages in the JSON are numbers.
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
