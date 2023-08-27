def buscamaior(arr):
    maior=arr[0]#Define the biggest value
    maiorIndice=0#Define the index
    for i in range(0,len(arr)):
        if arr[i] > maior:#If the current value is biggest than the old
            maior=arr[i]#update the biggest value
            maiorIndice=i#Update the index
    return maiorIndice
def ordenacaoSelecao(arr):
    novoArr=[]
    for i in range(len(arr)):
        maior=buscamaior(arr)
        novoArr.append(arr.pop(maior))#Remove the item from the original array and add it in the  sorted
    return(novoArr)
print(ordenacaoSelecao([5,4,6,45,7,8,9,9]))
