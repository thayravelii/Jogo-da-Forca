from random import *

palavras = ['aviao', 'caneca', 'sorvete', 'carro', 'leao', 'macaco', 'girassol']
letras_descobertas = []
tentativas = []
chances = 5
selecao = randrange(0, len(palavras))
pl_sl = palavras[selecao]
quant_letras = len(palavras[selecao])


print('Seja bem-vindo ao Jogo da Forca. Você deseja iniciar o jogo?')
iniciar = str(input('Sim ou não:')).strip().upper()
if iniciar == "SIM":
    print("Você terá 5 chances para acertar a palavra. Boa sorte!")
else:
    if iniciar == "NAO":
        print('Até a próxima!')
    quit()

    print('A palavra selecionada tem {} letras'.format(quant_letras))



while True:
    resposta = pl_sl
    for a in pl_sl:

        if a not in letras_descobertas:
            resposta = resposta.replace(a,"_")
    print(resposta)
    letras = input('Digite uma letra:')
    let = []
    for percorre in pl_sl:
        if percorre == letras:
            let.append(letras)

    if let:
        for l in let:
            letras_descobertas.append(l)

    if letras in pl_sl:
        print('Você acertou a letra :) ')


    else:
        print('Você errou a letra :( ')
        tentativas.append(letras)
        chances -= 1
        print('Agora te restam {} chances'.format(chances))
        if chances <= 0:
            print('Infelizmente você perdeu todas as suas chances :(. Tente de novo!')
            quit()
    if len(letras_descobertas) == len(pl_sl):
        print('Parabéns! Você ganhou')
        quit()

