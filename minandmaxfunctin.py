#Program to find the minimum (or maximum) element of an array

#using max and min function

def getmaxmin(arr): #created two arrays
    res=arr[0] #res is 1st index if array has only one element
    res1=arr[0] 
    for i in range(1,len(arr)):
        res=max(res,arr[i])
        res1=min(res,arr[i])
    return res,res1
arr=[int(x) for x in input().split()]
print(getmaxmin(arr))

#time complexity O(n)
#space complexity O(1)