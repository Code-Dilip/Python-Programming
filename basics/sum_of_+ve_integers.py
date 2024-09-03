print()
n=int(input(" enter the positive integer: "))
while(n<=0):
    print(" Invalid input")
    n=int(input(" enter the positive integer only: "))
    print()
def square_sum(n):
    square_sum=0
    for i in range(n):
        square_sum+=i*i
    return square_sum
print()
square_sum=square_sum(n)
print(" the sum of the squares of the number less than",n,"is",square_sum)
print()
    