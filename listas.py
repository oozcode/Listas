#Append(Valor) Agrega un valor a la ultima posicion
l1=[1,50,25,100,75]
print("Inicial: ",l1)

l1.append(250)
print("Append: ",l1)

#Extends([]): Agrega contenido listado al final de la lista
l2=[99,500]
l1.extend(l2)
print("Extend: ",l1)

#Insert(<index>,<obj>)El método insert(), permite añadir un elemento o valor en la posición indicada
l1.insert(6,999)
print("Insert: ",l1)

#Remove (valor):Entrego un valor, se busca y se elimina el valor otorgado
l1.remove(50)
print("Remove:",l1)
#Pop():Elimina el ultimo registro de de la posición indicada(Si no queda con valor borra el ultimo elemento registrado)
l1.pop(4)
print("Pop :",l1)

#Reverse(): Invierte el orden de la lista
l1.reverse()
print("Reverse:",l1)

#Sort():Ordena de forma ascendente la lista (Menor a Mayor)
l1.sort()
print("Sort:",l1)

#Sort(Reverse=True):Ordena de forma descendente ("Mayor a Menor")
l1.sort(reverse=True)
print("Sort(revrse=True):",l1)