# f =open("kaushik1.txt","w")
# f.write("No kaushik you are good boy")
# f.close()
#************************append
# f =open("kaushik1.txt","a")
# f.write("You cane be the greate\n")
# f.close()
#*******get how many carater we writed
# f =open("kaushik1.txt","a")
# a=f.write("No kaushik you are good boy")
# print(a)
# f.close()
#******************open file for read and write both
f =open("kaushik1.txt","r+")
print(f.read())
f.write("\nyes thankyou")