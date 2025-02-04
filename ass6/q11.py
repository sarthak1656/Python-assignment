# write a recursive function that multiplies two positive numbers and returns the
# result(use + operator)
def mult(a , b):
    if b == 0:
        return 0
    return (a + mult(a,b-1))

a1 = int(input("Enter the first number(a): "))
b1 = int(input("Enter the second number(b): "))
print(f"{a1} X {b1} = {mult(a1,b1)}")