low=0;high=100
life=5
for i in range(life):
    guess=(low+high)//2
    print(f"number of tries you have left {life-i}")
    print(f"my guess is {guess}")
    user_input=input("enter lesser,greater,equal\n")
    if user_input=="greater":
        low=guess
    elif  user_input=="lesser":
       high=guess
    elif user_input=="equal":
       print("i am win")
       break

else:
    print("i lose")