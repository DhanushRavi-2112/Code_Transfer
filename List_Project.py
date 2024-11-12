#LIST[]
'''fruits=['APPLE','ORANGE','GRAPE']
print(fruits)
print(fruits[1])'''
from itertools import count

#------------------------------
'''x=[[1,2],[3,4]]
print(x[0])
print(x[1][1])'''
#--------------------
#INDEXING IN LIST
'''animals=['lion','tiger','panther','cheetah']
print(animals.index('cheetah'))'''
#-----------------------
#REPLACE IN LIST
'''n=[1,2,3,4,5,6]   #INTEGER
n[0]=0
print(n)'''
#-----------------STRING
'''fruits=['apple','mango']
fruits[0]='orange'
print(fruits)'''
#---------------INSERT IN LIST-------------------
'''n=[1,2,3,4,5,6]
n.insert(0,0)
print(n)'''
#-----------------SORT IN LIST----------
#------------STRING SORTING-----------
'''n=['HII','SOLDIERS','WELCOME','BUDDY']
print(sorted(n))'''
#-------------INTEGER SORTING---------
'''n=[2,4,1,9,0,3]
print(sorted(n))'''
#-----------------
'''n=[9,8,7,6]
n.sort()
print(n)'''
#--------DELETE IN LIST------------
#---------DELETE IN STRING-------
'''n=['HII','HELLO','WELCOME']
del n[1]
print(n)'''
#------------DELETE IN INTEGER-----------
'''n=[1,1,2,3,4,5,6]
del n[0]
print(n)'''
#----------POP IN LIST---------
'''n=[1,2,3,4,5,6]
n.pop()    #Delete the last element
n.pop(0)   #Delete the indexing element
print(n)'''
#---------REMOVE IN LIST--------
'''n=[1,2,3,4,5]
n.remove(1)    #Delete The Mentioned Element  
print(n)'''
#------COUNT IN LIST-------
'''n=[1,2,3,2,4,5]
print(n.count(2))'''  #Count The Mentioned Value
#---------APPEND IN LIST--------
'''n=[1,2,3,4,5]     
n.append(6)
print(n)'''     #Append The Value
'''n=[1,3,5,7,9]
m=[2,4,6,8,10]
m.append(n)
print(m)'''      #Append The List
#-------EXTEND--------
'''n=[1,3,5,7,9]
m=[2,4,6,8,10]
m.extend(n)       #Extend means merge the list append the elments;
print(m)
m.sort()
print(m)'''
#------REVERSE THE LIST--------
'''n=[9,8,7,6,5]     #INTEGER REVERSE
n.reverse()
print(n)'''
#----STRING REVERSE--------
'''n=['a','b','c','d','e']
n.reverse()
print(n)'''
#-----CLEAR IN LIST-------
'''n=[1,2,3,4,5,6]
n.clear()      #Delete The All Elements
del n[:3]      #Delete The 0,1,2 indexing element
del n[:]        #Delete The All Elements
print(n)'''
#----
n=[1,2,3,4,5,6]


