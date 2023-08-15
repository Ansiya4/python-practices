import os
f = open("C:\\Users\\hp\\Desktop\\sample.txt", "w")
f.write("bye................")
f = open("C:\\Users\\hp\\Desktop\\sample.txt", "r")
print(f.read())
f.close()
new = open("C:\\Users\\hp\\Desktop\\learn python\\new.text","w")
new.write("haiiiiii")
new = open("C:\\Users\\hp\\Desktop\\learn python\\new.text","r")

for x in new:
    print(x)
os.remove("C:\\Users\\hp\\Desktop\\sample.txt")

