#Programming Problems

#PE1.py

class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def getName(self):
        return self.name
    
    def setScore(self, i, score):
        self.scores[i - 1] = score
        
    def getScore(self, i):
        return self.scores[i - 1]
    
    def getAverage(self):
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        return max(self.scores)
    
    def __eq__(self, student):
        return self.name == student.name
    
    def __ge__(self, student):
        return self.name == student.name or self.name>student.name
    
    def __lt__(self, student):
        return self.name<student.name
    
    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
        " ".join(map(str, self.scores))
        
def main():
    student = Student("Samuel", 5)
    print(Student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    
    print("\nSecond Student")
    student2 = Student("Elijah", 5)
    print(student2)
    
    print("\nThird Student")
    student3 = Student("Romeo", 5)
    print(student3)
    
    print("\nChecking equal student 1 and student 2")
    print(student.__eq__(student2))
    
    print("\nChecking equal student 1 and student 3")
    print(student.__eq__(student3))
    
    print("\nChecking greater than equal student 1 and student 3")
    print(student.__ge__(student3))
    
    print("\nChecking less than student 1 than student 3")
    print(student.__lt__(student3))
    
if __name__== "__main__":
    main()

--------------------------------------------------------------------

#PE2.py

import random

class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def getName(self):
        self.name
    
    def setScore(self, i, score):
        self.scores[i - 1] = score
        
    def getScore(self, i):
        return self.scores[i - 1]
    
    def getAverage(self):
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        return max(self.scores)
    
    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))
               
    def __lt__(self, other):
        return self.name<other.name
    
    def __ge__(self, other):
        return self.name >= other.name
    
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name
        
def main():
    lyst = []
    for count in reversed(range(5)):
        s = Student("Name " + str(count + 1), 10)
        lyst.append(s)
        
    random.shuffle(lyst)
    print ("Unsorted list of students: ")
    for s in lyst:
        print(s)
        
    lyst.sort()
    print ("\nSorted list of students: ")
    for s in lyst:
        print (s)
        
if __name__ == "__main__":
    main()

--------------------------------------------------------------------

#PE3.py

import pickle
import random
from savingsaccount import SavingsAccount

class Bank:

    def __init__(self, fileName = None):

        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        return "\n".join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        total = 0
        for account in self._accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        return []

    def save(self, fileName = None):
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
       
def createBank(numAccounts = 1):
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number = 10, fileName = None):
    testAccount()

if __name__ == "__main__":
    main()
