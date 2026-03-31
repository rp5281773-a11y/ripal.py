#write()-write a single string
f=open("one.text","w")
f.write("hello student\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun.\n")
f.close()

#example 2 
f=open("one.text","w")
f.write("new content only.\n")
f.close()

#writelines()-write multiple lines
f=open("one.text","w")
line=[
    "python progaraming\n"
    "file handlinge\n"
    "error handline\n"
    "excpetion handling\n"
]

f.writelines(line)
f.close()

