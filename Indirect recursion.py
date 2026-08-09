#In-Direct Recursion
#code to check the given numberis even or odd using In-direct recursion
def even(n):
    if n==0:
        print("Even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print("Odd")
        return
    even(n-1)
n=int(input("Enter a number :"))
even(n)
    