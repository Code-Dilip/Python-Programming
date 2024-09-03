print()
n=int(input(" enter the lenght of the list: "))
data=[]
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the list: "))
    data.append(b)
print()
print(" the list is",data)
print()
def reverse_list(data):
    return ([data[i] for i in range(len(data)-1,-1,-1)])
reversed_list=reverse_list(data)

print(" the list after reversing by using coustom function is",reversed_list)
print()
data.reverse()
print(" the list after reversing .reverse() is",data)
print()
