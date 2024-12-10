#LIST[]
'''fruits=['APPLE','ORANGE','GRAPE']
print(fruits)
print(fruits[1])'''


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
#------------------TUPLE()------------
#----------Allow duplicate-------
#--------We can stored any datatype----
#--------We can't modify,add,remove----
#------Immutable-------
#PROGRAM:01
'''a=(1,2,3,4,5)
b=('hi','hello')
print(b[0])'''
#-----Type Cast------
#PROGRAM:02
'''n=(1,2,3,4,5)
m=list(n)
m.append(6)
l=tuple(m)
print(l)'''
#---------------------------------------------------------------------

#---------SET------{}---------
#-----Not allowed duplicate values----
#-----Unorder-----
#-----Mutable----
#-----Uniq data---
#PROGRAM:03
'''a={1,2,3,3,4,5}
b={'hi','hellooo','welcome'}
#print(a)
#print(b)
#a.add(6)    #Add new value
#print(a)
#-----Update
a.update(b)     #Update means merge the two sets
print(a)'''
#--------------
#PROGRAM:04
#----Remove
'''n={1,2,3,4}
n.remove(1)       #Remove the value
n.discard(2)      #These also remove the value
print(n)'''
#----Clear()
'''n={1,2,3}
n.clear()
#print(n)
m={}
print(m)'''
#------Union---Symbol is |
'''n={1,2,3}
m={3,4,5,6}
print(n|m)       #merge  the sets and another datatypes like tuple.., 
l=n.union(m)     # | means merge the only two sets
print(l)'''
#-----
'''n={3,1,6,2,5}
m=(7,8,9)
l=n.union(m)
print(l)'''
#---Intersection--Symbol is &
'''a={1,2,3,4}
b={3,4,5,6}    #Print the common value of sets
c={4,8,12}
print(a&b&c)'''
#----------------
'''a={1,2,3,4}
b=(3,4,5,6)   #If use operator work the same datype
#c={4,8,12}   #Use keyword work with another datatype
c=a.intersection(b)
print(c)'''
#----Difference----Symbol is -
'''m={1,2,3,4}
n={3,4,5,6}      #Print the left side varible difference values
l=(4,5,6)        #Use keyword work with another datatype
print(m-n)
print(m.difference(l))'''
#---Symmetric differnce-----
'''x={1,2,3,4}
y={3,4,5,6}     #Print the all difference values
z=(4,8,12)         
print(x.symmetric_difference(z))
print(x^y)'''
#------------------------
#Differnce_Update:
'''m={1,2,3,4}
n={3,4,5,6}        #It means differnciate value store the first variable;
m.difference_update(n)
print(m)'''
#---Symmetric_Update---
'''m={1,2,3,4}
n={3,4,5,6}       #Stored the all differnciate values in first variable;
m.symmetric_difference_update(n)
print(m)'''
#---Intersection_Update---
'''m={1,2,3,4}
n={3,4,5,6}      #Stored the common value in first variable;
m.intersection_update(n)
print(m)'''
#---Isdisjoint---
m={1,2,3,4}
n={3,4,5,6}     #two sets are in any common value print false;
print(m.isdisjoint(n))