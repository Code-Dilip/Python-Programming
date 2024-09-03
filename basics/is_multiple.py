print()
n=int(input(" enter the value of n: "))
m=int(input(" enter the value of m: "))
def is_multiple(n,m):
    try:
        if(m%n==0):
            return 1
        else :
            return 0
    except:
        return -1
    finally:
        print(" Done!")

print()
state=is_multiple(n,m)
if(state==0):
    print(m,"is not a multiple of",n)
elif(state==1):
    print(m,"is multiple of",n)
elif(state==-1):
    print(" A Error occured!")
print()
