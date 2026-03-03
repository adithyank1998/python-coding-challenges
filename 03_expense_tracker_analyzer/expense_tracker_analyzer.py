def get_number_of_expenses():
    """Get valid number of expenses from user."""
    while True:
        try:
            count = int(input("How many expenses? "))
            if count <= 0:
                print("Please enter a positive number.")
            else:
                return count
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def collect_expenses(count):
    """
    Collect expense data from user.
    Returns a dictionary with category-wise totals
    and a list of all individual expense amounts.
    """
    expenses = {}
    all_amounts = []

    for _ in range(count):
        category = input("Category: ").strip()

        while True:
            try:
                amount = float(input("Amount: "))
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        all_amounts.append(amount)

    return expenses, all_amounts


def analyze_expenses(expenses, all_amounts):
    """Calculate total, highest, lowest, and average."""
    total_expense = sum(all_amounts)
    average_expense = total_expense / len(all_amounts)

    highest_category = max(expenses, key=expenses.get)
    lowest_category = min(expenses, key=expenses.get)

    return total_expense, average_expense, highest_category, lowest_category


def display_results(expenses, total, average, highest, lowest):
    """Display formatted expense analysis."""
    print("\n----- Expense Summary -----")
    print(f"Total Expense: {total:.2f}\n")

    print("Category-wise:")
    for category, amount in expenses.items():
        print(f"{category} -> {amount:.2f}")

    print(f"\nHighest Expense Category: {highest}")
    print(f"Lowest Expense Category: {lowest}")
    print(f"Average Expense: {average:.2f}")


def main():
    """Main function to run the program."""
    while True:
        count = get_number_of_expenses()
        expenses, all_amounts = collect_expenses(count)

        total, average, highest, lowest = analyze_expenses(expenses, all_amounts)

        display_results(expenses, total, average, highest, lowest)

        repeat = input("\nDo you want to run again? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting Expense Tracker. Goodbye!")
            break


if __name__ == "__main__":
    main()