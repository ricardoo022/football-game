import projeto_extras

def le_replay(nome_ficheiro):
    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá 
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    
    dicionario = {"bola": [], "jogador_vermelho": [], "jogador_azul": []}
    with open (nome_ficheiro, 'r') as nome_arquivo:
        nome_arquivo.seek(0)
        linhas_arquivo=nome_arquivo.readlines()

        def constroi_dicionario(chave, a):  #constroi lista no dicionario e devolve
            dicionario[chave]=linhas_arquivo[a].strip().split(";")[:-1] 
            return dicionario  #devolve o dicionario com as listas
            

        #return dicionario
    
    def lista_coordenadas(chave): #mete listas dentro de cada lista de cada chave
        lista=dicionario[chave]
        for c in range(len(lista)):
            lista[c]=lista[c].split(",")  

        for b in range(len(lista)):  #mete para float cada elemento de cada lista dentro da lista
            sub_lista=lista[b]
            for a in range(2):
                sub_lista[a]=float(sub_lista[a])
                    
        for e in range(len(dicionario[chave])):  #transforma as listas em tuplos
            lista[e]=tuple(lista[e])   

        return lista 


    constroi_dicionario("bola", 0)        #atualiza o dicionario com as listas
    constroi_dicionario("jogador_vermelho", 1)
    constroi_dicionario("jogador_azul", 2)      

    dicionario={"bola":lista_coordenadas("bola"), "jogador_vermelho": lista_coordenadas("jogador_vermelho"), "jogador_azul": lista_coordenadas("jogador_azul")}
         
    return dicionario



def main():
    estado_jogo = projeto_extras.init_state()
    projeto_extras.setup(estado_jogo, False)
    replay = le_replay('replay_golo_jv_0_ja_1.txt')
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['objeto'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()


if __name__ == '__main__':
    main()