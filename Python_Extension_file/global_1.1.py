# l=10 #global
# def function1(n):
#     # l=5 #local
#     global l
#     l=5
#     m=8
#     print(l,m)
#     print(n,"I have printed")
# function1("Thi is me")

def kaushik():
    x = 20

    def harsh():
        global x
        x = 80
    print("before calling harsh function", x)
    harsh()
    print("after calling harsh function", x)

kaushik()