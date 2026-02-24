def number_frequency_analyzer():
    while True:
        user_input = input("\nEnter numbers (comma-separated): ")

        try:
            number_list = user_input.replace(" ", "").split(",")

            numbers = []
            for num in number_list:
                if num == "":
                    continue
                numbers.append(int(num))

            if len(numbers) == 0:
                print("No valid numbers entered.")
                continue

        except ValueError:
            print("Invalid input! Please enter only comma-separated integers.")
            continue

        frequency = {}

        for num in numbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        sorted_frequency = sorted(
            frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("\nFrequency:")
        for num, count in sorted_frequency:
            if count == 1:
                print(f"{num} -> {count} time")
            else:
                print(f"{num} -> {count} times")

        max_freq = max(frequency.values())
        min_freq = min(frequency.values())

        most_frequent = []
        least_frequent = []

        for num, count in frequency.items():
            if count == max_freq:
                most_frequent.append(num)
            if count == min_freq:
                least_frequent.append(num)

        print("\nMost Frequent:", ", ".join(map(str, most_frequent)))
        print("Least Frequent:", ", ".join(map(str, least_frequent)))
        print("Total Unique Numbers:", len(frequency))

        choice = input("\nDo you want to try again? (y/n): ").lower()
        if choice != 'y':
            print("Program ended.")
            break


number_frequency_analyzer()