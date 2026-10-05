balance = 10000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful!")
    print(f"Remaining balance: Rs. {balance:.2f}")

except ValueError as e:
    print("Transaction failed:", e)

except Exception as e:
    print("Unexpected error:", e)
