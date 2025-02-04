# Write a function that takes a list of values as input parameter and returns another list without any
# duplicates.
def duplicate(x):
    return list(set(x))
x = input("Enter a list separated with spaces: ")
y = x.split()
print("Original list: ",x)
print("List without duplicates: ",duplicate(y))