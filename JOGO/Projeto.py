import os
import time

####### Funções #######
def clear():
    # for windows
    if os.name == 'nt':
        os.name = os.system('cls')
  
    # for mac and linux
    else:
        os.name= os.system('clear')


######## AREA JOGO DA VELHA #########################

def tela_inicial():
    clear()
    print("░░░░▒█░▄▀▀▄░█▀▀▀░▄▀▀▄░░░█▀▄░█▀▀▄░░░▒█░░▒█░█▀▀░█░░█░░░░█▀▀▄")
    print("░░░░▒█░█░░█░█░▀▄░█░░█░░░█░█░█▄▄█░░░░▒█▒█░░█▀▀░█░░█▀▀█░█▄▄█")
    print("░▒█▄▄█░░▀▀░░▀▀▀▀░░▀▀░░░░▀▀░░▀░░▀░░░░░▀▄▀░░▀▀▀░▀▀░▀░░▀░▀░░▀")


    PalavraSecreta=input("\n\nInsira a palavra que outra pessoa deverá advinhar: ")
    clear()

    list_Palavra=list(PalavraSecreta)
    return list_Palavra



###### variaveis 
Repetir='s'
erros=0
acertos=0
tamanho= []
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#### VERIFICAR A ENTRADA JOGO DA VELHA
def check(entrada): 
    global palavra, tamanho, acertos, erros

    if entrada in palavra:
        if entrada in  tamanho:
            palavra("Letra repitida") 
            time.sleep(0.5)
            clear()

        else:
            for x in range(len(palavra)):
                if entrada == palavra[x]:
                    acertos += 1
                    tamanho.pop(x)
                    tamanho.insert(x, entrada)
                    if acertos == len(palavra):
                        clear()
                        print("\nVocê Venceu Pararabéns!!! \nPalavra:", palavra)
                        time.sleep(2.5)
                        clear()
                        break
    
    else:
        print("Letra errada!!")
        time.sleep(0.5)
        erros += 1
        clear()

    if erros == 7:
        print("Você atingiu o limite de erros!!!\n\n")
        time.sleep(2)
        clear()


#### JOGAR JOGO DA VELHA
def play():
    global erros, tamanho, palavra, acertos, check, FORCAIMG

    for i in range(len(palavra)):
        tamanho.append("_")
    
    while True:
        clear()
        print('Total de letras:', len(palavra), '| erros:',erros)
        print("\n"+FORCAIMG[erros],"\n")
        

        print("\n\nPalavra:", tamanho,"\n")
        try:
            entrada=input("digite uma letra: ")
        except:
            entrada=input("Valor invalido! tente novamente: ")
        check(entrada)

        if erros == 7 or acertos == len(palavra):
            break




################ AREA JOGO DA FORCA #######################################

JogarNovamente="s"
jogadas=0
quemJoga=2 #1=CPU / 2J=ogador
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    clear()
    print("    0   1   2")
    print("0: ",velha[0][0], "|", velha[0][1], "|", velha[0][2])
    print("   ------------")
    print("1: ",velha[1][0], "|", velha[1][1], "|", velha[1][2])
    print("   ----------")
    print("2: ",velha[2][0], "|", velha[2][1], "|", velha[2][2])
    print("   ------------")
    print("\nJogadas", jogadas)


#### vez do jogador
def JogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga==2 and jogadas<maxJogadas:   
        try:
            linha=int(input("Linha..: "))

            coluna=int(input("Coluna.: "))

            while velha[linha][coluna]!=" ":
                linha=int(input("Linha..: "))
                coluna=int(input("Coluna.: "))
  
            velha[linha][coluna]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e/ou coluna invalida")
            wait = input("Pressione ENTER para digitar outro valor")


##### vez da maquina
def CPUJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga==1 and jogadas<maxJogadas:
        linha=random.randrange(0,3)
        coluna=random.randrange(0,3)

        while velha[linha][coluna]!=" ":
            linha=random.randrange(0,3)
            coluna=random.randrange(0,3)
        
        velha[linha][coluna]="O"
        jogadas+=1
        quemJoga=2

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]

    for s in simbolos:
        vitoria="n"

        #Verificar vitoria em linhas
        IndiceL=IndiceC=0
        while IndiceL<3:
            soma=0
            IndiceC=0

            while IndiceC<3:
                if(velha[IndiceL][IndiceC]==s):
                    soma+=1

                IndiceC+=1     
            if soma==3:
                vitoria=s
                break
            IndiceL+=1

        if(vitoria!="n"):
            break

        #Verificar vitoria em colunas
        IndiceL=IndiceC=0
        while IndiceC<3:
            soma=0
            IndiceL=0

            while IndiceL<3:
                if(velha[IndiceL][IndiceC]==s):
                    soma+=1
                IndiceL+=1
            if soma==3:
                vitoria=s
                break
            IndiceC+=1
            
        if(vitoria!="n"):
            break

        #Verificar vitoria em diagonal 1
        soma=0
        IndiceD=0

        while IndiceD<3:
            if(velha[IndiceD][IndiceD]==s):
                soma+=1
            IndiceD+=1
        if soma==3:
            vitoria=s
            break

        #Verificar vitoria em diagonal 2
        soma=0
        IndiceDC=2
        IndiceDL=0

        while IndiceDC >= 0:
            if(velha[IndiceDL][IndiceDC]==s):
                soma+=1
            IndiceDL+=1
            IndiceDC-=1
        if soma==3:
            vitoria=s
            break

    return vitoria

def Redefinir():
    global velha; global vit; global maxJogadas; global quemJoga; global jogadas

    jogadas=0
    quemJoga=2 #1=CPU / 2J=ogador
    maxJogadas=9
    vit=""
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]


############### AREA DO JOGO ################################




def main():
    global tamanho, erros, acertos, palavra, entrada, check;
    global velha, vit, maxJogadas, quemJoga,  jogadas, Repetir;


    while True:

        clear()
        print("Qual jogo você quer jogar?\n\n")
        print("1 - Jogo da velha")
        print("2 - Jogo da forca")
        print("3 - SAIR")
        resposta = int(input("Opção: "))


        #### jogo da velha
        if resposta == 1:
            while Repetir == 's':
                clear()
                tela()
                JogadorJoga()
                CPUJoga()
                vit=verificarVitoria()
                if vit!="n" or jogadas>=maxJogadas:
                    break

                print("FIM DE JOGO")
                if vit=="X" or vit=="O":
                    print("Resultado: Jogador",vit,"Venceu")
                else:
                    print("Resultado: Empate")
                
                Repetir = input(F"Digite [s] para continuar ou [n] para sair: ")
                Redefinir()


        #### jogo da forca
        elif resposta == 2:
            while Repetir == 's':
                clear()
                erros=0
                acertos=0
                tamanho= []
                palavra=tela_inicial()
                play()

                try:
                    Repetir = input("Gostaria de jogar de novo?[S/n]")
                except:
                    print("Valor invalido!!!")
                    Repetir = input("Gostaria de jogar de novo?[S/n]")
        
        else:
            print("\n\nObrigado por jogar!!!")
            time.sleep(2)
            break

                    

if __name__ == '__main__':
    main()
    