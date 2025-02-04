# write a recursive function to find nth Fibonacci number
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)
n=int(input("Enter a number: "))
print(f"The number at {n}th position of the fibonacci series is {fibo(n)}")