import os
with open("demofile.txt","a") as f:
    f.write("\nNow the file has more content!")
with open("demofile.txt","r") as f:
    print(f.read())
with open("demofile.txt","w") as f:
    f.write("Woops! I have deleted the content!")
with open("demofile.txt","r") as f:
    print(f.read())
f=open("myfile.txt","x")
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")
