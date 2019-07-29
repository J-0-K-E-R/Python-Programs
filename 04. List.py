list1 = [10, "Dragon", 48, "Run", 100, "Forrest", 101, "Run!"]        # creating a list

print(list1)

print(list1[::2])   # Elements with jump 2

print(list1[::-2])  # Reverse list with jump 2

list2 = [42, 35, 26, 78]    # Creating 2nd list

print(sum(list2))       # Printing sum of elements of list 2

print(list1[3], list2[3])      # printing specific elements from both lists.

list2[1:3] = ["Orange", "Black"]       # Updating list

print(list2)

del list1[0]        # Deleting 0th element from first list

list1.append("HA!")     # Appending element into list

print(len(list1))       # Printing length of list

list1.extend(list2)     # Adding list 2 to list 1

list3 = [42, 35, 26, 78]

print(list3.count(87))     # Calculates total occurrence of given element of List

print(list3.index(78))     # Returns the index of specific element

print(list3.index(78, 2, 4))      # This will check from index 2 to 3 only

print(min(list3))       # Min element from list

print(max(list3))       # Max element from list

list1.pop(1)        # Removing element at index 2

list1.remove(78)     # Remove element by using element value

print(list1)

list1.reverse()     # Reversing of the list

print(list1)

list3.sort()        # Sort the list in ascending way

print(list3)

if 42 in list3:     # Checking if 42 is in list3
    print("YES")

if 101 not in list3:        # Return true if element is not in the list
    print("NO")