with open("tdh.txt","w") as f:
    f.write("this is my first file\n")
    f.write("this program to learn\n")
    f.write("how to deal with file\n")
    f.write("i am learning python")
with open("tdh.txt","r") as f:
    print(f.read())