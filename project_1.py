
'''n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    '''

'''
num=5
res=1
for i in range(2,num+1):
    res*=i
print(res)
n=int(input('enter the value:'))
for i in range(1,n+1):
    print(f'{i}*2=',i*2 )
    '''
'''
n=int(input('enter the value:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()
 '''
'''
nn=int(input('enter the value:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()
 '''
'''
n=int(input('enter the value:'))
for i in range(n):
    for k in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('*',end=' ')
    print()
'''
'''
n=int(input('enter the value:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for k in range(i+1):
        print(' ',end='')
    for j in range(n-i-1):
        print('*',end=' ')
    print()
'''

'''
n=int(input('enter the value:'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()
'''
'''
n=int(input('enter the value:'))
for i in range(n-1):
    for k in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('*',end=' ')
    print()
for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(i+1):
            print('*', end=' ')
        print()'''
'''n=int(input('enter the value:'))
for i in range(n-1):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()'''
s='hello'
'''i=1
while i<=len(s):
    print(s[-i])
    i+=1'''
'''a=int(input('enter your value:'))
res=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res)

print(56%10)'''
'''a=int(input('enter the value:'))
sum=0
while a>0:
    sum=sum+a%10
    a//=10
print(sum)'''
'''a=int(input('enter your value:'))
sum=0
for i in range(a):
    sum=sum+a%10
    a=a//10
print(sum)'''
'''a=int(input('enter your value:'))
num=a
res=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
if num==res:
    print('palindrome')
else:
    print("not palindrome")

a=int(input("enter the value:"))
res=0
while a>0:
    rem=a%10
    res=res*10+rem
    a=a//10
print(res)s*10+rem'''
#-------------------------------------------------
'''A=int(input('num='))
if A<0 or A<15:
    print('Average Mark')
elif A<0 or A>15:
    print('HELLO')
elif A>0 or A>15:
    print('WELCOME')
elif A>0 or A<15:
    print('BYE')
else:
    print()'''
#-------------------------------
'''Q=int(input('Enter your Mark:'))
if Q>=18 :
    print('The',Q,'Age is Eligible For Voting')'''
#------------------------------------------
#----------FOR LOOP------------------
#n=int(input('START:'))#----INTEGER VALUE RANGE()--------
'''for i in range(n):
    print(i)
print(range(5))'''

'''for i in range(2,8):
    print(i)'''

#----REVERSE PRINTING VALUE---
'''Q=int(input('END:'))
R=int(input('INCREMENT:'))
for i in range(n,Q,R): #----(START,END,INDEXING VALUE)
     print(i)'''

'''a=int(input())
for i in range(1,a+1):
    if a%2==0:
        print(i'is even')
    else:
        print(i,'is odd')'''
'''n=int(input('Value='))
for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(1,n+1-i):
        print('*',end='')
    print()'''
#----------------------------------------------------
#PATTERN
#n=int(input('Value='))
#for i in range(1,n+1):
#    print('*',i,end=' ')  #O/P:*1 *2 *3
#----------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j,'/',end='')''' #O/P:1 1/1 2/1 3 etc..,
#---------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j,end=' ')
    print() '''                  #O/P:1 1,1 2,1 3
                              #    2 1,2 2,2 ,2 3
#----------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print() '''                     #O/P:* * *
#                                        * * *
#                                        * * *
#-------------------------------------
'''for i in range(1,n+1):
    for j in range(i):
        print(j,end=' ')
    print() '''                     #O/P:1
#                                        1 2
#                                        1 2 3
#------------------------------------
'''for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print() '''                       #O/P:1
#                                          2 1
#                                          3 2 1
#----------------------------------
'''for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print() '''                           #O/P:3 2 1
#                                           3 2
#                                           1
#-------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print() '''                             #O/P:1 1 1
#                                                2 2 2
#                                                3 3 3
#--------------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print() '''                                  #O/P:1 2 3
#                                                  1 2 3
#                                                  1 2 3
#----------------------------------------------
'''for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(i,end=' ')
    print() '''                            #O/P:3 3 3
#                                               2 2 2
#                                               1 1 1
#-------------------------------------
'''for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j,end=' ')
    print()'''                               #O/P:3 2 1
#                                                 3 2 1
#                                                 3 2 1
#----------------------------------------
'''for i in range(1,n):
    for j in range(1,n):
        print(n,end=' ')
    print()  '''                                #O/P:2 2 2 2 2 2
#                                                 2 2 2 2 2 2
#                                                 2 2 2 2 2 2 etc...,
#------------------------------------
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(n+1-j,end=' ')
    print()'''
#------------------------------------------
#1ST PATTERN
'''for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=' ')
    print()'''                        #O/P:3
#                                          2 3
#                                          1 2 3
#------------------------------------------------
#2ND PATTERN
'''for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print() '''                             #O/P:3 3 3
#                                                2 2
#                                                1
#------------------------------------------------
#3RD PATTERN
'''for i in range(n,0,-1):
    for j in range(1,i+1):
        print(n,end=' ')
    print() '''                           #O/P:3 3 3
#                                              3 3
#                                              3
#----------------------------------------------------
#4TH PATTERN
'''for i in range(n,0,-1):
    for j in range(1,i+1):
        print(n-j+1,end=' ')
    print()'''                        #O/P:3 2 1
#                                          3 2
#                                          3
#---------------------------------------------
#5TH PATTERN
'''for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end=' ')
    print()  '''                       #O/P:1 1 1
#                                           2 2
#                                           3
#--------------------------------------------------
#6TH PATTERN
'''for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()'''                        #O/P:3 2 1
#                                          3 2
#                                          1
#------------------------------------------------
#7TH PATTERN
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print() '''                      #O/p:1
#                                         2 2
#                                         3 3 3
#-----------------------------------------------
# 3 LOOP USE
'''for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()'''
                                      #O/P:   1
#                                           1 2
#                                         1 2 3
#---------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print() '''                             #O/P:    *
#                                                  * *
#                                                * * *
#------------------------------------------
'''for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print()'''                            #O/P:* * *
#                                              * *
#                                              *
#----------------------------------
'''for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()'''                                #O/P:1 2 3
#                                                    1 2
#                                                      1
#------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(n-k+1,end=' ')
    print()'''                             #O/P:   3
#                                                3 2
#                                              3 2 1
#-----------------------------------------
'''for i in range():
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(i,n+1):
        print(k,end=' ')
    print()  '''                             #O/P:    3
#                                                2 3
#                                              1 2 3
#---------------------------------------

#--------------------------------------
#1
#for i in range(1,n+1):
#    for j in range(1,n+1):
#        print('*',end=' ')
#    print()
#-----------------------------------
#2
#for i in range(1,n+1):
#    for j in range(1,n+1):
#        print(n,end=' ')
#    print()
#----------------------------------------
#3
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()'''
#----------------------------------
#4
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()'''
#-----------------------------------
#5
'''for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()'''
#-----------------------------
#6
'''for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()'''
#----------------------------
#7
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(1,i):
        print(k,end=' ')
    print()'''
#-----------------------------
n=int(input('n='))
'''for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for l in range(i-1,0,-1):
        print(l,end=' ')
    print()'''
#------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for l in range(i,0,-1):
        print(l,end=' ')
    print()'''
#-------------------------------------
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for k in range(n*2,i*2,-1):
        print(' ',end=' ')
    for l in range(i,0,-1):
        print('*',end=' ')
    print()'''
#------------------------------------
'''for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('*',end=' ')
    for k in range(1,i*2-1):
        print(' ',end=' ')
    for l in range(1,n+2-i):
        print('*',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for k in range(n*2,i*2,-1):
        print(' ',end=' ')
    for l in range(i,0,-1):
        print('*',end=' ')
    print()'''
#-----------------------------------------
#BREAK
'''for i in range(n):
    if i==6:
        break
    print(i)'''
#-----------------
#CONINUE
'''for i in range(n):
    if i==2:
        continue
    print(i)'''
#------------------
'''while n>5:
    print(n)
    n-=1'''
#------------------
'''while n<6:
    print(n)
    n+=1'''
#---------------
'''for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(n+1,i,-1):
        print('*',end=' ')
    print()'''
#----------------------
'''for i in range(1,n):
    for j in range(1,n+2-i):
        print(n-1,end=' ')
    for k in range(1,i*2-1):
        print(' ',end=' ')
    for l in range(1,n+2-i):
        print(n-1,end=' ')
    print()
for m in range(1,n*2+1):
    print(n-1,end=' ')'''
#-------------------------
'''while n<6:
    print(n)
    n+=1'''
#---------------------
'''while n<10:
    n+=1
    continue'''
#----------------
#PALINDROME
'''a=input('word=')
prm=a[::-1]
if prm==a:
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')'''
#-------------------------------
'''a=input('value=')
a1=str(a)
prm=a1[::-1]
if prm==a:
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')'''
#------------------------------------
'''p=int(input('VALUE='))
q=str(p)
l=len(q)
res=0
for i in q:
    res+=int(i)**l
if res==p:
    print(p,'is a armstrong')
else:
    print(p,'is not ')'''
#------------------------------------
'''a=input('word=')
prm=a[::-1]
if prm==a:
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')'''
#----------------------------------------------------
'''n=input('n=')
res=0
while n>0:    #REVERSE AND DIGIT ADD
    digi=n%10
    res=res*10+digi
    n=n//10
print(res)
for i in n:
    res=res+int(i)
print(res)'''
#-----------------------------------------------------------
'''n=int(input('VALUE='))
res=0
for i in range(1,n):
    if n%i==0:
        res+=i
if res==n:
    print(n,'IS A PERFECT NUMBER')
else:
    print(n,'IS NOT PERFECT NUMBER')'''
#-----------------------------------------
'''n=int(input())
res=1
for i in range(1,n+1):
    res*=i
print(res)'''