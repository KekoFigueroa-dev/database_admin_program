"""
Database Admin Program

Simulates a simple user login system with password management.
- Users can log in with their credentials.
- Non-admin users can change their password (minimum 8 characters).
- Admin user can view all usernames and passwords.
"""

# Print welcome message
print("Welcome to my Database Admin Program!")

# Initialize user database with usernames and passwords
user_database = {
    "user01": "password01",
    "user02": "password02",
    "user03": "password03",
    "admin00": "adminpass",
}

# Prompt for username input
username = input("Enter your username: ").strip().lower()

# Validate username existence; exit if not found
if username not in user_database.keys():
    print("Username not found. Please try again.")

# Prompt for password input
password = input("Enter your password: ").strip().lower()

# Validate password; exit if incorrect
if password != user_database[username]:
    print("Incorrect password. Please try again.")
else:
    print(f"Hello {username}, welcome to the database admin program!")

# If admin, display all usernames and passwords
if username == "admin00":
    print("\nHello Admin! Here are the current users and their passwords:")
    for user, pwd in user_database.items():
        print(f"Username: {user}, \tPassword: {pwd}")

# If non-admin, offer password change option
if username != "admin00":
    print(f"\nHello {username}! You are logged in!")
    change_password = input("Do you want to change your password? (yes/no): ").strip().lower()
    if change_password == "yes":
        new_password = input("Enter your new password (at least 8 characters): ").strip()
        # Update password if it meets length requirement
        if len(new_password) >= 8:
            user_database[username] = new_password
            print(f"Your password has been changed successfully! New password: {new_password}")
        else:
            print(f"Password too short. Your old password remains: {user_database[username]}")
    else:
        print("Goodbye!")