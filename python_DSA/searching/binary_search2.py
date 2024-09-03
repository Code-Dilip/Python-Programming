print()
n=int(input(" enter the length of the list: "))
data=[]
print()
for i in range(n):
    b=int(input(" enter the "+str(i+1)+" element into the list: "))
    data.append(b)
print()
print(" the list is",data)

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
        quick_sort(arr,0,pi-1)
        quick_sort(arr,pi+1,high)

print()
quick_sort(data,0,len(data)-1)
print(" the array after sorting is",data)
print()
def binary_search(arr,low,high,ele):
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==ele):
          return mid
        elif(arr[mid]>ele):
          high=mid-1
        else:
          low=mid+1
    return -1

kp="y"
while(kp=="y"):
  ele=int(input(" enter the search element to search it in the array: "))
  search_ele_pos=binary_search(data,0,len(data)-1,ele)
  if(search_ele_pos==-1):
    print(" the search element",ele,"is not found in the array ")
  else:
    print(" the search element",ele,"is found in the array at the position",search_ele_pos)
  kp=str(input(" Want to search more elements (y/n) ?: "))
  print()
print()
print()