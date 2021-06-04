f=open("E:\text.txt","r")
for lines in f:
    print(*lines.split(','))