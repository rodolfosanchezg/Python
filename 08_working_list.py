#Create a list 
magicians = ['alice', 'david', 'carolina']

#Printing every item of the list
for magician in magicians: 
    print(magician)

#Doing more work within for a Loop
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Doing something After a for Loop
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

