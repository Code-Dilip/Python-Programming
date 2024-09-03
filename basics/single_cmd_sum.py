print()
n=int(input(" enter a positive number: "))
sum=sum([i*i for i in range(n)])
print(" the sum of sum() is",sum)
print()
sum_2=0
for i in range(n):
    sum_2+=i*i
print(" the loop sum is",sum_2)
print()