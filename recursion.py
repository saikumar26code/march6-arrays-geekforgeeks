# Find a peak element which is not smaller than its neighbors

def peakeleutil(arr,low,high,n):
    mid=low+(high-low)/2
    mid=int(mid)
    if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid]):
        return mid
    elif mid>0 and arr[mid-1]>arr[mid]:
        return peakeleutil(arr,low,(mid-1),n)
    else:
        return peakeleutil(arr,(mid+1),high,n)
def peak(arr,n):
    print(peakeleutil(arr,0,n-1,n))
n=int(input())
arr=list(map(int,input().split()))
peak(arr,n)

#time complexity O(log n)
#space complexity O(log n)