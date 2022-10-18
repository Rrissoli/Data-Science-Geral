import random






def imprimir_mensagem_boasvindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")









def definir_variaveis():
    words = []
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        words.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(words))
    palavra_secreta = words[numero].upper()
    return palavra_secreta
    
    

    

def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().upper()


def marca_chute_correto(palavra_secreta,chute, valores):
    index = 0
    for letra in palavra_secreta:
                if(chute == letra):
                    valores[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1



      



def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]




def jogar():
    imprimir_mensagem_boasvindas()
    palavra_secreta = definir_variaveis()
    enforcou = False
    acertou = False
    valores = inicializar_letras_acertadas(palavra_secreta)
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta,chute, valores)
        else: 
            erros +=1 
        enforcou = erros == 6 
        acertou = "_" not in valores        
        print(valores)
        print("jogando ...")
        if(acertou):
            print('ganhou')
        elif(enforcou):
            print('Perdeu')
     
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar() 
    
