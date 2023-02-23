class my_class:
    
    def add(self,a,b):
        print(a+b)
obj = my_class()                                 #object created of my_class class
obj.add(5,10)                                    #accesing add method outside the class
obj1 = my_class()                                #we can create more than 1 object of the same class
obj1.add(16,5)                                   #accessing same method with different classes
