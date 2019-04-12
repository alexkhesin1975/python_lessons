#!/usr/bin/python2.7
-------------------------------------------------------------------
-------------------------------------------------------------------
print ('hello')
if 3<2:
    print ('ok')
elif 3>2:
    print('oki doki')
else:
    print('not ok')

-------------------------------------------------------------------
-------------------------------------------------------------------
name=('alex')
age=36

if name == 'alex' and age < 36:
    print('yey')
else:
    print('ups')
-------------------------------------------------------------------
-------------------------------------------------------------------
list1=['alex','moshe','vasya','don','dror']
for i in range(1,5):
    print(list1[i])
-------------------------------------------------------------------
-------------------------------------------------------------------
for i in range(0,101,5):
    print(i)
-------------------------------------------------------------------
-------------------------------------------------------------------
i=2
while i<10:
    print(i+100)
    i=i+1
e=0
for d in range(0,5):
    for s in range(0,5):
        print(e)
        e=e+1
-------------------------------------------------------------------
-------------------------------------------------------------------
#array and list functions
list=[2,3,4,5]
array=["a","b","c"]
len(array) #prints lenth
len(list)
max(list) #only for int arrays prints biggest number
min(list) #returns minimum number
sum(list) #makes summ of all numbers in list

-------------------------------------------------------------------
-------------------------------------------------------------------

#prime numbers
for i in range(2,90):
    j=2
    counter=0
    while j<i:
        if i%j==0:
            counter=1
            j=j+1
        else:
            j=j+1
    if counter == 0:
        print(str(i)+"prime number")  #str() coverts integer to string, int() converts string to int[if possible]
    else:
        counter=0

-------------------------------------------------------------------
-------------------------------------------------------------------
#breake loop on selected condition
#pass work regulary until condition are ok
counter=0
while counter <100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter = counter+1

#continue skips one step
for i in "Python":
    if i=="h":
        continue
    print(i)


#in case scrip runs in to bad condition printing an error
try:
    if name>3
    print('hi')
except:
    print('error')
-------------------------------------------------------------------
-------------------------------------------------------------------
#comment
"""
multi line comment
multi line comment
multi line comment
"""
-------------------------------------------------------------------
-------------------------------------------------------------------
#escape characters
# if we type ( string = 'baba'baba') it well be error
#if we type (string='baba\'baba') it ok  the \ before any sign makes it simple letter

# if we put (   \ ) before move next line then next line considered as regular code continu
#example
counter=0
while \
    counter <100:
    if \
        counter == 4:
        break
    else:
        pass
    print(counter)
    counter = counter+1

-------------------------------------------------------------------
-------------------------------------------------------------------
#### functions
def func():
    for in range(0,5):
        print("Hi")
        return
for i in range(0,5):
    func()

def func1(num1,num2):
    num3=num1+num3
    return(num3)
#same function different disighn
def func1.1(num1,num2):
    return(num1+num2)
-------------------------------------------------------------------
-------------------------------------------------------------------
## variables
total=10   #global variable works in all script
def multi(num1,num2):
    total=num1*num2  #local variable works only in function
    return total

multi(5,7) #will return 35
total #vill return 10
-------------------------------------------------------------------
-------------------------------------------------------------------
#abs and bool functions
abs(-5) # will return 5
abs(5) #will return 5
#abs is returns an absolute value
bool(0) #returns False
bool(None) #returns False
#in all other cases returns True
bool(1)
bool(67)
bool("haha") #teturns True
-------------------------------------------------------------------
-------------------------------------------------------------------
# Dir and Help
#Dir returns all available commans we can use 
dir(["jsfjgesk"]) # gives response what we can do with List

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

tiger="ukdkf"
dir(tiger)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

help(tiger.decode) #explains what doing exact function 

-------------------------------------------------------------------
-------------------------------------------------------------------
# eval  evalueting simple commands
eval(print("Hello"))
#will print hello
eval("23+23")
#will response 46

# exac same as eval but can run multiline code
exec(print("Hello  i go ")
     print("home now"))
-------------------------------------------------------------------
-------------------------------------------------------------------
age = input("what is your age") #input 14
age #equals 14 now but it string
int(age) #now it integer
age="123.345"
float(age) #converting to decimal 123.456

-------------------------------------------------------------------
-------------------------------------------------------------------

