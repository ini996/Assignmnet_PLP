#Create an empty list
my_list = []

#append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print('my_list: ', my_list)

#insert 15 at the second position
my_list.insert(1, 15)
print('Insert 15 at 2nd position: ', my_list)

#Extend list with another list
my_list.extend([50, 60, 70])
print('Extended list: ', my_list)

#Remove the last element from my_list
my_list.pop()
print('Remove last element: ', my_list)

#sort my_list in ascending order
my_list.sort()
print(my_list)

#find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print('Index of 30: ', index_of_30)


