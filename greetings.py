greetings = input()
#print(greetings)
firstGreetings = greetings[0]
lastGreetings = greetings[len(greetings) - 1]
# print(firstGreetings)
# print(lastGreetings)
numberOfE = 0
for i in greetings:
    if i == 'e':
        numberOfE += 1
replyE = numberOfE * 2 * ('e')
print(replyE)
reply = firstGreetings + replyE + lastGreetings
print(reply)


