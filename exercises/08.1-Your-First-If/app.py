total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total > int(100):
    print("Give me your money!")
elif total > int(50):
    print("Buy me some coffee you cheap!")
else:
    print("You are a poor guy, go away!")