print()
data=[]
n=int(input(" enter the length of the list: "))
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the list: "))
    data.append(b)
print()
print(" the list is",data)
print()
def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
                
selection_sort(data)
print(" the list after sorting is",data)
print()