import os

def sep():
    print("\n===================================\n")

def comprimento (c):
    while True:
        f = float(input("Digite a frequencia em Hz: "))
        if f > 0.3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e m" % (c/f))
            print("Tipo de onda: onda de radio")
            break
        elif f > (10**-3) or f < 0.3:
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e mm" % ((c/f)*(10**3)))
            print("Tipo de onda: micro-onda")
            break
        elif f > 7*(10**-7) or f < (10**-3):
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
            print("Tipo de onda: infravermelho")
            break
        elif f > 7*(10**-7) or f < 4*(10**-7):
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
            print("Tipo de onda: luz visivel")
            break
        elif f > 4*(10**-7) or f < 3*(10**-8):
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
            print("Tipo de onda: ultravioleta")
            break
        elif f > 3*(10**-8) or f < 3*(10**-11):
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
            print("Tipo de onda: raio-x")
            break
        elif f < 3 * (10**-11):
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
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
        op = int(input("Escolha o calculo ou saia:\n1 - Frequencia\n2 - Comprimento de onda:\n0 - Sair\nEscolha:  "))
        if op == 1:
            frequencia(c)
        elif op == 2:
            comprimento(c)
        elif op == 0:
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("Opcao invalida! Escolha uma das opcoes")
        sep()

if __name__ == "__main__":
    main()
