### Part Three -- your code goes here. 
number_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Original List: {number_list}")

number_list.sort()
print(f"Sorted List: {number_list}")

while 1 in number_list:
    number_list.remove(1)
print(f"List after remove all 1's is: {number_list}")

number_list.extend([7,8])
print(f"List after adding 7 and 8: {number_list}")

print(f"The final list is: {number_list}")
