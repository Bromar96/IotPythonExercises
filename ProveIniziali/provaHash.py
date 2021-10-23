myTable = {"000": "Gai Omar", "001": "Dalmasso Luca", "002":"Dogliani Gianmarco"}
print('first element: ', myTable["000"])

#insert
myTable["003"] = "Giuliano Emanuele"

#delete
del myTable["002"] 

#overwrite
myTable["003"] = "Fodale Luca"

print('All keys of my table: ')
keys=myTable.keys()
for i in keys:
	print(i)
	
print('All values of my table: ')
val=myTable.values() 
for i in val:
	print(i)
	
print('All items of my table: ')
items=myTable.items()
for i in items:
	print(i)

res="000" in myTable
print('Gai Omar è presente? ', res)

