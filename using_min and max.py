#Program to find the minimum (or maximum) element of an array

#using max and min 

def maximun(arr):
    return max(arr)
def minimun(arr):
    return min(arr)
ar=[int(x) for x  in input().split()] 
print(maximun(ar),minimun(ar))

#time complexity O(n)
#space complexity O(1)