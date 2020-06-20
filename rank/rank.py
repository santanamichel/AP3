from tabulate import tabulate

def saveRank(data):
    '''
        Essa função salva a pontuação e o nome do jogador 
        na última posição do arquivo rank.txt
    '''
    with open('rank.txt', 'a', encoding="UTF-8") as rank:
        data = str(data)+'\n'
        rank.write(data)
        
def ordRank():
    '''
        Essa função ordena por ordem de pontuação o ranking de jogadores
    '''
    with open('rank.txt','r',encoding="UTF-8") as rank:
        rankList = rank.read().split("\n")
        ranksDic = []
        for rank in rankList:
            if rank:
                splitRank = rank.split(',')
                ranksDic.append({
                    "Nome":splitRank[0],
                    "Pontos":int(splitRank[1]),
                    "Erros":int(splitRank[2])
                    })
        ranksDic = sorted(ranksDic, key=lambda ranks: ranks['Pontos'], reverse = True)
        return ranksDic

def mostrarRanking(ranks):
    '''
        Essa função mostra de maneira tabular o ranking dos jogadores
    '''
    tabelalist = []
    for rank in ranks:
        tabelalist.append([rank["Nome"], rank["Pontos"], rank["Erros"]])
    print("""
    -yyyyyyyyyyyyyyso/.                                                                         
    /mmmmmmmmd+sdmmmmmd+`     .+oooooooooo:      :ooooo/`  .ooooo+.  :ooooooo-  `-oo.           
    /mmmmmmmmy``smmmmmmd-     ommmmmmmmmmmd-     smmmmmmy- +mmmmmd-  +mmmmmmm+`:sdmmd+`         
    /mmmmmmmms``smmmmmmy`    -dmmmmmmodmmmms`    smmmmmmmd+ommmmmd-  +mmmmmmmyymmmmdy:          
    /mmmmmmmmy:odmmmmd+.    `ommmmmmy.ymmmmd-    smmmmmmmmmmmmmmmd-  +mmmmmmmmmmmmo-`           
    :mmmmmmmmmmmmmmmmh+`    -dmmmmmmo.ommmmms`   smmmmmmmmmmmmmmmd-  /mmmmmmmmmmmms:`           
    -dmmmmmmmdsdmmmmmmmh:  `smmmmmmmdddmmmmmd:   ommmmmhohmmmmmmmd-  /mmmmmmmdmmmmmmy/`         
    .hmmmmmmmh.-ymmmmmmds. -dmmmmmmd+++dmmmmmy   ommmmmy`.smmmmmmd-  /mmmmmmm::ymmmmmh:         
    `/sssssss+` `ohdys/.`  :sssssss/   /osssso`  :sssso/  `:ssssso`  -sssssss` `/yyo-`          
                  ```                                                            `              
    """)
    print(tabulate(tabelalist, headers=ranks[0].keys(), tablefmt='pretty'))

