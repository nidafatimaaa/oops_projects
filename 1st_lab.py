class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)

print(s1.name)
print(s1.age)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student("Ali", 20)
s1.display()

class Student :
    def __init__(self):
        print("Hello Student")
s1= Student()

class Student :
    def __init__(self,name):
        self.name = name
s1 = Student("ali")
print(s1.name)

class Student :
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 =Student("Ahmad",20)
print(s1.name)
print(s1.age)

class Car: 
    def __init__(self,brand,year,model):
        self.brand = brand
        self.year = year
        self.model = model
c1 =Car("Toyota",2024,"Corolla")
print(c1.brand)
print(c1.year)
print(c1.model)

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
e1 =Employee("Ahmad",50000)
e2 =Employee("Ali",60000)
print(e1.name)
print(e1.salary)
print(e2.name)
print(e2.salary)

class Book:
    def __init__(self,title,author,price):
        self.title= title
        self.author= author
        self.price= price
b1 =Book("Python","John",1500)
b2 =Book("C++","James",2000)
print(b1.title)
print(b1.price)
print(b2.title)
print(b2.price)
print(b1.author)
print(b2.author)

class Bankaccount:
    def __init__(self,name,balance):
        self.name= name
        self.balance= balance
b1= Bankaccount("Ali",40000)
print(b1.name)
print(b1.balance)

class Student:
    def __init__(self,name):
        self.name= name
    def introduce(self):
        print("My name is",self.name)
s1= Student("Ali")
s1.introduce()

class Student:
    def __init__(self,name):
        self.name= name
    def introduce(self):
        print("My name is",self.name)
s1= Student("Ahmad")
s2= Student("ali")
s1.introduce()
s2.introduce()

class Claculator:
    def add (self,a,b):
        print(a+b)
c1= Claculator()
c1.add(10,20)

class Claculator:
    def multiply(self,a,b):
        print(a*b)
c1= Claculator()
c1.multiply(4,5)

class Student:
    def __init__(self,name):
        self.name= name
    def greet(self):
        print("Hello",self.name)
s1= Student("ali")
s2= Student("ahmad")
s1.greet()
s2.greet()

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def show_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
p1= Person("Ali",20)
p1.show_info()

class Student:
    def __init__(self,name):
        self.name= name
    def greet(self,message):
        print(self.name,message)
s1= Student("Ali")
s1.greet("Good morning")

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    def show_salary(self):
        print(self.name,"Earns",self.salary)
e1= Employee("Ali",90000)
e1.show_salary()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_age(self, new_age):
        self.age = new_age
s1 = Student("Ali", 20)
s1.change_age(21)
print(s1.age)

class Student:
    school="UET"
    def __init__(self,name):
        self.name= name
s1= Student("Ali")
s2= Student("Ahmad")
print(s1.name)
print(s2.name)
print(s1.school)
print(s2.school)

#class variables(cls)
#instance variable(self)
class Student:
    school= "UET"
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()
class Student:
    school = "UET"
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()
Student.change_school("PU")
Student.show_school()

class Student:
    school= "PU"
    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()
Student.change_school("UET")
Student.show_school()

class School:
    name = "UET"
    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name
School.change_name("UNIQUE School")
print(School.name)
# class varirable change
class Student:
    school = "UET"
    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
Student.change_school("FC")
print(Student.school)

# class method +display
class Company:
    name = "ABC"
    @classmethod
    def show_company(cls):
        print("Company:",cls.name)
Company.show_company()

# change the display
class University:
    name = "FCU"
    @classmethod
    def change_name(cls,new_name):
        cls.name = new_name
    @classmethod
    def show_name(cls):
        print(cls.name)
University.show_name()
University.change_name("King Edward")
University.show_name()
class Student:
    school = "UET"
    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
# company change example
class Company:
    company = "Tekxel"
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
print(Company.company)        
Company.change_company("System Limited")
print(Company.company)
#bank name change example
class Bank:
    bank_name = "HBL"
    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name = new_bank
print(Bank.bank_name)
Bank.change_bank("Mezzan Bank")
print(Bank.bank_name)
# Normal method:
#def show(self):
#     ↓
# self = object
# 
# Class method:
# @classmethod
# def show(cls):
#     ↓
# cls = class
# 
# Static method:
# @staticmethod
# def add(a, b):
#     ↓
# self nahi
# cls nahi
#static method
class Calculator:
    @staticmethod
    def add (a,b):
        print(a+b)
Calculator.add(10,20)

class Math:
    @staticmethod
    def square(n):
        print(n*n)
Math.square(5)

class Calculator:
    @staticmethod
    def multiply(a,b):
        print(a*b)
Calculator.multiply(6,5)    

class Student:
    @staticmethod
    def welcome():
        print("Welcome to python")
Student.welcome()        

class Calculator:
    @staticmethod
    def divide(a,b):
        print(a//b)
Calculator.divide(20,5)

class Math:
    @staticmethod
    def cube(n):
        print(n*n*n)
Math.cube(3)        
#Encapsulation
#Encapsulation = data ko class ke andar rakhna aur us data ko controlled way mein access/change karna.
#Python mein hum mainly 3 levels dekhte hain:
#1. Public
#2. Protected _
#3. Private __
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("ALI")
print(s1.name)

class Student:
    def __init__(self,name):
        self._name=name
s1 = Student("Ali")
print(s1._name)

#double underscore
#print(s1.__name)it has attribute error bec double underscore
class Student:
    def __init__(self,name):
        self.__name=name
    def show_name(self):
        print(self.__name)
s1= Student("ALI")
s1.show_name()
#__name
   
#Private variable
   
#show_name()
   
#Class ke andar access
   
#Ali
#getter   

class Student:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
s1 = Student("ALI")
print(s1.get_name())
# Getter → value READ karta hai
# Setter → value CHANGE karta hai
class Student:
    def __init__(self,name):
        self.__name=name
    def set_name(self,new_name):
        self.__name=new_name
    def get_name(self):
        return self.__name
s1= Student("ahmad")
s1.set_name("ali")
print(s1.get_name())

class Student:
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age= new_age
s1 = Student(20)
print(s1.get_age())
s1.set_age(21)
print(s1.get_age())
class Student:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name= new_name
s1 = Student("khurram abbas")
print(s1.get_name())
s1.set_name("Ahmad")
print(s1.get_name())
class BankAccount:
    def __init__(self,balance):
        self.__balance= balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance= new_balance
b1 = BankAccount(40000)
print(b1.get_balance())
b1.set_balance(50000)
print(b1.get_balance())
class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary
e1 = Employee(60000)
print(e1.get_salary())
e1.set_salary(75000)
print(e1.get_salary())
class Car :
    def __init__(self,price):
        self.__price =  price
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        self.__price = new_price
c1 = Car(2000000)
print(c1.get_price())
c1.set_price(2500000)
print(c1.get_price())
#with condition
class Student:
    def __init__(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Invalid age")
s1 = Student(20)
print(s1.get_age())
s1.set_age(21)
print(s1.get_age())
s1.set_age(-5)
print(s1.get_age())

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balnace")
b1 = BankAccount(40000)
print(b1.get_balance())
b1.set_balance(50000)
print(b1.get_balance())
b1.set_balance(-1000)
print(b1.get_balance())
#complex code
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name = new_name
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        self.__salary = new_salary
e1 = Employee("Ahmad",60000)
print(e1.get_name())
print(e1.get_salary())
e1.set_name("Ali")
e1.set_salary(70000)
print(e1.get_name())
print(e1.get_salary())
#Inheritance
#Inheritance = ek class doosri class ke attributes aur methods ko use kar sakti hai.      
class Animal:
    def eat(self):
        print("Animal is eating")
    def bark(self):
        print("Animal is barking")
        
class Dog(Animal):
    pass
d1 = Dog()
d1.eat()
d1.bark()

class Vehicle:
    def start(self):
        print("Vehicle is starting")
class car (Vehicle):
    pass
c1 = car()
c1.start()

class Animal:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
class Dog(Animal):
    pass
d1 =Dog("Tommy")
d1.show_name()
    
