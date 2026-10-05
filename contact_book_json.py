import json

contacts = {
    "Ali": {
        "phone": "03001234567",
        "email": "ali@example.com"
    },
    "Ahmed": {
        "phone": "03111234567",
        "email": "ahmed@example.com"
    }
}

# Convert Python dictionary to JSON
json_data = json.dumps(contacts, indent=4)

print("Contact Data:")
print(json_data)

# Convert JSON back to Python dictionary
data = json.loads(json_data)

print("\nAli's Phone:", data["Ali"]["phone"])
print("Ahmed's Email:", data["Ahmed"]["email"])

Description:
This project demonstrates how Python dictionaries can be converted into JSON using "json.dumps()" and converted back using "json.loads()". It simulates a simple contact book and shows how structured information can be stored and accessed using JSON.

---

2. Exception Handling — ATM Simulator

GitHub file name: "atm_exception_handling.py"

:::writing{variant="document" id="74106" title="ATM Simulator — Exception Handling"}

balance = 10000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount

    print(f"Withdrawal successful!")
    print(f"Remaining balance: Rs. {balance:.2f}")

except ValueError as e:
    print("Transaction failed:", e)

except Exception as e:
    print("Unexpected error:", e)
