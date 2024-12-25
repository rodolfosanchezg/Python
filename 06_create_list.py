#Create a list of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#Printing a list
print(bicycles)

#Accessing elements to the list
element = bicycles[1].title()
print(element)

#Last element of the list
last_element = bicycles[-1]
print(last_element)

#Printing values from the list
element = bicycles[3]
print(f"My favorite bike is a {element.title()}")

#Modifying elements in the list
print(bicycles)
bicycles[0] = 'uranium'
print(bicycles)

#Adding elements to the end of the list
bicycles.append('pinarelo')
print(bicycles)

#Adding elements to the begining of the list
bicycles.insert(0, 'monareta')
print(bicycles)

#Adding elements to any part of the list
bicycles.insert(4, 'giant')
print(bicycles)

#Removing elements of the list, using del
del bicycles[3]
print(bicycles)

#Removing last element of the list, using pop
popped_element = bicycles.pop()
print(f"I am not so much fan of {popped_element} bikes.")
print(bicycles)

#Remove any element of the list, using pop
popped_element = bicycles.pop(0)
print(f"A {popped_element} bike is expensive. I don't want it in my list.")
print(bicycles)

#Remove an element by value
bicycles.remove('uranium')
print(bicycles)