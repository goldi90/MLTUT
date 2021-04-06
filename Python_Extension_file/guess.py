print("Your have only Five time to guess the number ")
SecretNumber = 50
Lnumber = 1
while Lnumber <= 5:
    number = int(input("Enter your number"))
    if number < SecretNumber:
        print("Pls increment the number")
    elif number > SecretNumber:
        print("Pls decrement the number")
    elif number == SecretNumber:
        print(f"You got it  right number is {SecretNumber}")
        print(f" You have taken {Lnumber} of attempts")
        break
    Lnumber=Lnumber+1
print("Done")
