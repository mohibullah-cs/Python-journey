import requests

expenses = [
    {"item": "Food", "amount": 500},
    {"item": "Transport", "amount": 300},
    {"item": "Books", "amount": 1000}
]

total = sum(expense["amount"] for expense in expenses)

print("Expense Tracker")
print("-" * 25)

for expense in expenses:
    print(f"{expense['item']}: Rs. {expense['amount']}")

print("-" * 25)
print(f"Total Expenses: Rs. {total}")

# Example of using an external package installed with pip
response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("\nInternet connection is working!")
else:
    print("\nCould not connect to the internet.")
