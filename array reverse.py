# Array Reverse
#using the slice operation
def reversearray(arr):
    reverse=arr[::-1]
    return reverse
arr=[x for x in map(int,input().split())]
print(reversearray(arr))

#time complexity O(n)
#space complexity O(n)

#inbuilt functions also takes time ans space 