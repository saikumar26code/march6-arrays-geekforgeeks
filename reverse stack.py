#array reverse
#using stack 
def reverse (arr):
    stack=[]
    for ele in arr:
        stack.append(ele)
    for i in range(len(arr)):
        arr[i]=stack.pop()
    return arr
arr=[int(x) for x in input().split()]
print(reverse(arr))

#time complexity O(n)
#space complexity O(n)