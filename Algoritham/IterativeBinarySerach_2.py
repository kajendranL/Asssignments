#Itrative Binary Search

# from a given array find x

def Binary_Search(data,x):
    #find the mid point of the array
    left = 0                 # from mid point to left side
    right = len(data)-1         # from mid point to right side

    while left<=right:
        mid = left + (right - left)//2  # divide the array to find the mid point

        if x == data[mid]:       # check if x is present in the middle or not
            return x     # return the x which is in the middle
        elif x > data[mid]: # then search  towards right side from left
            left = mid+1
        else:
            right = mid -1 # then search towards left from right
    return False # if x is not found by above code return False

# call by reference variable
 
print(Binary_Search([1,2,3,4,5],1))
print(Binary_Search(["Orange", "Apple","Mango", "Grapes","Plums"],"Apple"))
print(Binary_Search([10,20,56,48,97,36,],29))
print(Binary_Search([2,4,6,8],4))
