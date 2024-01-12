print('Enter the type of vehicle')
print('enter c for car \n enter b for bus \n enter t for truck \n enter s for scooter \n enter m for motor bike')

vehicle = int(input('enter your choice'))

time = int(input('enter number of hours'))

if vehicle == "t" or vehicle == "b":

    print(time * 20)

elif vehicle == "c" :

    print(time * 10)

elif vehicle == "s" or vehicle == "m":

    print(time * 5)

else:

    print("Wrong choice")
