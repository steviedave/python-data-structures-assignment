# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

# Extending the list with another list
my_list.extend([50, 60, 70])

# Removing the last element from the list using the pop() function
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print the final list
print("Final List:", my_list)
