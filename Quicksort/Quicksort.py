#The quicksort is a technic to order elements in a array
#It uses recursion
def quicksort(arr):
    if len(arr)<2:#If the array size is smaller than 2...
        return arr
    else:
        pivot=arr[0]#Choice one pivot
        smallers=[]
        for i in arr[1:]:
            if i < pivot:#If the element is smaller than the pivot value
                smallers.append(i)
        biggests=[]
        for i in arr[1:]:
            if i > pivot:#If the element is biggest than the pivot value
                biggests.append(i)
        print(smallers, [pivot], biggests)
        return quicksort(smallers)+[pivot]+quicksort(biggests)
print(quicksort([10,5,7,6,3,2,11,8,9]))