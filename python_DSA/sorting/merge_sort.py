print()
data=[]
n=int(input(" enter the length of the list: "))
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the array: "))
    data.append(b)
print()
print(" the list is",data)
print()
def merge_sort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        l=arr[0:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0

        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
                k+=1
            else:
                arr[k]=r[j]
                j+=1
                k+=1
        
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
    else:
        return arr

merge_sort(data)
print(" the list after sorting is",data)
print()