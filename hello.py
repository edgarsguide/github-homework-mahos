import time
hour = time.localtime().tm_hour

# set greeting depending on time
if hour > 4 and hour < 12:
    greeting = "Morning,"
elif hour == 12:
    greeting = "What's for lunch"
elif hour > 12 and hour < 18:
    greeting = "Good afternoon,"
elif hour >= 18:
    greeting = "Good evening"
else:
    greeting = "It's bed time,"

name = input("Hi, what's your name?")

print("{} {}!".format(greeting, name))

