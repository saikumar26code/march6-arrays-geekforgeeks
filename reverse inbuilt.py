#Array Reverse
#Using Inbuilt Method

def reverse(arr):
    res=list(reversed(arr))
    return res
arr=[x for x in map(int,input().split())]
print(reverse(arr))

#time complexity O(n)
#space complexity O(n)