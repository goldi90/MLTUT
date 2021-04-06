f = open("kaushik.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(0)
print(f.readline())
f.close()

# f.tell which line are we
# f.seek put on that chatacter 