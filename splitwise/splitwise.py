from enum import Enum
from typing import List


class User():
    def __init__(self,name,phone,email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getEmail(self):
        return self.__email



    
class Type(Enum):
    EQUAL = "equal"
    EXACT = "exact"
    PERCENT = "percent"

class Expense():
    def __init__(self,user:User,users:List[User],amount:int,type:Type):
        self.__user = user
        self.__otherUsersList = users
        self.__amount = amount
        self.__userToUserAmount = {}
        self.type = type

    def getUserToUserAmount(self):
        return self.__userToUserAmount

    def getAmount(self):
        return self.__amount

    def getUser(self):
        return self.__user.getName()

    def getOtherUser(self):
        return self.__otherUsersList

    def setExactAndGetUserToBalance(self):
        self.type = Type.EXACT
        for otherUser in self.getOtherUser():
            self.__userToUserAmount[otherUser.getName()] = self.getAmount()
    
    def setEqualAndGetUserToBalance(self):
        self.type = Type.EQUAL
        splitAmount = self.getAmount()/len(self.getOtherUser())
        for user in self.getOtherUser():
            self.userToUserAmount[user.getName()] = splitAmount
        
          
class Group():
    def __init__(self,name:str,users :List[User]):
        self.name = name
        self.__users = users
        self.userToBalance = {}
        self.expenseObjs  = []

    def getTotalExpenseUserSpecific(self,user:User):
        totalExpense = 0
        for obj in self.expenseObjs:
            if obj.getUser() == user.getName():
                totalExpense += obj.getAmount()
            
        print("Total Expense for {} is --->{}".format(user.getName(),totalExpense))
            
    def addExpenseToGroup(self,user:User,users:List[User],amount,type:Type):
        expense = Expense(user,users,amount,type)
        if type == "equal":
            expense.setEqualAndGetUserToBalance()
        elif type == "exact":
            expense.setExactAndGetUserToBalance()
        import pdb;pdb.set_trace()
        for userObj in expense.getUserToUserAmount():
            ##if first entry at userToBalance
            if not userObj in self.userToBalance:
                self.userToBalance[userObj] = {user.getName():expense.getUserToUserAmount()[userObj]}
            
            else:
                if  not user.getName() in self.userToBalance[userObj]:
                    self.userToBalance[userObj][user.getName()] = expense.getUserToUserAmount()[userObj]
                else:
                    self.userToBalance[userObj][user.getName()] += expense.getUserToUserAmount()[userObj]
    
        for userObj in expense.getUserToUserAmount():
            if not user.getName() in self.userToBalance:
                self.userToBalance[user.getName()] ={userObj: -expense.getUserToUserAmount()[userObj]}

            else:
                if userObj not in self.userToBalance[user.getName()]:
                    self.userToBalance[user.getName()][userObj] = -expense.getUserToUserAmount()[userObj]

                self.userToBalance[user.getName()][userObj] -= expense.getUserToUserAmount()[userObj]
            
        self.expenseObjs.append(expense)


        

        print("Group expense is --->",self.userToBalance)
    

    def getTotalGroupExpense(self):
        totalExpense = 0
        for eachExpenseObj in self.expenseObj:
            totalExpense  += eachExpenseObj.getAmount()
        return totalExpense
    
    def showAllUsers(self):
        return self.__users

u1 = User("spandan","8249071806","mishraspandan2@gmail.com")
u2 = User("suraj","987679211","suraj@gmail.com")
u3 = User("akash","98213131","podau@gmail.com")
g1 = Group("ladakhTrip",[u1,u2,u3])

g1.addExpenseToGroup(u1,[u2],1000,Type["EXACT"].value)
g1.addExpenseToGroup(u1,[u2],500,Type["EXACT"].value)
g1.addExpenseToGroup(u2,[u1],500,Type["EXACT"].value)
g1.addExpenseToGroup(u3,[u1],500,Type["EXACT"].value)
g1.getTotalExpenseUserSpecific(u1)
g1.getTotalExpenseUserSpecific(u2)