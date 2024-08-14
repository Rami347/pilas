1
2
# def listarPila(Pila, top, maxPila)
#     iniPila(Paux, topAux)
#     while(top<>0)
#         eliPila(pila, top, dato)
#         print(dato)
#         adiPila(Paux,topAux, maxPila,dato)
#     end while

#     while(topAux<>0)
#         eliPila(Paux, topAux, dato)
#         adiPila(pila, top, maxPila, dato)
#     end while
# end listarPila



# if __name__=="__main__":
#     run()

def iniPila(pila):
    print("Pila inicializada")

def adiPila(pila, maxPila, item):
    if len(pila) == maxPila:
        print("Pila llena")
    else:
        pila.append(item) 

def eliPila(pila):
    if len(pila) == 0:
        print("Pila vacía")
        return None
    else:
        return pila.pop()  # pop elimina el último elemento

def listarPila(pila, maxPila):
    Paux = []
    # Vaciar la pila original y llenar la pila auxiliar mientras se imprimen los elementos
    while len(pila) != 0:
        dato = eliPila(pila)
        if dato is not None:
            print(dato)
            adiPila(Paux, maxPila, dato)
    
    # Restaurar los elementos de la pila auxiliar a la pila original
    while len(Paux) != 0:
        dato = eliPila(Paux)
        if dato is not None:
            adiPila(pila, maxPila, dato)

def run():
    p = []
    maxPila = int(input("maxPila: "))
    
    # Inicializamos la PILA
    iniPila(p)

    # Introducimos los datos a la pila
    for i in range(1, maxPila + 1):
        dato = int(input("Inserte un dato: "))
        adiPila(p, maxPila, dato)

    print("Contenido de la pila:")
    listarPila(p, maxPila)

    print("Pila después de listar:")
    print(p)
    

if __name__ == "__main__":
    run()
