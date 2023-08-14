import random
import os
import time

lista = ["Batman","Hulk","Thor","Flash","Wolverine","Deadpool","Falcão","Loki","Magneto","Demolidor" ]


contador = 0


while contador != 1:
    continuar = 0
    um = 1
    dois = 2
    tres = 3
    quantErros = 0
    listaerrada = []
    os.system('cls') or None
    palavra = random.choice(lista)
    contPalavra = len(palavra)

    underline = "_"
    
    tamanho=[]
    for indice in range(contPalavra):
        tamanho.append(underline)

    print(15 * "=" + " JOGO DA FORCA " + 15*"=")
    print (7*"_")
    print("|/    |")
    print("|")
    print("|")
    print("|")
    print(*tamanho, sep="")
    print(f"({contPalavra} letras)")
    
    continuar = int(input(f" Aperte 1 se deseja continuar/ digite 2 se deseja sortear outra palavra: / digite 3 para sair: "))
    print("=== Caso você demore mais de 2 minutos o jogo será reinciado!!! === ")
   
    if tres == continuar:
        os.system('cls') or None
        print("      obrigado!!!")
        print("───▄▄▄▄▄▄─────▄▄▄▄▄▄")
        print("─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄")
        print("▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌")
        print("█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█")
        print("█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█")
        print("▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌")
        print("─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀")
        print("───▀█▓▓▒▒░░░░░▒▒▓▓█▀")
        print("─────▀█▓▓▒▒░▒▒▓▓█▀")
        print("──────▀█▓▓▒▓▓█▀")
        print("────────▀█▓█▀")
        print("──────────▀")
        exit()
    if dois == continuar:
        palavra = random.choice(lista)
        os.system('cls') or None
    if um == continuar:
        timer = time.time()
        timerLimite = 120
        while quantErros <= 6:

            letraEscolhida = input("escolha uma letra: ")
            if letraEscolhida == '.':
                 quantErros+=6
                 break
                 

    
            for i,v in enumerate (palavra):
                   if letraEscolhida == palavra:
                        tamanho.clear()
                        tamanho.append(palavra)

                   elif letraEscolhida.upper() == v.upper():
                        tamanho.pop(i)    
                        tamanho.insert(i,letraEscolhida)   
            
            
            if letraEscolhida.upper() not in palavra.upper():
                 listaerrada.append(letraEscolhida)
                        
            os.system('cls') or None
            print(15 * "=" + " JOGO DA FORCA " + 15*"=")
            print (7*"_")
            print("|/    |")
            print("|")
            print("|")
            print("|")
            print(*tamanho, sep="")                    #sep é para tirar as , da lista
            print(f"({contPalavra} letras)")
            print(listaerrada)

            
                

            if letraEscolhida.upper() not in palavra.upper():
                quantErros = quantErros+1
            

            match quantErros:

                    case 1:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     o")
                        print("|")
                        print("|")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)               5 chances restantes!!!(◑‿◐)")
                        print(listaerrada)
                    case 2:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     o")
                        print("|     |")
                        print("|")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)              4 chances restantes!!! (/•ิ_•ิ)/")
                        print(listaerrada)

                    case 3:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     o")
                        print("|    /|")
                        print("|")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)              3 chances restantes!!!＼(>o<)ノ")
                        print(listaerrada)
                       
                    case 4:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     o")
                        print("|    /|\\")
                        print("|")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)              2 chances restantes!!! L(・o・)」") 
                        print(listaerrada)
                       
                       
                    case 5:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     o")
                        print("|    /|\\")
                        print("|    /")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)              1 chance restante!!!⊙▂⊙")
                        print(listaerrada)

                    case 6:
                        os.system('cls') or None
                        print(15 * "=" + " JOGO DA FORCA " + 15*"=")
                        print (7*"_")
                        print("|/    |")
                        print("|     ×͜×")
                        print("|    /|\\")
                        print("|    / \\")
                        print(*tamanho, sep="")                    #sep é para tirar as , da lista
                        print(f"({contPalavra} letras)               Você perdeu (｡•́︿•̀｡)")
                        print(listaerrada)
                        print(f"***** A palavra era {palavra} *****")
                        print("== Digite '.' letra para reiniciar ==")

            timerPercorrido = time.time() - timer
            if timerPercorrido > timerLimite:
                os.system('cls') or None
                print("💀💀💀 Acabou o tempo 💀💀💀")
                print(f"====== A palvra era: {palavra} ======")
                time.sleep(3)
                quantErros+=6
                break
            
            if "_" not in tamanho:
                os.system('cls') or None
                print("            Você ganhou 🥇🥇🥇 ")
                print("   ___________")
                print("  '._==_==_=_.'")
                print("  .-\:      /-.")
                print(" | (|:.     |) |")
                print("  '-|:.     |-'")
                print("    \::.    /")
                print("     '::. .'")
                print("       ) ( ")
                print("     _.' '._")
                print("     """""""       "")
                print("Digite '.' para continuar")
                
               