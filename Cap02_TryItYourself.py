#Save each of the following exercises as a separate file with a name like
#name_cases.py. If you get stuck, take a break or see the suggestions in
#Appendix C.

#2-1. Simple Message: Assign a message to a variable, and then print that
#message.

message = 'This is the solution of the exercise on page 19.'
print(message)

#2-2. Simple Messages: Assign a message to a variable, and print that message.
#Then change the value of the variable to a new message, and print the new
#message.

variable = 'This is the first message'
print(variable)
variable = 'This is a different message in the same variable'
print(variable)

#2-3. Personal Message: Use a variable to represent a person’s name, and print
#a message to that person. Your message should be simple, such as, “Hello Eric,
#would you like to learn some Python today?”

userName = 'Eric'
print(f"Hello {userName}, would you like to learn some Python today?")

#2-4. Name Cases: Use a variable to represent a person’s name, and then print
#that person’s name in lowercase, uppercase, and title case.

personName = 'ruperto gonzalez'
print(f"{personName}")
print(f"{personName.lower()}")
print(f"{personName.upper()}")
print(f"{personName.title()}")

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the
#quote and the name of its author. Your output should look something like the
#following, including the quotation marks:
#   Albert Einstein once said, “A person who never made a
#   mistake never tried anything new.”

message = '\tAlbert Einstein once said, "A person who never made a\n\tmistake never tried anything new"'
print(message)

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
#famous person’s name using a variable called famous_person. Then compose
#your message and represent it with a new variable called message. Print your
#message.

famous_person = 'harry callahan'
quote = '"Go ahead, make my day."'
message = f"{quote} - {famous_person.title()}"
print(message)

