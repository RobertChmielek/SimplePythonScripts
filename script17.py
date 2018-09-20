Age=int(input("How old are you?"))
if Age >= 18:
    print("You can vote")
elif Age == 17:
    print("You can learn to drive")
elif Age == 16:
    print("You can buy a lottery ticket")
elif Age < 16:
    print("You can go Trick-or-Treating")