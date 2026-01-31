f=open("demofile.txt")
print(f.read())
f.close()

with open("demofile.txt","r") as f:
    print(f.read(7))
    print(f.readline())
    print(f.readline())