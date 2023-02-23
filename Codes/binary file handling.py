#file handling write list into file (binary read write)

fh = open(r'C:\Users\lenovo\Desktop\b.txt','wb')  #wb for binary write instruction.

print('file open successfully')
marks = [1,2,3,4,5,6,7,8,9,0]
ba = bytearray(marks)     #convert marks(list) into binary
fh.write(ba)

print('Data written to file successfully')

fh.close()   #file closing is mandatory to save changes permenantly.

#read part

fh = open(r'C:\Users\lenovo\Desktop\b.txt','rb')  #rb for binary read instruction.

data=fh.read()

print('File data is:')
for it in data:              #get o/p in hexadecimal
         print(it,end=' ')   

fh.close()   #file closing is mandatory to save changes permenantly.
