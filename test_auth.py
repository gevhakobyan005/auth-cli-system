from auth import login

def test_valid_login():
    assert login("student", "Password123") == "Login successful!"

def test_wrong_password():
    assert login("student", "wrong") == "Invalid password."

def test_wrong_username():
    assert login("unknown", "Password123") == "Invalid username."

def test_empty_fields():
    assert login("", "") == "Username and password cannot be empty."