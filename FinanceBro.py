def add_expense(expenses):
    try:
        exName = input("Enter the name of the expense: ")
        exAmount = float(input("Enter the amount: "))
        expenses.append((exName, exAmount))
        print(f"Expense '{exName}' of amount ${exAmount:.2f} added to your expenses successfully!!")
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")

def view_expenses(expenses):
    if not expenses:
        print("No record of any expenses yet!")
    else:
        print("\nRecord of expenses:")
        for index, (exName, exAmount) in enumerate(expenses, 1):
            print(f"{index}. {exName}: ${exAmount:.2f}")
    print("\n")

def total_expenses(expenses):
    total = sum(exAmount for _, exAmount in expenses)
    print(f"The total of your expenses is: ${total:.2f}\n")

def main():
    expenses = []
    while True:
        print("\nTrack your money!!")
        print("Choose a number to:")
        print("1: Add expense\n2: View all recorded expenses\n3: Get total expenses\n4: Exit\n")
        pick = input("What do you want to do? (options from 1-4): ")

        if pick == '1':
            add_expense(expenses)
        elif pick == '2':
            view_expenses(expenses)
        elif pick == '3':
            total_expenses(expenses)
        elif pick == '4':
            print("Exiting!! Bye :)")
            break
        else:
            print("Invalid choice :( Please pick from 1 to 4\n")

if __name__ == "__main__":
    main()
