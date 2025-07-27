# Database Admin Program

A simple console-based Python application that simulates logging into a database and allows users to change their password.  
If the admin logs in, the program displays all usernames and passwords.

## Features

- User login with username and password
- Password change option for non-admin users (minimum 8 characters required)
- Admin view: displays all usernames and passwords
- Input validation and clear user feedback

## Valid Usernames and Passwords

| Username   | Password     |
|------------|--------------|
| user01     | password01   |
| user02     | password02   |
| user03     | password03   |
| admin00    | adminpass    |

## How to Use

1. **Clone the repository:**
   ```
   git clone https://github.com/KekoFigueroa-dev/database_admin_program.git
   ```

2. **Navigate to the project directory:**
   ```
   cd database_admin_program
   ```

3. **Run the program:**
   ```
   python databaseadmin.py
   ```

4. **Follow the prompts:**
   - Enter your username and password.
   - If you are not the admin, you can choose to change your password.
   - If you are the admin (`admin00`), you will see all users and their passwords.

## Example Output

```
Welcome to my Database Admin Program!
Enter your username: user01
Enter your password: password01
Hello user01, welcome to the database admin program!

Hello user01! You are Logged in!
Do you want to change your password? (yes/no): yes
Enter your new password (at least 8 characters): newpass123
Your password has been changed successfully! New password: newpass123
```

## Requirements

- Python 3.x

## License

This project is open source and available under the