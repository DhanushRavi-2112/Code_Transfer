from numpy.f2py.capi_maps import lcb_map


def add():
    return a+b
def sub():
    return a-b
def mul():
    return a*b
def div():
    return a/b

'''a=int(input('a='))
b=int(input('b='))
c=[1,2,3,4]
print('1.add\n2.sub\n3.multiply\n4.divide')
d=int(input('Select The Option:'))
if c[0]==d:
    print(add())
elif c[1]==d:
    print(sub())
elif c[2]==d:
    print(mul())
elif c[3]==d:
    print(div())
else:
    print('Invalid Option')'''


'''def mark(n):
    if n>=35:
        return 'pass'
    else:
        return 'fail'
n=int(input('mark='))
print(mark(n))'''

'''user='john'
password=1234
def user_pas(user1,password1):
    if user==user1 and password==password1:
        print('Verified')
    else:
        print('Unverified User')
user1=input('username:')
password1=int(input('password:'))
user_pas(user1,password1)'''

#---------NESTED FUNCTION--------
'''def add(i,j):
    return i**j
print(add(2,3))
print(add(3,3))'''

#-------LAMBDA FUNCTION-------
'''n=int(input('n='))
m=lambda a:a*a
print(m(n))'''

#-----MAP FUNCTION------
'''n=[1,2,3,4,5]
m=map(lambda x:x**2,n)
print(list(m))'''

#-----WITHOUT MAP FUNCTION-----
'''def val(x):
    return x**2
a=[1,2,3,4,5]
y=[]
for i in a:
    n=val(i)
    y.append(n)
print(y)'''

#---FILTER FUNCTION-------
'''x=[1,2,3,4,5]
y=filter(lambda a:a%2==0,x)
print(list(y))'''


def check(n):
    if n=='A+':
        return 'donate:A+\nrecieve:A-,A+,O-,O+'
    elif n=='B+':
        return 'donate:B+,AB+\nrecieve:B+,B-,O-,O+'
    elif n=='AB+':
        return 'donate:AB+\nrecieve:Everyone'
    elif n=='O+':
        return 'donate:All +ve groups\nrecieve:O-,O+'
    elif n=='A-':
        return 'donate:A+,A-,AB-,AB+\nrecieve:A-,O-'
    elif n=='B-':
        return 'donate:B+,B-,AB+,AB-\nrecieve:B-,O-'
    elif n=='AB-':
        return 'donate:AB+,AB-\nrecieve:All -ve groups'
    elif n=='O-':
        return 'donate:Everyone\nrecieve:O-'
    else:
        return 'Invalid blood group!'
#n=input('n=')
#print(check(n))

#---KEY VALUE CHANGE------
'''a={1:'a',2:'b',3:'c'}
b={j:i for i,j in a.items()}
print(b)'''

'''n=['apple','orange','mango']
m=[i[2].upper() for i in n]
print(m)'''

#----POSITIONAL ARGUMENT---
def n(fname,lname):
    return 'Hello',fname,lname
'''m=n('Tony','Stark')
print(m)'''

def add(a,b,c):
    return f'a={a},b={b},c={c}'
'''n=add(2,3,5)
print(n)'''

#----KEYWORD ARGUMENT-----
#print(n(lname='Stark',fname='Tony'))
#print(add(c=1,a=3,b=6))

#--DEFAULT ARGUMENT---
def hello(name='Thor'):
    return f'Hello {name}!'
#print(hello())
#print(hello('Stark'))

#def sum(a=3,b=4,c=5):
#    return f'{a},{b},{c} is Sum of {a+b+c}'
#print(sum())
#print(sum(10,7,2))

#--ARBITARY----
'''def ad(f):
    return sum(f)
n=range(1,6)
print(ad(n))'''

'''def add(*args):
    b=sum(args)
    print(b)
add(1,2,3,4,5)

def arg(**argv):
    for i,j in argv:
        print(f'{i}:{j}')
arg(name='Tony',age=27,city='New York')'''

#--------RECURSIVE FUNCTION---
'''def fact(n):
#  if n==0:
        return 1
#  else:
        return n*fact(n-1)
        '''
#a=int(input('a='))
#print(fact(a))

#print(factorial(5))

#----FIBNANACII SERIES--
'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
a=int(input('a='))
for i in range(a):
    print(fib(i))'''

'''def power(base,pwr):
    if pwr==0:
        return 1
    else:
        return base*power(base,pwr-1)
b=int(input('base='))
p=int(input('power='))
print(power(b,p))'''

'''def add(n):
    if n==0:
        return 0
    else:
        return n+add(n-1)
a=int(input('a='))
print(add(a))'''

'''n=int(input('n='))
res=0
for i in range(1,n+1):
    res=res+i
print(res)'''

'''x,y,z=1,1,2
a=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
print(a)'''

#-------VARIABLE SCOPE-------
#--LOCAL SCOPE: Variable declared inside a function are local to that function and can't
#               access outside it.
#PGM:01
'''def hello():
    x='John'        #This variable can't access from out of the function.
    print(f'Hello,{x}')
hello()'''

#----GLOBAL SCOPE:Vaiable defined out of the function its called global scope variable.They
#                 can be access thruoghout the module.But not modified inside functions
#                 without using global keyword.
#PGM:01
'''n='John'    #This variable to access everywhere.
def hello():
    print(f'Hii {n}')
hello()
print(n)'''

'''def hello():
    global n     #global keyword using local scope access from out of function.
    n='Jackie'
    print(f'Hello {n}')
hello()
print(n)'''

#Example:
'''a=0
def inc():
    global a
    a+=1
    print(a)
def dec():
    global a
    a-=1
    print(a)
inc()
dec()
print(a)'''

#---CLOSURE:**A Nested function(inner function) is defined inside enclosing function.
#           **The inner function user variables from the enclosing function.
#           **The outer function returns the inner function.

#Example:
'''def out(n):
    def inn(m):
        return n**m
    return inn
y=out(2)
print(y(3))'''

#ENCLOSING SCOPE:**In Nested function, the enclosing scope refers to variables in the outer
#                function.
'''def outer():
    p=20
    def inner():
        p=15
        print(f'inner {p}')
    inner()
    print(f'outer {p}')
outer()'''
#    **Use nonlocal keyword modify these variable.
'''def outer():
    p=20
    def inner():
        nonlocal p
        p=15
        print(f'inner {p}')
    inner()
    print(f'outer {p}')
outer()'''

#----------------------------------------------------------------
#    DECORATOR: A decorator is a function that wraps another function.
'''def a():
    print('Hello')
def b(c):
    print('Welcome')
    c()
b(a)'''

'''def upp(a):
    def inner():
        return a.upper()
    return inner
def d():
    return 'hello'
c=d()
print(c)
b=upp(d())
print(b())'''

#import random
'''n=['apple','orange','mango']
l=random.choice(n)
print('apple\norange\nmango')
x=input('select the fruit:')
if x==l:
    print('correct')
else:
    print('mismatch')
a=['raj','ram','john','raja']
n=random.choice(a)
print(n)'''

#----FILE HANDLING-----

'''fle=open('sample','w')
fle.write('Hello Guys!')
fle.close()'''

#---------
import os
#print(os.getcwd())    #current working  directory path printing command

#os.chdir('c:\\Python')    #change the diectory path
#print(os.getcwd())

#----------
'''import re     #re-regular exression
a='Hello'
n=re.findall('He.+',a)
print(n)'''
#-----------------
'''def cash_withdraw():
    user_pin=int(input('Enter Your Pin:'))
    if user_pin==pin:
        amt=int(input('Enter your Amount:'))
        print('Please Collect Your Money')
    else:
        print('Incorrect pin')
def deposit():
    user_pin = int(input('Enter Your Pin:'))
    if user_pin == pin:
        amt = int(input('Enter your Amount:'))
        print(f'{amt} deposited')
    else:
        print('Incorrect pin')
def bal_chk():
    user_pin = int(input('Enter Your Pin:'))
    if user_pin == pin:
        print(amount)
name=input('Enter Your Name:')
print(f'Welcome {name}')
print('1.cash withdraw\n2.deposit\n3.balance check')
opt=int(input('select the option:'))
amount=12000
a=[1,2,3]
pin=2112
if a[0]==opt:
    cash_withdraw()
elif a[1]==opt:
    deposit()
elif a[2]==opt:
    bal_chk()
else:
    print('Invalid option!')'''
#------------------------------------
'''
n=input('ente:')

cap=0
small=0
num=0
for i in n:
    if i>='a' and i<='z':
        small+=1
    elif i>='A' and i<='Z':
        cap+=1
    elif i>='0' and i<='9':
        num+=1
print(cap)
print(small)
print(num)'''
#---------------------------OS MODULE BASIC------
'''import os
print(os.getcwd())  #print current directory
os.chdir('C:\\Python')  #change the directory path
print(os.getcwd())'''
#print(os.listdir())      #list out the directory
#print(os.makedirs('pyfile'))   #create new directory
#print(os.removedirs('pyfile'))  #remove the directory

#---------MATH MODULE------
#import math
#print(dir(math))
#print(math.fabs(-67))  #fabs use negative value change posituve value
#print(math.ceil(3.9)) #o/p:4  #. values maximum a full number
#print(math.floor(3.8)) #o/p:3  #. values minimum a full number
#print(math.lcm(4,7,6))
#print(math.remainder(45,7)) #print the reminder value

#------------*EXCEPTION HANDLING*--------
'''m=45
n='hello'
try:
    print(m+n)
except:
    print('cant add str int' )'''
'''def fun():
   print(5/0)
try:
    fun()
except ZeroDivisionError:
    print('Please Enter Valid Number')
except IndentationError:
    print('Change The Function Alignment')'''
'''def a(b,c):
    try:
        n=(b+c)/(b-c)
    except:
        print('Zerodivision Error')
    else:
        print(n)
a(4,2)
a(3,3)'''

#-------------------------------------------------------------------------







