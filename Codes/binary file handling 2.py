#file handling write list into file (binary read write)

import pickle          #library for write str+int data

fh = open(r'C:\Users\lenovo\Desktop\bf.dat','wb')  #wb for binary write instruction.(.dat file ext to store thse data)

print('file open successfully')
L = [(1,'Tushar',24),(2,'mama',25),(3,'ammi',45),[4,'appa',50]]
pickle.dump(L,fh)   #writing data in file                                     

print('Data written to file successfully')

fh.close()   #file closing is mandatory to save changes permenantly.

#read part

fh = open(r'C:\Users\lenovo\Desktop\bf.dat','rb')  #rb for binary read instruction.

data = pickle.load(fh)     #to read the data from file

print('File data is:')
for it in data:              #get o/p in readable format
         print(it,end=' ')   

fh.close()   #file closing is mandatory to save changes permenantly.



#we can read and write many file formats python supports many of them 
