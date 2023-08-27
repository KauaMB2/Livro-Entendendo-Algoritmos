import random
#Organazing a list of bands according their visualizations
bandViews = [
    ("U2", random.randint(1, 150)),
    ("Coldplay", random.randint(1, 150)),
    ("Queen", random.randint(1, 150)),
    ("The Beatles", random.randint(1, 150)),
    ("Led Zeppelin", random.randint(1, 150)),
    ("Pink Floyd", random.randint(1, 150)),
    ("Radiohead", random.randint(1, 150)),
    ("Nirvana", random.randint(1, 150)),
    ("The Rolling Stones", random.randint(1, 150)),
    ("AC/DC", random.randint(1, 150))
]
def searchBiggest(arr):
    value=arr[0][1]#Define the biggest value
    biggestIndex=0#Define the index
    for i in range(0,len(arr)):
        if arr[i][1] > value:#If the current value is biggest than the old
            value=arr[i][1]#update the biggest value
            biggestIndex=i#Update the index
    return biggestIndex
def SelectionSort():
    novoArr=[]#Defines the new array
    for i in range(0,len(bandViews),1):
        index=searchBiggest(bandViews)#Get the biggest index
        novoArr.append(bandViews.pop(index))#Remove the item from the original array and add it in the  sorted
    return novoArr
sortedData=SelectionSort()
for bandName, views in sortedData:
    print(f"{bandName}: {views}")
print("=================================")