
def skip(skip_elements):
    lista = []
    for index, elements in enumerate(skip_elements):
        if index % 2 == 0:
            lista.append(elements)
    
    print(lista)

skip(["a", "b", "c", "d", "e", "f", "g"])
skip(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])



###if skip_elements.index(skip_elements[num]) % 2 == 0:
##lista.append(skip_elements[num])
#print(lista)
#num+=1

#skip(["a", "b", "c", "d", "e", "f", "g"])
#skip(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])###