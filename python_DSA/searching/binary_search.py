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
def partition(arr,low,high):
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
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
quick_sort(data,0,len(data)-1)
def binary_search(arr,low,high,ele):
    if(len(arr)>1):
        mid=(low+high)//2
        if(arr[mid]==ele):
            return mid
        elif(arr[mid]>ele):
            return binary_search(arr,mid+1,high,ele)
        else:
            return binary_search(arr,low,mid-1,ele)
ele=int(input(" enter the search element that u want to search it in the list: "))
ele_pos=binary_search(data,0,len(data)-1,ele)
print()
print(" the position of the search element",ele,"in the list is",ele_pos)
print()