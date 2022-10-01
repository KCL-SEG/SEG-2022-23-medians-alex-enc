"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def findMedian(numbers):
    numbers = (sorted(numbers))
    middle = len(numbers)//2
    if len(numbers) % 2 == 0:
        if numbers[middle] == numbers[middle - 1]:
            median = numbers[middle]
        else:
            if numbers[middle] - numbers[middle - 1] == 1:
                median = (numbers[middle - 1] + 0.5)
            else:
                median = (f'{numbers[middle - 1]}, {numbers[middle]}')

    else:
        median = numbers[middle]

    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(findMedian(numbers))
