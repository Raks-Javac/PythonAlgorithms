# Lesson four
# Working with List

Best_friends = [
"Jane","Jone","Kate","grid"
];
Normal_friends =["john","micheal","joshua","katee"];
                    # keeping in mind that elements in a list starts from 0
# this outputs the whole list
print(Best_friends)
print(Best_friends[2])


# changing the list at run time just specify the index
Best_friends[1] = "grey"
print(Best_friends)


#this joins another list to the specified list
Best_friends.extend(Normal_friends)
print(Best_friends)


# helps you to add either a list or an element to the end of the list
new_friend = 'Mary'
Best_friends.append(new_friend)


# helps you to remove an element from  list
Best_friends.pop(0)


# this helps you to insert an element with its index and pushes element coming index +1
Best_friends.insert(1,"Mary")
print(Best_friends)



# this helps you to remove an element
Best_friends.remove(Best_friends[2])
# this removes  grey from the list because its of index 2
print(Best_friends)


# to check if an element is in a list
Best_friends.index("Mary")
print(Best_friends)


# this help you to count the numberof the specified element is in the list
Best_friends.count("katee")
print(Best_friends)


# this helps you to sort you list
Best_friends.sort()
print(Best_friends)


# this helps you to reverse your list
Best_friends.reverse()
print(Best_friends)