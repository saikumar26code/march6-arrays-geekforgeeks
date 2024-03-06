# Find a peak element which is not smaller than its neighbors

def peakele(arr,n):
    if n==1: #if length of the array is one then return the 
        return 0
    if arr[0]>=arr[1]:#if the 1st ele is greater than 2nd ele, then return the 0th index
        return 0
    if arr[n-1]>=arr[n-2]:#if the last ele is greater than second last ele , then return last index
        return n-1
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]: #excluding the first and last ele, traverse the array to find the peak ele
            return i #returns the peak index of the array (only )
arr=list(map(int,input().split()))
n=int(input())
print(peakele(arr,n))

#time complexity o(n)
#auxiliary complexity o(1)