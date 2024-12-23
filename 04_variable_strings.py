#Using variables in Strings
firstName = "rodolfo"
lastName = "sanchez"
fullName = f"{firstName} {lastName}"
print(fullName)

#Adding text without a variable
print(f"Hello, {firstName} {lastName}")

#Fixing some typos
print(f"Hello, {firstName.title()} {lastName.title()} ")

#Same but as variable
message = f"Hello, {fullName.title()}"
print(message)

#Alternative for Python 3.5 and older
formattedFullName = "{} {}".format(firstName, lastName)
print(formattedFullName)