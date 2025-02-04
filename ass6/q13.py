# write a recursive function to find the length of a string
def leng(n):
    if n == "":
        return 0
    return 1 + leng(n[1:])

n = input("Enter a string: ")
print(f"The length of {n} is {leng(n)}")