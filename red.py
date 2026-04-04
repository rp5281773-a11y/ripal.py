#reading text files
f=open("one.text","r")
data=f.read()
print("file content:",data)
f.close()

#reading specific number of charaters
f=open("one.text","r")
data=f.read(10)
print("first part:",data)
f.close()

#readline()-read one_line
f=open("one.text","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()

#redlines()-read all linews into a list
f=open("one.text","r")
lines=f.readlines()
print("list pt line:",(lines))
print("number of lines:",len(lines))
f.close()

#reasding specific line from a file using reading
f=open("one.text","r")
lines=f.readlines()
print(lines [1].strip())
f.close()