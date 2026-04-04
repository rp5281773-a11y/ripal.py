#copy content from one file to another
src=open("one.text","r")
data=src.read()
src.close()


dst=open("2.text","w")
dst.write(data)
dst.close()
print("file copies succrssfully.")