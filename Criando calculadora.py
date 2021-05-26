import os
print("=============== Calculadora em python 1.0 ================")
print()
print("MENU")
print()
print("Somar========[1]")
print("Subtrair=====[2]")
print("Multiplicar==[3]")
print("Dividir======[4]")
print()

enter = int(input("INFORME 1,2,3 OU 4 :"))

if(enter == 1):
    print("Somar :")
    n1 = int(input("Informe o Número para SOMAR :"))
    n2 = int(input("Informe o Número para SOMAR :"))
    print("Resultado da Soma :",n1 + n2)
if(enter == 2):
    n1 = int(input("Informe o Número para SUBTRAIR :"))
    n2 = int(input("Informe o Número para SUBTRAIR :"))
    print("Resultado da Subtração :",n1 - n2)
if(enter == 3):
    n1 = int(input("Informe o Número para MULTIPLICAR :"))
    n2 = int(input("Informe o Número para MULTIPLICAR :"))
    print("Resultado da Multiplicação :",n1 * n2)
if(enter == 4):
    n1 = int(input("Informe o Número para DIVIDIR :"))
    n2 = int(input("Informe o Número para DIVIDIR :"))
    print("Resultado da Divisão :",n1 / n2)    
if(enter >=5):
    print("opção invalida.")    


os.system("pause")   