#promedioNotas
sw = 1
listaNotas = []
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción"))
contador=0
contador2=0
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            nota=int(input("Incorpore su nota, si desea salir, presione 0: "))
            if(nota != 0):
                listaNotas.append(nota)
                contador+=1
                contador2+=nota
            
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
else:
    print("Adiós")

print(f"se ingresaron {contador} notas")
print(f"las notas ingresadas fueron {listaNotas} ")
print(f"El promedio de notas fue{contador2/contador}: ")