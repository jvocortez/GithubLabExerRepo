#Programming Problem 1

#stats.py
def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

def mode(numbers):
    if not numbers:
        return None

    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = 0
    mode_value = None

    for number, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            mode_value = number
    return mode_value

import stats

my_numbers = [7, 4, 1, 2, 8, 1, 3, 9, 3]

average = stats.mean(my_numbers)
middle_value = stats.median(my_numbers)
most_frequent = stats.mode(my_numbers)

print(f"The mean of {my_numbers} is: {average}")
print(f"The median of {my_numbers} is: {middle_value}")
print(f"The mode of {my_numbers} is: {most_frequent}")

------------------------------------------------------------

#Programming Problem 2

def navigate_file():
    while True:
        filename = input("Enter the filename (or 'quit' to exit): ")
        if filename.lower() == 'quit':
            print("Exiting program.")
            return

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            break
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    num_lines = len(lines)
    print(f"The file '{filename}' has {num_lines} lines.")

    while True:
        try:
            line_number_str = input(f"Enter a line number (1 to {num_lines}, or 0 to quit): ")
            line_number = int(line_number_str)

            if line_number == 0:
                print("Quitting Simulation")
                break
            elif 1 <= line_number <= num_lines:
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print(f"Invalid line number. Please enter a number between 1 and {num_lines}, or 0 to quit.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    navigate_file()
