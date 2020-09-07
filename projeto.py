import os
import math

def sep():
    print("\n===========================================\n")

def classificaOnda(c):
    while True:
        op = int(input("Entre com: \n1 - Numero de onda\n2 - Frequencia angular\nEscolha: "))
        if op == 1:
            no = float(input("Numero de onda (em rad/m): "))
            comprimento = (2 * math.pi)/no
            frequencia = (2 * math.pi * c)/no
            break
        elif op == 2:
            fa = float(input("Frequencia angular (em rad/s): "))
            frequencia = fa/(2 * math.pi)
            comprimento = (fa * c)/(2 * math.pi)
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opcao invalida! Digite uma opcao valida.")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Frequencia: %.2e Hz" %frequencia)
    
    if comprimento > 0.3:
        print("Comprimento de onda = %.2e m" %comprimento)
        print("Tipo de onda: onda de radio")
    elif comprimento > 0.001:            
        print("Comprimento de onda = %.2e mm" % (comprimento*(10**3)))
        print("Tipo de onda: micro-onda")
    elif comprimento > 0.0000007:
        print("Comprimento de onda = %.2e nm" % (comprimento*(10**9)))
        print("Tipo de onda: infravermelho")
    elif comprimento > 0.0000004:
        print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
        print("Tipo de onda: luz visivel")
    elif comprimento > 0.00000003:
        print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
        print("Tipo de onda: ultravioleta")
    elif comprimento > 0.00000000003:
        print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
        print("Tipo de onda: raio-x")
    else:
        print("Comprimento de onda = %.2e nm" % (comprimento * (10**9)))
        print("Tipo de onda: raio gama")

def numeroOnda (c):
    while True:
        op = int(input("Entre com:\n1 - Frequencia\n2 - Comprimento de onda\nEscolha:  "))
        if op == 1:
            f = float(input("Digite a freuquencia em Hz: "))
            no = (2 * math.pi * c)/f
            fa = 2 * math.pi * f
            break
        elif op == 2:
            co = float(input("Digite o comprimento de onda em m: "))
            no = (2 * math.pi)/co
            fa = (2 * math.pi * co)/c
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opcao invalida! Digite uma opcao valida.")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Numero de onda: %.2e rad/m" %no)
    print("Frequencia angular: %.2e rad/s" %fa)

def campoMagMax (c):
    ceMax = float(input("Digite o valor do campo eletrico maximo em V/m: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    cmMax = ceMax/c
    print("Campo magnetico maximo: %.2e T" %cmMax)

def campoEleMax (c):
    cmMax = float(input("Digite o valor do campo magnetico maximo em T: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    ceMax = c * cmMax
    print("Campo eletrico maximo: %.2e V/m" %ceMax)

def comprimento (c):
    while True:
        f = float(input("Digite a frequencia em Hz: "))
        comprimento = c/f
        if comprimento > 0.3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e m" %comprimento)
            print("Tipo de onda: onda de radio")
            break
        elif comprimento > 0.001:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e mm" % (comprimento*(10**3)))
            print("Tipo de onda: micro-onda")
            break
        elif comprimento > 0.0000007:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % (comprimento*(10**9)))
            print("Tipo de onda: infravermelho")
            break
        elif comprimento > 0.0000004:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
            print("Tipo de onda: luz visivel")
            break
        elif comprimento > 0.00000003:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
            print("Tipo de onda: ultravioleta")
            break
        elif comprimento > 0.00000000003:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % (comprimento *(10**9)))
            print("Tipo de onda: raio-x")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % (comprimento * (10**9)))
            print("Tipo de onda: raio gama")
            break

def frequencia (c):
    while True:
        op = int(input("Escolha a unidade do comprimento de onda:\n1 - nm\n2 - mm\n3 - m\n4 - km\nEscolha: "))
        if op == 1:
           co = float(input("Digite o comprimento de onda: "))
           co = co * (10**-9)
           break
        elif op == 2:
           co = float(input("Digite o comprimento de onda: ")) 
           co = co * (10**-3)
           break
        elif op == 3:
           co = float(input("Digite o comprimento de onda: ")) 
           break
        elif op == 4:
           co = float(input("Digite o comprimento de onda: ")) 
           co = co * (10**3)
           break
        else:
           os.system('cls' if os.name == 'nt' else 'clear') 
           print("Opcao invalida! Digite uma opcao valida")
    frequencia = c/co
    os.system('cls' if os.name == 'nt' else 'clear')
    
    tipoDeOnda = ""

    if frequencia > (10**19):
        tipoDeOnda = "raio gama"
    elif frequencia > (10**16):
        tipoDeOnda = "raio X"
    elif frequencia > (7.5 * (10**14)):
        tipoDeOnda = "ultravioleta"
    elif frequencia > (4.28 * (10**14)):
        tipoDeOnda = "luz visivel"       
    elif frequencia > (3 * (10**11)):
        tipoDeOnda = "infravermelho"
    elif frequencia > (10**9):
        tipoDeOnda = "micro-onda"
    else:
        tipoDeOnda = "onda de radio"

    print("Frequecia da onda: %.2e Hz" % frequencia)
    print("Tipo de onda: %s" %tipoDeOnda)

# Variaveis globais
c = 3 * (10**8) #velocidade da luz em m/s
h = 6.6226 * (10**-34) #constante de planck em J . s 
e = 1.602 * (10**-19) #carga elementar em C

def main ():
    while True:
        op = int(input("Escolha o calculo ou saia:\n1 - Frequencia\n2 - Comprimento de onda\n3 - Campo magnetico maximo\n4 - Campo eletrico maximo\n5 - Numero de onda e frequencia angular\n6 - Classificar olhando a equacao senoidal\n0 - Sair\nEscolha:  "))
        if op == 1:
            frequencia(c)
        elif op == 2:
            comprimento(c)
        elif op == 3:
            campoMagMax(c)
        elif op == 4:
            campoEleMax(c)
        elif op == 5:
            numeroOnda(c)
        elif op == 6:
            classificaOnda(c)
        elif op == 0:
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("Opcao invalida! Escolha uma das opcoes")
        sep()

if __name__ == "__main__":
    main()
