print()
data=[]
n=int(input(" enter the lenght of the list: "))
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the list: "))
    data.append(b)
print()
print(" the list is",data)
print()
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

bubble_sort(data)
print(" the list after the sorting is",data)
print()