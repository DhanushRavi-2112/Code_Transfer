#n=int(input('VALUE='))
'''for i in  range(1,n+1):
    for j  in range(1,i):
        print(' ',end=' ')
    for k in range(1,n+2-i):
        print('*',end=' ')
    print()'''
#--------------------------
'''n=int(input('n='))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=' ')
    print()'''
#------------------------------
'''n=int(input())
for i in range(1,n+1):
    for j  in range(n+1-i,0,-1):
        print(j,end=' ')
    print()'''
#-----------------------------
'''n=int(input())
for i in  range(1,n+1):
    for j  in range(n-i,0,-1):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end=' ')
    print()'''
#-------------------------------
'''n=int(input('n='))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    for k in range()'''
#-------------------------------
'''n=int(input('n='))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n-i+1,end=' ')
    print()'''
#---------------------
'''m=input('enter=')
rev=m[::-1]
if m==rev:
    print(m,'IS A PALINDROME')
else:
    print(m,'IS NOT PALINDROME')'''
#----------------------------
'''n=int(input('n='))
res=1
for i in range(1,n+1):
    res*=i
print(n,'factorial is',res)'''
#------------------------
'''a=int(input('a='))
if a%2==0:
    print(a,'is even number')
else:
    print(a,'is odd number')'''
#--------------------------------
'''n=int(input('n='))
for i in range(1,n+1):
    if i%2==0:
        print(i)'''
#-------------------------
'''n=int(input('n='))
while n<11:
    if n%2==0:
        print(n)
    n+=1'''