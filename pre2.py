import os

def comprimento (c):
    while True:
        op = int(input("Escolha o tipo de onda: \n1 - Onda de radio\n2 - Micro-ondas\n3 - Infravermelho, visivel, ultravioleta, raios X ou raio gama\nEscolha:"))
        if op == 1:
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e m" % (c/f))
            break
        elif op == 2:
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e mm" % ((c/f)*(10**3)))
            break
        elif op == 3:
            f = float(input("Digite a frequencia em Hz: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Comprimento de onda = %.2e nm" % ((c/f)*(10**9)))
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
    print("Frequecia da onda: %.2e Hz" % frequencia)

# Variaveis globais
c = 299792458

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


if __name__ == "__main__":
    main()
