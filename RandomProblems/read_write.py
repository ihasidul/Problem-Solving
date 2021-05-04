#this is to read the file
f = open('testFile.txt', 'r')
print(f.read())
f.close()
#this is to rewrite the file
f = open('testFile.txt', 'w')
f.write("Hello i am changing the contents")
f.close()
#this to append to the existing file
f = open('testFile.txt', 'a')
f.write("i am adding things at the end")
f.close()



