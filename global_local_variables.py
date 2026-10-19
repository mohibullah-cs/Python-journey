username = "Mohib"  # Global variable
total_points = 100


def show_profile():
    # Accessing a global variable
    print(f"Username: {username}")

    # Local variable
    level = "Beginner"
    print(f"Level: {level}")


def update_points():
    global total_points
    total_points += 50
    print(f"Updated Points: {total_points}")


show_profile()
update_points()

print(f"Final Points: {total_points}")
