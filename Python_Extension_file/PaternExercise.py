# print pattern
# input integer n
# Bollen true or false

# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

def Print(n):

    for i in range(1, n):
        print("*" * i)


def Printr(P):
    for i in reversed(range(1,P)):
        print("*" *i)


number= int(input("Enter number for length"))
number2=int(input("Enter number between 1,0"))
if number2==0:
    Printr(number)
elif number2==1:
    Print(number)
else:
    print("something wrong")