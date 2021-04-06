# File I/O Basics
"""
"r"= open file for reading
"w"= open file for reading
"x"= Create file if not exist
"a"= Add more content to a file
"t"= text mode -default
"b"= binary
"+"= read and write

"""
# To read function doc
# print(sum.__doc__)
# ************************* Read file good practice to close
# print("Printed using read Function")
f = open("kaushik.txt")
# content = f.read()  # can insert number of line to read in read function
# print(content)

# f.close()
# **************************Printed using for loop
# print("Printed using for loop")
# f = open("kaushik.txt")
# for line in f:
#     print(line)
# **************************Printed using for readline
# print("Printed using for readline")
# print(f.readline())
# print(f.readline())
# **************************Printed using for readlines
print("Printed using for readlines")

print(f.readlines())