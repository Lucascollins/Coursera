def listMane(value):
    lista = value
    print(lista)
    lista.append("Ravena") #append adiciona um valor no final da lista
    print(lista)
    lista.insert(0,"Luana") #insert funciona primeiro você delimita a posição da casa que a sua informação vai ficar depois você coloca a informação
    print(lista)
    lista.remove("Daniel")
    print(lista)
    lista.pop(1)#remove o valor na lista pelo indice removido da lista
    print(lista)
    lista[0] = "Lucas Gostoso"
    print(lista)

listMane(["Lucas","Daniel"]
)