numeros = []
numeros.append(int(input("Ingrese primer numero de loteria")))
numeros.append(int(input("Ingrese segundo numero de loteria")))
numeros.append(int(input("Ingrese tercer numero de loteria")))
numeros.append(int(input("Ingrese cuarto numero de loteria")))
numeros.append(int(input("Ingrese quinto numero de loteria")))

temp = []
for i in range(numeros.length): 
    if numeros[i]< numeros[i+1]:
        temp.append