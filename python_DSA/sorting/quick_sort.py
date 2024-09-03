print()
n=int(input(" enter the lenght of the list: "))
data=[]
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element in the list: "))
    data.append(b)
print()
print(" the list is",data)
print()

def pivot(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if(low<high):
        pi=pivot(arr,low,high)
        quick_sort(arr,0,pi-1)
        quick_sort(arr,pi+1,high)

quick_sort(data,0,len(data)-1)
print(" the list afte the quick sort is",data)
print()