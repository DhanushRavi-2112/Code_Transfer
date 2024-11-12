'''n=input('word=')
l=len(n)
for i in range(l):
    for j in range(i+1):
        print(n[j],end=' ')
    print()'''
'''n= input('enter=')
rev=' '
for i in n:
    rev=i+rev
    print(rev)'''
#---------------------------------
'''n=input('enter=')
rev=n[::-1]
print(rev)'''
#-------------------------------------
#PRIME NUMBER
'''n=int(input('n='))
if n>1:
    for i in range(2,n):
        if n%i==0:
        print(n,'is not prime')
        break
else:
    print(n,'is prime number')'''
#--------------------------------------
#LEAP YEAR
m=int(input('start year='))
n=int(input('end year='))
for i in range(m,n+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
#------------------------------
#SORTED
'''a=input()
print(sorted(a))'''
#------------------------
#ANAGRAM
'''x=input('x=').upper()
y=input('y=').upper()
x1=sorted(x)
y1=sorted(y)
if x1==y1:
    print('Anagram')
else:
    print('not anagram')'''


