# Program to find the minimum (or maximum) element of an array

#using built-in sorted function

def maxmin(arr):
    s=sorted(arr) #time complexity of this function is O(nlog(n))
    max_value=s[-1]
    min_value=s[0]
    return max_value,min_value
arr=[int(x) for x in input().split()]
print(maxmin(arr))

#time complexity O(nlog(n))
#space complexity O(1)
