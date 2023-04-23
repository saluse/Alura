#print('Pagamento de diária de carro e KMs rodados')
#d = int(input('Quantos dias alugados? '))
#k = float(input('Quantos KMs rodados? '))
#pd = d * 60
#pk = k * 0.15
#print('O preço a pagar é de: R${}'.format(pd + pk))

'''print("**********************************************")
print("****** Bem Vindo ao Jogo de Advinhação *******")
print("**********************************************")

NS = 42
chute = str(input("Digite seu número: "))
print("Você chutou {}".format(chute))
chute = int(chute)
if chute == 42:
    print("Você acertou!")
else:
    if chute > NS:
        print("Você errou!, seu chute foi mnais alto do que o número.")
    elif chute < NS:
        print("Voce errou, seu chute foi mais baixo do que o numnero.")
print("Fim de Jogo")

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")
print("****************************************")  
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12
print("****************************************") 

usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

print("****************************************")

total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")

    # Aula 04/05

print("R$ {:7.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))

ns = 42
tt = 3

for rodada in range(1, tt + 1):
    print("Tentativa {} de {}.".format(rodada, tt))
    chute = str(input("Digite um número entre 1 e 100: "))
    print("Você digitou {}".format(chute))
    chute_int = int(chute)

    if chute_int < 1 or chute_int > 100:
        print("Você deve digitar um número válido")
    acertou = chute_int == ns
    maior = chute_int > ns
    menor = chute_int < ns

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou, o seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou, o seu chute foi menor do que o número secreto")
Paulo = 1
Juliana = 2
Tamires = 3
import random

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")'''

# arquivo a.py
def executa():
    print("Executando a")
# arquivo b.py
def executa():
    print("Executando b")
# principal.py

import a
import b