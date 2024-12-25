#Create a list
og_cars = ['bmw', 'audi', 'toyota', 'subaru']
print(og_cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

#Sorting permanently with sort() method
cars.sort()
print(cars)

#Sorting reverse
cars.sort(reverse=True)
print(cars)

#Sorting the list temporarily with sorted() method
print("\nThis is the original list...")
print(og_cars)

print("\nTemporarily sorted list")
print(sorted(og_cars))

print("\nTemporarily sorted list, in reverse")
print(sorted(og_cars,reverse=True))

print("\nThe original list again...")
print(og_cars)

#Print the list in reverse order
og_cars.reverse()
print(og_cars)

#Printing back in the original order
og_cars.reverse()
print(og_cars)

#Finding the length of a list
print(len(og_cars))