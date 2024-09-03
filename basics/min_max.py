print()
n=int(input(" enter the no. of elements: "))
data=[]
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element: "))
    data.append(b)
print(" The list of elements is",data)
print()
def min_max(data):
    small=big=data[0]
    for i in data:
        if(i>=big):
            big=i
        elif(i<=small):
            small=i
        else:
            return (small,big)
    
(min,max)=min_max(data)
print()
print(" the smallest element in the list",data,"is",min)
print(" the largest element in the list",data,"is",max)
print()