#The goal is apply the Divide to conquer technique using recursion
#Recursion is a situation when a function call itself
#The Divide to conquer technique is when we try to approximate the base case
def Add(arr):
    if (len(arr)==0):#If the array is void...
        return 0
    elif (len(arr)==1):#If the array have jsut one element
        return arr[0]
    else:
        #Separate the first value of the rest of the list and call again the function until it be void
        totalValue=arr[0]
        totalValue+=Add(arr[1:])
        return totalValue
print(Add([6,8,6,7]))