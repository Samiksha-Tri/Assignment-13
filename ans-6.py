"""Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""

firstlist=['java','python','Sql']
secondlist=['C','Cpp','NoSql']
print("first list :",firstlist)
print("second list",secondlist)
firstlist.append(secondlist[0])       #append operation
print("new first list :",firstlist) 