#How to use nonoprinting characters to organize the output of a text
message = "Python"
print(message)

#Use of Tab \tab
message = "\tPython"
print(message)

#Use of newline \n
message = "Languages:\nPython\nC\nJavaScript"
print(message)

#Combine \n and \t
message = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(message)

#Eliminate extraspace at the end of the string with .rstrip() method
username = "plopez77 "
print(username)
print(len(username))
print(username.rstrip())
print(len(username.rstrip()))