#dividing the array
def partition(arr,p,q):
    x=arr[p]
    i=p
    for j in range(p+1,q+1):
        if arr[j]<x:
            i=i+1
            #temp=arr[i]
            #swapping the value
            # print(x)
            # print(arr[i],arr[j])
            arr[i],arr[j]=arr[j],arr[i]
    arr[p],arr[i]=arr[i],arr[p]
    return i
#quicksort implementation
def quicksort(arr,p,q):
    #single array
    if p==q:
        return arr[p]
    if p<q:
        mid=partition(arr,p,q)
        #print(mid)
        #recursive function
        quicksort(arr,p,mid-1)
        quicksort(arr,mid+1,q)

arr1=[50,70,80,30,40,88,19,27,69]
arr2=[6,4,5,2,1]
quicksort(arr1,0,len(arr)-1)
print(arr1)
# for i in range(0,-1):
#     print(i)