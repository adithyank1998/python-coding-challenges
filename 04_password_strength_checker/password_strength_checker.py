def check_password_rules(password):
    """Check password conditions and return results."""

    length_rule = len(password) >= 8
    upper_rule = False
    lower_rule = False
    digit_rule = False
    special_rule = False

    special_characters = "!@#$%^&*"

    for char in password:
        if char.isupper():
            upper_rule = True
        elif char.islower():
            lower_rule = True
        elif char.isdigit():
            digit_rule = True
        elif char in special_characters:
            special_rule = True

    rules = {
        "Minimum 8 characters": length_rule,
        "Uppercase letter": upper_rule,
        "Lowercase letter": lower_rule,
        "Number": digit_rule,
        "Special character": special_rule
    }

    return rules


def determine_strength(rules):
    """Determine password strength based on satisfied rules."""
    satisfied = sum(rules.values())

    if satisfied == 5:
        return "Strong"
    elif satisfied >= 3:
        return "Medium"
    else:
        return "Weak"


def show_missing_rules(rules):
    """Display which password rules are missing."""
    missing = [rule for rule, status in rules.items() if not status]

    if missing:
        print("\nMissing requirements:")
        for rule in missing:
            print(f"- {rule}")


def main():
    """Main program loop."""
    while True:
        password = input("Enter password: ")

        rules = check_password_rules(password)
        strength = determine_strength(rules)

        print(f"\nPassword Strength: {strength}")

        if strength != "Strong":
            show_missing_rules(rules)

        if strength == "Strong":
            break

        retry = input("\nTry again? (y/n): ").lower()
        if retry != "y":
            break


if __name__ == "__main__":
    main()