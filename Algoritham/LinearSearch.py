'''A Binary search is an algorithm which searches a target value in a list of
numbers. We use for loop to iterate through the list and then we print the
True or False if the algorithm finds that number and when it doesnot respectively'''


#import two libraries which can generate random numbers
from random import randint


# data = Put that in a variable
data = [1,2,3,4,5,6]

target = int(input('Enter the number between 0 to 10 ')) #correct this line
def linear_search(target, data ): #Enter the two necessary parameters
    for i in range(len(data)): #The two brackets denotes two missing function
        if data[i] == target:
            return True
        else:
            return False



print(data)
print(target)
print(linear_search(target,data))

#print the data
#print the target
#print the linear_search function and check the result

