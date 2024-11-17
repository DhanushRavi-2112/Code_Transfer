#                ---DICTIONARY---
#--SYNTAX: VAR_NAME={'KEY' : 'VALUE'}
'''
n={
    'Name':'Stark',
    'Id':11015,
    'Rank':12
}
print(n.keys())
print(n.values())
print(n['Id'])'''
#--Change the values----
'''lap={
    'Brand':'Apple',
    'Model':'Macbook Pro',
    'Processor':'m1',
    'Ram':16
}
lap['Processor']='m2'
print(lap)
#--Delete---
del lap['Ram']
print(lap)'''
#----------Clear()------------
#Syntax: -- var_name.clear()--
#clear() means delete the all key and values;
#--------Copy()------
'''lap={
    'Brand':'Apple',
    'Model':'Macbook Pro',
    'Processor':'m1',
    'Ram':16
}
pc=lap.copy()
print(pc)'''
#-------From_Keys-----
#Syntax: var_name3=dict.fromkeys(var_1,var_2);
'''m={'x','y','z'}
n=4
l=dict.fromkeys(m)
print(dict.fromkeys(m,n))
print(l)'''
#-----get()----
#Syntax:  var.get('key')
#----items-----
#Syntax:  var.items()
m={'x':10,'y':20,'z':30}
print(m.items())


