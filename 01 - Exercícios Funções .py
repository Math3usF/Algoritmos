def soma(a,b): 
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def testeAB():
    # global a
    # global b

    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: ")) 
 
    if a > b:
        print("certo")
    else:
        while(a<b):
            print("deu erro")
            a = float(input("Insira o primeiro valor: "))
            b = float(input("Insira o segundo valor: "))
            # print(a,b)

    return a,b
                
a, b  = testeAB()
#print(resultado)
resultado1 = soma(a, b)
resultado2 = subtracao(a, b)
resultado3 = multiplicacao(a, b)
resultado4 = divisao(a, b)

#print textos 
#print("a soma é:", resultado1)
#print("a subtração é:", resultado2)
#print("a multiplicação é:", resultado3)
#print("a divisão é:", resultado4)

# print c/ textos (f"{resultado1:.3f}")
print(f"Resultados para {a} e {b}: Soma: {resultado1:.3f}, Subtração: {resultado2:.3f}, Multiplicação: {resultado3:.3f}, Divisão: {resultado4:.3f}")
