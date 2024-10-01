def selection_sort(lista):
    tamanna = len(lista)
    for i in range(tamanna):
        min_idx = i
        for j in range(i+1,tamanna):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i] , lista[min_idx] = lista[min_idx], lista[i]
    return lista



numeros = [51,42,74,1,10]
print(selection_sort(numeros))
