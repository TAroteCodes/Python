#file handling (read file line by line)


fh = open(r'C:\Users\lenovo\Desktop\book.txt','r')  #r for read instruction.

data=fh.readline()       #read only one line
#data=fh.readlines()      #read all lines showing o/p in list format.

print('File data is:')

print(data)

fh.close()   #file closing is mandatory to save changes permenantly.
