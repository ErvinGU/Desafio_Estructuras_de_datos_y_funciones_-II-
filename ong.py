def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact_" in clave:  
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif "prod_" in clave:  
            print(f"La productoria de {valor} es {productoria(valor)}")

calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
calcular(prod_2=[4, 6, 7, 4, 3], fact_3=8)
calcular(fact_4=7, prod_3=[2, 3, 5])
