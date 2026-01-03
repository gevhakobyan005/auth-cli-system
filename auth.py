users = {
    "student": "Password123",
    "admin": "AdminPass"
}

def login(username, password):
    if not username or not password:
        return "Username and password cannot be empty."

    if username not in users:
        return "Invalid username."

    if users[username] != password:
        return "Invalid password."

    return "Login successful!"


def main():
    print("Welcome to the Authentication System")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    result = login(username, password)
    print(result)


if __name__ == "__main__":
    main()