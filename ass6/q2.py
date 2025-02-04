#  Write a function that takes a list of numbers as input from the user and produces the corresponding
# cumulative list where each element in the list at index i is the sum of elements at index j <= i.
# L=[1,2,3,4] Then newL=[1,3,6,10]
def csum(x):
    l=[]
    s=0
    for i in x:
        s+=i
        l.append(s)
    return l
a = int(input("Enter a list separated with spaces. "))
x=[]
for i in a.split():
    x.append(int(i))
res=csum(x)
print("Original list: ",a)
print("Cumulative list is: ",res)