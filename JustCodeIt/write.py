import os
with open("old.txt","r") as f, open("new.txt","w") as ff:
    for i in f:
        if "python" in i:
            i = i.replace("python","newpython")
        ff.write(i)
os.rename("old.txt","old2.txt")
os.rename("new.txt","old.txt")


