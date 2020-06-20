import random

def sortear(palavrasChaves = [], palavrasFeitas = []):
    '''
        Essa função tem o objetivo de sortear uma palavra chave ainda não feita no jogo e retorna-la
    '''

    palavrasNaoFeitas = [] # Aqui será armazenada as palavras não feitas ainda no jogo

    # Aqui será feita uma comparação, das palavras já feitas e das não feitas ainda
    for palavra in palavrasChaves:
        if palavra not in palavrasFeitas:
            palavrasNaoFeitas.append(palavra)

    # Será sorteada uma palavra ainda não feita do jogo
    palavraSorteada = random.choice(palavrasNaoFeitas)

    return palavraSorteada
