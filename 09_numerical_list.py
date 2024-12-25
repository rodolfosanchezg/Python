#Use a for to generate numbers from 1 to 5, not including 5.
for value in range(1,5):
    print(value)

#Use a for to generate numbers from 1 to 6, not including 6.
for value in range(1,6):
    print(value)

#Create a list of numbers, using range() function
numbers = list(range(1,6))
print(numbers)

#Create a list with even numbers between 2 and 10, including 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Create a list of first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

#Same previous exercise but concise
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

#Some stats functions for lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print(f"Min number: {min(digits)}")
print(f"Max number: {max(digits)}")
print(f"Sum of the numbers: {sum(digits)}")

#List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)