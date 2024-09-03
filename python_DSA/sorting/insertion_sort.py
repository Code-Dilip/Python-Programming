print()
n=int(input(" enter the length of the list: "))
data=[]
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the list: "))
    data.append(b)
print()
print(" the list is",data)
print()
def insertion_sort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while (j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

insertion_sort(data)
print(" the array after the insertion sort is",data)
print()