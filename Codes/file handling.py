#file handling (open file)

fh = open(r'C:\Users\lenovo\Desktop\book.txt','w')  #w for write instruction.

print('file open successfully')

fh.write('Tushar\n')
fh.write('Tukaram\n')
fh.write('Arote\n')

print('Data written to file successfully')

fh.close()   #file closing is mandatory to save changes permenantly.
