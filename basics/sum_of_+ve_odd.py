print()
n=int(input(" enter the positive integer: "))
print()
def sum_of_odd(n):
    sum=0
    for i in range(n):
        if(i%2!=0):
            sum+=i*i
    return sum
odd_sum=sum_of_odd(n)
print(" the sum of the squares of odd no. lesser than is",odd_sum)
print()