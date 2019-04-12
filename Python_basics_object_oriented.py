#!/usr/bin/python2.7

-------------------------------------------------------------------
-------------------------------------------------------------------

#clases

class ClassName:  #simple class that do nothing
    pass

class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

studen1=Students("Bob",12,"4th") #we created object of student and now we can call different parts

student1.name
#return Bob
student1.age
#return 12
studen1.grade
#return 4th

student1=Student("alex",13) #will return error missing parameter

-------------------------------------------------------------------
-------------------------------------------------------------------
#Functions in classes

class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayStudent(self):
        return("Student name is " + self.name + "and age :" + str(self.age))

stu=Students("chad",15) #loading data tu the function in class sorts and imports to stu
stu.displayStudent() #calling function from class with data imported to stu
#response
# Student name is  chad and age : 15

-------------------------------------------------------------------
-------------------------------------------------------------------
# attributes in classes

class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=Students("Fred",17)
student2=Students("Mike",12)

hasattr(student1, "age")  #chckeng if such parameter (attribute) exists in class
#return true
hasattr(student1, "Grade")
#returns False

setattr(student1,'grade',"8th") #adding another attribute that not configured in main clas on first time


getattr(student1,"grade")
getattr(student1,"age") #same as student1.age

delattr(student1, "Grade") #removes attribute

-------------------------------------------------------------------
-------------------------------------------------------------------

#class inheretance
#child clases

class Parent:
    counter =10
    def __init__(self):
        print("Class Initialized.")
    def parentFunc(self):
        print("ParentFunc being Called")
    def setCounter(self, num):
        Parent.counter=num
    def showCounter(self):
        print(str(Parent.counter))

class Child(Parent):  #that mean the Child class inherites all thins from parent
    def __init__(self):
        print("Child class being initialized")
    def childFunc(self):
        print("Child func being called")

c = Child()  #we are setting all Child class to c variable
c.childFunc() #call function from child and delivers c to there
c.parentFunc() #call function from parents but do it over previously set child class
c.counter #requesting counter valu from Parent class but do it over child class
c.setCounter(20) #setting counter variable in function as 20
c.showCounter() #requesting counter value

-------------------------------------------------------------------
-------------------------------------------------------------------

### overriding methods

class Parent:
    def func(self):
        print("This is a parent function")
class Child(Parent):
    def func(self):
        print("This is a child function")

c = Child()
c.func()
#this will return "This is a child function"
#this method colled overriding functions 
#in case both of them are the same
