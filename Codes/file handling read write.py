#file handling (multiple strings input

#writing part

fh = open(r'C:\Users\lenovo\Desktop\bk.txt','w')  #w for write instruction.

print('file open successfully')

fh.writelines(['Tushar\n','Tukaram\n','Arote\n','Pune'])

fh.close()   #file closing is mandatory to save changes permenantly.

#reading part


fh = open(r'C:\Users\lenovo\Desktop\bk.txt','r')  #r for read instruction.

data=fh.read(6)  #no. for read only that much charactors from file

print('File data is:\n')

print(data)

fh.close()   #file closing is mandatory to save changes permenantly.
