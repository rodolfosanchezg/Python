#Try these short programs to get some firsthand experience with Python’s lists.
#You might want to create a new folder for each chapter’s exercises to keep
#them organized.

#3-1. Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.

names = ['pepo', 'camilo', 'chiqui', 'marto', 'vicho']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.

print(f"Bienvenido a mi lista {names[0]}. Espero verte pronto.")
print(f"Oye, {names[1]}, recuerda que mañana es el partido.")
print(f"{names[2]}, te estuvo llamando tu hermana. Llamala pronto.")
print(f"Querido {names[3]}, me alegro de verte!")
print(f"Hola, {names[4]}. ¿Que deseas hacer hoy?")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”

statements = ['I would like to own a Honda motorcyle.', 'A Toyota Supra is my favorite sport car.', 'A Nissan Xtrail EPower is a nice car to have.']
print(statements[0])
print(statements[1])
print(statements[2])

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.

invitees = ['David Bacon', 'Roberto Calorias', 'Redondinho', 'Tony Croissant', 'Macarooney']
print(invitees[0])
print(invitees[1])
print(invitees[2])
print(invitees[3])
print(invitees[4])

#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still
#in your list.

invitees = ['David Bacon', 'Roberto Calorias', 'Redondinho', 'Tony Croissant', 'Macarooney']
print(invitees[0])
print(invitees[1])
print(invitees[2])
print(invitees[3])
print(invitees[4])
print(f"Unfortunately, {invitees[2]} cannot join us to our dinner")
invitees[2] = 'Diego Armando Arahona'
print(invitees[0])
print(invitees[1])
print(invitees[2])
print(invitees[3])
print(invitees[4])

#3-6. More Guests: You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#call to the end of your program informing people that you found a bigger
#dinner table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

print(invitees[0])
print(invitees[1])
print(invitees[2])
print(invitees[3])
print(invitees[4])
print("There's more room to our dinner meeting! I found a bigger dinner table.")
invitees.append('Yuca Toni')
invitees.insert(0,'Cabezon Ruggeri')
invitees.insert(3,'Cristiano Farsardo')
print(invitees[0])
print(invitees[1])
print(invitees[2])
print(invitees[3])
print(invitees[4])
print(invitees[5])
print(invitees[6])
print(invitees[7])

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a
#message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.
#• Print a message to each of the two people still on your list, letting them
#know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty
#list. Print your list to make sure you actually have an empty list at the end
#of your program.

print("Unfortunately, I can afford just 2 invitees today.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
popped_invitee = invitees.pop()
print(f"I'm sorry, {popped_invitee}. Let's make it another time.")
print(f"We are still on time, {invitees[0]}.")
print(f"We are still on time, {invitees[1]}.")
del invitees[0]
del invitees[0]
print(invitees)