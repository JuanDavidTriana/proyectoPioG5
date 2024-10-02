def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >=0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = clave
    return lista

numeros = [51,42,74,1,10]
print(insertion_sort(numeros))
