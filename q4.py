def stats_decorator(func):
    def wrapper(line):
        numbers = func(line)
        if numbers:
            print("Numbers read:", numbers)
            print("Count of numbers read:", len(numbers))  # This should show the count of numbers per line
            print("Average of numbers:", sum(numbers) / len(numbers))
            print("Maximum of numbers:", max(numbers))
        else:
            print("No valid numbers on this line.")
    return wrapper

@stats_decorator #a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
def process_line(line):
    try:
        return [float(num) for num in line.split()]  # Converts each piece of the line into a number
    except ValueError:
        return []  # Returns an empty list if the line cannot be converted to numbers

def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            process_line(line.strip())

# Example usage
printStats('numbers.txt')
