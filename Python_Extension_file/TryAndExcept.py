print("Enter num1")
num1 = input()
print("Enter num1")
num2 = input()
try:
    print("The sum of two number is", int(num1) + int(num2))
# if user entered alphabet instated of Number than   line 8 will not execute but we have to execute next line to
# it . We dont to stop execution of script so we use try Except
# print("This is very important")
except Exception as e:
    print(e)

print("This is very important")
