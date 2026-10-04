correct_username = "admin"
correct_password = "python123"

attempts = 0

while attempts < 3:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        print("Fields cannot be empty.")
        continue

    attempts += 1

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break

    print("Incorrect username or password.")
    print("Attempts left:", 3 - attempts)

else:
    print("Too many failed attempts. Account locked.")
