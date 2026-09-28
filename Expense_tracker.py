def get_expense():
    description = input("Enter the expense description (or 'done' to finish): ")
    if description == 'done':
        return None
    catagory = input("Enter category: ")
    amount = float(input("Enter amount: "))
    return description, catagory, amount 

total = 0
expenses = []

while True:
    result = get_expense()
    if result is None:
        break
    description, category, amount = result
    total = total + amount
    expenses.append(amount)
    print(f"Logged: {description} (${amount:.2f}) — {category}")

print(f"\nTotal spent: ${total:.2f}")
print(f"Expenses: {expenses}")
tot=sum(expenses)
print(tot)
print(len(expenses))
print(max(expenses))
average = tot / len(expenses)
print(f"Average: ₹{average:.2f}")