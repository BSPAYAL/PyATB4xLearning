count = 0


def increment():
    global count
    count = count + 1

increment()
print(count) # prints  1

increment()
print(count) #prints 2
