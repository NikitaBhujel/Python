#Encapsulation:Wrapping data and fucntions into single unit
#Encapsulation=>Data Hiding
class BankAccount:
    def __init__(self,name,balance):
        self.name=name  #public attributes
        self.__balance=balance #private attribute


#If we have to give access to private attributes, we do through special functions, getters and setters
#If we use double underscore, it is private attribure
    def get_balance(self):  #getter function
        return self.__balance
    
    def set_balance(self,newBalance):  #setter function
        self.__balance=newBalance


acc1=BankAccount("Nikita Bhujel",5_00_000)
acc1.set_balance(6_00_000)
print(acc1.name,acc1._BankAccount__balance) 
#print(acc1.name,acc1.get_balance()) 

#Don't access protected attribute from outside using self._balance
#Private: Data mangling, we cannot access outside the class 
#There is no true protected or true private attribures


