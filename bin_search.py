# Find a peak element which is not smaller than its neighbors

def peak(arr,n):
    l,r=0,n-1 
    while (l<=r):
        mid= (l+r)>>1
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid]):
            break
        elif mid>0 and arr[mid-1]>arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return mid
n=int(input())
arr=list(map(int,input().split()))
print(peak(arr,n))

#time complexity O(log n)
#space complexity O(1)