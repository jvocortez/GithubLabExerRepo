#Programming Problem 1

#stats.py
def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0

    numbers_copy = sorted(numbers)
    n = len(numbers_copy)
    midpoint = n // 2

    if n % 2 == 1:
        return numbers_copy[midpoint]
    else:
        return (numbers_copy[midpoint] + numbers_copy[midpoint - 1]) / 2
    
def mode(numbers):
    if not numbers:
        return 0

    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    max_count = 0
    mode_value = None
    
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            mode_value = number

    if mode_value is None and numbers:
         return numbers[0]
    elif mode_value is None and not numbers:
         return 0

    return mode_value    

def main():
    fileName = input("Enter the file name: ")
    f = open(fileName, 'r')
    
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))

    print(f"Mean:", mean(numbers))
    print(f"Median:", median(numbers))
    print(f"Mode:", mode(numbers))
    
main()

---------------------------------------------------------

#Programming Problem 2

#LR2_2.py
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please try again.")
        return None
    
def main():
    filename = input("Enter filename: ")
    
    lines = read_file(filename)
    
    if lines is not None:
        num_lines = len(lines)

    while True:
        print(f"\nNumber of lines in the file: {num_lines}")
        line_number = int(input("Enter line number (1 to number of lines, 0 to quit): "))

        if line_number == 0:
            print("Quitting Simulation")
            break
        elif 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1]}")
        else:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()

---------------------------------------------------------

#Programming Problem 3

#generator_modified.py
import random

def getWords(filename):
    fp = open(filename)
    temp_list = list()
    for each_line in fp:
        each_line = each_line.strip()
        temp_list.append(each_line)
    words = tuple(temp_list)
    fp.close()
    return words

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')
    
def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
