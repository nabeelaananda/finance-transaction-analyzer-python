data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for index, transaction in enumerate(transactions):
    amount, statement = transaction
    print(f"{index + 1}. ${amount:,.2f} - {statement}")

def print_summary(transactions):
  if not transactions:
      print("\nNo transactions available.")
      return
      
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"\nTotal Deposited: ${total_deposited:,.2f}")

  withdrawal = [transaction[0] for transaction in transactions if transaction[0] <= 0]
  total_withdrawn = sum(withdrawal)
  print(f"Total Withdrawn: ${total_withdrawn:,.2f}")

  balance = total_deposited + total_withdrawn
  print(f"Current Balance: ${balance:,.2f}")

def analyze_transactions(transactions):
  if not transactions:
      print("\nNo transactions available.")
      return

  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"\nLargest deposit: ${largest_deposit[0]:,.2f} ({largest_deposit[1]})")
  print(f"Largest withdrawal: ${largest_withdrawal[0]:,.2f} ({largest_withdrawal[1]})")

  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  average_deposited = total_deposited/len(deposits) if deposits else 0
  print(f"Average deposit: ${average_deposited:,.2f}")

  withdrawal = [transaction[0] for transaction in transactions if transaction[0] <= 0]
  total_withdrawn = sum(withdrawal)
  average_withdrawal = total_withdrawn/len(withdrawal) if withdrawal else 0
  print(f"Average withdrawal: ${average_withdrawal:,.2f}")

def add_transaction(transactions):
  print("\n--- Add New Transaction ---")
  try:
    amount = float(input("Enter amount (positive for income, negative for expense): "))
    statement = input("Enter transaction description: ")
    transactions.append((amount, statement))
    print(f"Successfully added: ${amount:,.2f} - {statement}")
  except ValueError:
    print("Error: Invalid amount. Please enter numbers only.")

def delete_transaction(transactions):
  print_transactions(transactions) 
  if not transactions:
      return
  try:
    index_to_delete = int(input("\nEnter the number of the transaction to delete: ")) - 1
    if 0 <= index_to_delete < len(transactions):
      removed_transaction = transactions.pop(index_to_delete)
      print(f"Successfully deleted: ${removed_transaction[0]:,.2f} - {removed_transaction[1]}")
    else:
      print("Error: Transaction number not found.")
  except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

while True:
  print("\nChoose an option:")
  print("1. Print summary (type 'print')")
  print("2. Analyze transactions (type 'analyze')")
  print("3. View all transactions (type 'list')")
  print("4. Add a transaction (type 'add')")
  print("5. Delete a transaction (type 'delete')")
  print("6. Stop program (type 'stop')")
  
  choice = input("Enter your option: ").lower()
  
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "list":
    print_transactions(data)
  elif choice == "add":
    add_transaction(data)
  elif choice == "delete":
    delete_transaction(data)
  elif choice == "stop":
    print("Exiting program. Have a great day!")
    break
  else:
    print("Invalid choice, please try again.")
