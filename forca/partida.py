#Programa da forca - V1.1

from forca import sortearPalavras
from rank import rank
from forca import imprimirForca as impForca

def iniciarPartida(nome, palavrasChaves, palavrasFeitas=[], pontos=0, TotalErros=0):
  ''' Essa função inicia as partidas, fazendo alterações nos pontos 
      e nas vidas do jogar, caso necessário '''

  nVidas = 6 # Aqui é o número máximo de derrotas que o jogador pode ter (Para aparecer todo o desenho, o valor deve ser 6)
  erros=0 # Número de erros do jogador
  temp=[] # letras corretas ou _ caso ainda não acertadas que aparece no jogo
  letrasJaUsadas = [] # Letras já usadas pelo jogador

  palavraSorteada = sortearPalavras.sortear(palavrasChaves, palavrasFeitas) # Pegar uma palavra ainda não sorteada
  palavrasFeitas.append(palavraSorteada) # Adiciona a nova palavra sorteada a lista de palavras já sorteadas

  # Colocar _ para cada número de letras da palavra
  for letra in palavraSorteada["palavra"]:
    temp.append('_')

  # Inicia partida
  while True:
    print('\n'*20) # limpa a tela
    print("Partida:", len(palavrasFeitas),"de", len(palavrasChaves)) # Mostra o número de partidas jogadas
    print ("Dica:\n", palavraSorteada["dica"], "\n") # Mostra dica na tela, antes da forca
    
    # Mostra as letras já usadas pelo jogador
    print ("Letras já usadas: ",    ", ".join(letrasJaUsadas))

    # imprime desenho da forca
    impForca.forca(erros)

    #imprime a adivinhacao
    print('\n\nAdivinhe: ', end='')

    for let in temp: # _ _ _ _ 
      print(let, end=' ')
    print('\n'*2)

    #Verifica se perdeu
    if erros==nVidas:

      print ("Infelizmente... Você perdeu... Mas não desista, continue jogando! =D")
      
      # Salvar Ranking
      rank.saveRank(nome+","+str(pontos)+","+str(TotalErros))

      # Mostrar Ranking
      rankPontuacoes = rank.ordRank()
      rank.mostrarRanking(rankPontuacoes)

      break #sai do jogo (sai do while)

    #Verificar se terminou partida
    ganhouJogo=True
    for let in temp: # _ _ _ 
      
      # Se houver qualquer caracter na variavel temp que seja _, o jogador não terá ganho
      if let=='_':     
        ganhouJogo=False

    # Caso ele tenha ganhado
    if ganhouJogo: 

      # O jogador ganhará de pontos o equivalente ao número de letras da palavra acertada
      pontos += len(palavraSorteada["palavra"]) 

      # Se todas a palavras foram feitas, acabou o jogo e ele ganhou
      if len(palavrasFeitas) == len(palavrasChaves):
        print('\nPARABÉNS VENCEDOR!!!')
        print("Fim de jogo!")
        # Salvar Ranking
        rank.saveRank(nome+","+str(pontos)+","+str(TotalErros))

        # Mostrar Ranking
        rankPontuacoes = rank.ordRank()
        rank.mostrarRanking(rankPontuacoes)

        return

      # Caso não tenha terminado todas as palavras, é carregada a próxima fase
      else:
        iniciarPartida(nome, palavrasChaves, palavrasFeitas, pontos, TotalErros)
        return

    # Caso não tenha ganho o jogo e nem excedido o número máximo de tentativas, o jogo continua
    if not ganhouJogo: 
      
      #captura a letra do usuario
      letraDig=input("Informe uma letra: ")
      letrasJaUsadas.append(letraDig)

      #verifica se acertou alguma letra
      errouLetra=True
      for i, let in enumerate(palavraSorteada["palavra"]):
        if palavraSorteada["palavra"][i]==letraDig:
          temp[i]=palavraSorteada["palavra"][i]
          errouLetra=False
      if errouLetra:
        erros=erros+1
        TotalErros+=1 # Soma os erros com todos os outros erros das perguntas anteriores, se tiver
        