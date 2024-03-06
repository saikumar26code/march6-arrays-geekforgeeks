#Array reverse
#using loop
def reverse(arr):
    for i in range(len(arr)//2): #upto mid only to reverse the array
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i] # here the assigning process is : 1st element= n-1 element and n-1 element = 1st element
    return arr
        
arr=[int(x) for x in input().split()]
print(reverse(arr))

#time complexity O(n)
#space complexity O(1)

# i got error like : return should be out of the loop to execute whole process
#to reverse any array , the array should traverse until the mid end of the array,
# if we traverse the entire array then we will get the same array as it is.