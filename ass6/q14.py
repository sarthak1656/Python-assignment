# write a recursive function to reverse a string
def rev(s):
    if s=="":
        return ""
    return s[-1] + rev(s[:-1])

n = input("Enter a string: ")
print(f"The reverse of {n} is {rev(n)}")