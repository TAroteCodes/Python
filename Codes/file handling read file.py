#file handling (read file)


fh = open(r'C:\Users\lenovo\Desktop\book.txt','r')  #r for read instruction.

data=fh.read()

print('File data is:')

print(data)

fh.close()   #file closing is mandatory to save changes permenantly.
