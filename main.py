with open("amar.txt","a")as f:
  f.write("hello komal\n")
  f.write("how are you\n")
  f.write("hello python\n")
  for line in f:
    print(line,end="")