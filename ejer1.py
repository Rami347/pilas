def iniPila(pila):
    print("Pila incializada")

def adiPila(pila, maxPila, item):
    if(len(pila) == maxPila):
        print("Pila llena")
    else:
        pila.append(item) #append inserta elemento

def eliPila(pila):
    if(len(pila) == 0):
        print("PILA VACIA")
    else:
        item = pila.pop()       #pop elimina el ultimo elemento   (sacar elementos)      
    
    return(item)

def listarPila(pila, maxPila):
    paux = []
    iniPila(paux)
    while(len(pila) !=0):
        dato = eliPila(pila)
        print(dato)
        adiPila(paux, maxPila, dato)

    while(len(paux) !=0):
        dato = eliPila(paux)    
        adiPila(pila, maxPila, dato)




if __name__=="__main__":
    run()

# tarea para la proxima el listarPila