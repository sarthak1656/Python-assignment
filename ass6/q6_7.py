# Write a function that takes n as an input and creates a list of n lists such that ith list contains first
# five multiples of i.

# Sample output
# >>>enter the n:3
# [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

def multiples(n):
    result=[]
    for i in range(1,n+1):
        x=[i*j for j in range (1,6)]
        result.append(x)
    return result
n = int(input("Enter a number: "))
print(multiples(n))



# Write a function to solve question 6 using list comprehension
def multiples(n):
    return[[i*j for j in range(1,6)] for i in range(1,n+1)]

n = int(input("Enter a number: "))
print(multiples(n))