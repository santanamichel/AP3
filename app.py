from forca import partida
from forca import sortearPalavras
import json
import random

def iniciarJogo():
    ''' Essa função serve para iniciar o jogo, pedindo o nome e iniciando a partida do jogo. '''

    nome = '' # Aqui será armazenado o nome do jogador
    palavrasChaves = [] # Aqui será carregada as perguntas

    # Apresentação e pegando nome do jogador
    print("Bem-vindo ao Jogo da Forca.")
    nome = input("Qual seu nome? ")

    # Carregar Palavras Chaves
    with open('palavrasChaves.json', 'r', encoding="UTF-8") as arquivoPalavras:
        palavrasChaves = json.load(arquivoPalavras)
    
    # Embaralhar perguntas carregadas
    random.shuffle(palavrasChaves)

    # Iniciando as partidas do jogo
    partida.iniciarPartida(nome, palavrasChaves)

if __name__ == "__main__":
    iniciarJogo() 