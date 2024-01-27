import math
import turtle as t
import functools
import random
import time

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 4
BOLA_START_POS = (5,5)
 


# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

def marcar_golo(equipa,estado_jogo):
    texto=t.Turtle()
    texto.color('black')
    texto.write("GOLO "+equipa, align="center", font=('Arial',50,"normal"))
    estado_jogo["janela"].update()

    time.sleep(1)
    texto.clear()
    estado_jogo["janela"].update()
    time.sleep(1)
    texto.hideturtle()

def comecar_jogo(estado_jogo):
    texto=t.Turtle()
    texto.color('red')
    for i in range(1,4):
        texto.write(i, align="left", font=('Arial',50,"normal"))
        estado_jogo["janela"].update()

        time.sleep(0.5)
        texto.clear()
        estado_jogo["janela"].update()
        time.sleep(0.5)
        texto.hideturtle()
     




def bandeira_alemanha():
    t.pu()
    t.home()
    t.seth(90)
    t.fd(260)
    t.seth(180)
    t.fd(60)
    def retangulo(cor, angulo):
        t.fillcolor(cor)
        t.begin_fill()
        t.seth(0)
        t.fd(50)
        t.left(angulo)
        t.fd(15)
        t.left(angulo)
        t.fd(100)
        t.left(angulo)
        t.fd(15)
        t.left(angulo)
        t.fd(50)
        t.end_fill()
    
    
    retangulo("black",90) 
    retangulo("red",270)
    t.pu()
    t.seth(270)
    t.fd(30)
    t.seth(0)
    retangulo("yellow",90)
    t.hideturtle()


def bandeira_polonia():
    t.pu()
    t.home()
    t.seth(90)
    t.fd(255)
    t.seth(0)
    t.fd(50)
    def retangulo(cor, angulo):
        t.fillcolor(cor)
        t.begin_fill()
        t.seth(0)
        t.fd(35)
        t.left(angulo)
        t.fd(20)
        t.left(angulo)
        t.fd(70)
        t.left(angulo)
        t.fd(20)
        t.left(angulo)
        t.fd(35)
        t.end_fill()
    
    
    retangulo("white",90) 
    retangulo("red",270)
    t.hideturtle()
    





def jogador_cima(estado_jogo, jogador):
    '''Cria a turtle novo_estado através do j_1 que foi retornado na criação do jogador '''
    
    novo_estado= estado_jogo[jogador] 
    coordenadas = novo_estado.ycor()
    if(coordenadas<ALTURA_JANELA/2-PIXEIS_MOVIMENTO):
      novo_estado.setheading(90)
      novo_estado.fd(PIXEIS_MOVIMENTO)

    return novo_estado

def jogador_baixo(estado_jogo, jogador):
    '''Cria a turtle novo_estado através do j_1 que foi retornado na criação do jogador '''
    novo_estado= estado_jogo[jogador] 
    coordenadas = novo_estado.ycor()
    if(coordenadas>-ALTURA_JANELA/2+PIXEIS_MOVIMENTO):
        novo_estado.setheading(-90)
        novo_estado.fd(PIXEIS_MOVIMENTO)
    return novo_estado
    
def jogador_direita(estado_jogo, jogador):
    '''Cria a turtle novo_estado através do j_1 que foi retornado na criação do jogador '''
    novo_estado= estado_jogo[jogador] 
    coordenadas = novo_estado.xcor()
    if(coordenadas<LARGURA_JANELA/2-PIXEIS_MOVIMENTO):
      novo_estado.setheading(0)
      novo_estado.fd(PIXEIS_MOVIMENTO)
    if(coordenadas<LARGURA_JANELA/2-PIXEIS_MOVIMENTO*1.5):
        novo_estado.setheading(0)
        novo_estado.fd(PIXEIS_MOVIMENTO/2)

    return novo_estado

def jogador_esquerda(estado_jogo, jogador):
    '''Cria a turtle novo_estado através do j_1 que foi retornado na criação do jogador '''
    novo_estado= estado_jogo[jogador] 
    coordenadas = novo_estado.xcor()
    if(coordenadas>-(LARGURA_JANELA/2-PIXEIS_MOVIMENTO)):
      novo_estado.setheading(180)
      novo_estado.fd(PIXEIS_MOVIMENTO)
    if(coordenadas>-(LARGURA_JANELA/2-PIXEIS_MOVIMENTO*1.5)):
        novo_estado.setheading(180)
        novo_estado.fd(PIXEIS_MOVIMENTO/2)

    return novo_estado

def desenha_linhas_campo():
    def balizas(lado,a): 
        '''O lado corresponde ao tamanho da baliza, o "a" serve para inverter o lado mais pequeno da baliza'''
        t.penup()
        t.goto(lado,100)
        t.pendown()
        t.setheading(0)
        t.fd(a*50)
        t.setheading(90)
        t.fd(-200)
        t.setheading(180)
        t.fd(a*50)

    t.penup()
    t.goto(LARGURA_JANELA/6,ALTURA_JANELA/2)
    t.setheading(-90)
    t.pendown()
    t.pensize(1)
    t.pencolor(("forest green"))
    t.fillcolor("forest green")
    t.begin_fill()
    t.fd(ALTURA_JANELA)
    t.setheading(180)
    t.fd(LARGURA_JANELA/6)
    t.setheading(90)
    t.fd(ALTURA_JANELA)
    t.setheading(0)
    t.fd(LARGURA_JANELA/6)
    t.end_fill()
    t.penup()
    t.goto(LARGURA_JANELA/2,ALTURA_JANELA/2)
    t.setheading(-90)
    t.pendown()
    t.pensize(1)
    t.pencolor(("forest green"))
    t.fillcolor("forest green")
    t.begin_fill()
    t.fd(ALTURA_JANELA)
    t.setheading(180)
    t.fd(LARGURA_JANELA/6)
    t.setheading(90)
    t.fd(ALTURA_JANELA)
    t.setheading(0)
    t.fd(LARGURA_JANELA/6)
    t.end_fill()
    t.penup()
    t.goto(-LARGURA_JANELA/6,ALTURA_JANELA/2)
    t.setheading(-90)
    t.pendown()
    t.pensize(1)
    t.pencolor(("forest green"))
    t.fillcolor("forest green")
    t.begin_fill()
    t.fd(ALTURA_JANELA)
    t.setheading(180)
    t.fd(LARGURA_JANELA/6)
    t.setheading(90)
    t.fd(ALTURA_JANELA)
    t.setheading(0)
    t.fd(LARGURA_JANELA/6)
    t.end_fill()
    t.pencolor("white")
    t.pensize(7)
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.setheading(-90)
    t.fd(600)
    t.penup()
    t.goto(-50,0)
    t.pendown()
    t.circle(RAIO_MEIO_CAMPO)
    balizas(-512,1)
    balizas(512,-1)
    t.penup()
    t.goto(512-LADO_MENOR_AREA-LADO_MENOR_AREA,10)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-512+LADO_MENOR_AREA+LADO_MENOR_AREA,10)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-512,0.75*LADO_MAIOR_AREA)
    t.pendown()
    t.fd(-0.75*LADO_MAIOR_AREA)
    t.setheading(-90)
    t.fd(LADO_MAIOR_AREA *0.4)
    t.setheading(180)
    t.circle(LADO_MAIOR_AREA/3,-180)
    t.setheading(90)
    t.fd(LADO_MAIOR_AREA )
    t.setheading(-90)
    t.fd(LADO_MAIOR_AREA+LADO_MAIOR_AREA*0.5 )
    t.setheading(180)
    t.fd(0.75*LADO_MAIOR_AREA)
    t.penup()
    t.goto(512,0.75*LADO_MAIOR_AREA)
    t.pendown()
    t.fd(0.75*LADO_MAIOR_AREA)
    t.setheading(-90)
    t.fd(LADO_MAIOR_AREA *0.4)
    t.setheading(180)
    t.circle(LADO_MAIOR_AREA/3,180)
    t.setheading(90)
    t.fd(LADO_MAIOR_AREA )
    t.setheading(-90)
    t.fd(LADO_MAIOR_AREA+LADO_MAIOR_AREA*0.5 )
    t.setheading(0)
    t.fd(0.75*LADO_MAIOR_AREA)
    t.penup()
    t.goto(LARGURA_JANELA/6,ALTURA_JANELA/2)
    t.setheading(-90)
    t.pendown()
    
    bandeira_alemanha()
    bandeira_polonia()
    
    pass


def criar_bola():
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, \\
    começa na posição BOLA_START_POS com uma direção aleatória. \\ 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. \\ 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    dicionario_bola={}
    direcaox=random.uniform(-1,1)
    direcaoy=random.uniform(-1,1)
    bola=t.Turtle()
    bola.shape("circle")
    bola.pu()
    bola.goto(BOLA_START_POS)
    dicionario_bola["Direção xx"]=direcaox 
    dicionario_bola["Direção yy"]=direcaoy        
    dicionario_bola["objeto"]=bola
    dicionario_bola["Posicao anterior"]=None

    print(dicionario_bola)

    return dicionario_bola #dicionario pedido



def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    j_1 = t.Turtle()
    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''
    j_1.penup()
    j_1.goto(x_pos_inicial,y_pos_inicial)
    j_1.pendown
    j_1.shape("circle")
    j_1.color(cor)
    j_1.shapesize(stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE)



    return j_1


def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo

def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window

def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("ALEMANHA: 0\t\tPOLONIA: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    
    pontuacaoV=estado_jogo['pontuacao_jogador_vermelho'] 
    pontuacaoA=estado_jogo['pontuacao_jogador_azul']  
    contador=1


    with open ('numerodeJogos','a+') as f: #tem q ser a+ senão estaria sempre a criar um ficheiro novo se usasse w, se usasse r não criava o ficheiro quando ele não exista
        f.seek(0)
        linha=f.read()  #le a o numero
        with open ('numerodeJogos','r+') as f:
            if not linha:
                f.write(str(contador))
            else: 
                contador=int(linha) 
                contador+=1 #ao numero lido adicona 1 e escreve

            f.seek(0)
            f.write(str(contador))     
               

    with open("historico_resultados.csv", "a+") as ficheiro:
        ficheiro.seek(0)
        primeira_linha= ficheiro.readline()
        if not primeira_linha:                              # se a primeira linha não tiver nada 
            ficheiro.write("NJogo ,JogadorVermelho,JogadorAzul\n")
            ficheiro.write("{},".format(contador))
            ficheiro.write("{},{}\n ".format(pontuacaoV,pontuacaoA))
            

        else:
            ficheiro.write("{},".format(contador))
            ficheiro.write("{},{}\n ".format(pontuacaoV,pontuacaoA))
            
            
            
    

    print("Adeus")
    estado_jogo['janela'].bye()
    

  
    


def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    desenha_linhas_campo()
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "black")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul
    comecar_jogo(estado_jogo)


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("ALEMANHA: {}\t\tPOLONIA: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))

def movimenta_bola(estado_jogo):
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''

    bola=estado_jogo["bola"]['objeto'] #vai criar uma nova bola
    posx = bola.xcor()
    posy=bola.ycor()
    bola.goto(posx + estado_jogo["bola"]['Direção xx'], posy + estado_jogo["bola"]['Direção yy'])   #vai buscar o objeto bola e a
    
    pass

def verifica_colisoes_ambiente(estado_jogo):
    '''
    Função responsável por verificar se há colisões com os limites do ambiente, 
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais, 
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''
    bola=estado_jogo["bola"]['objeto']
    if bola.xcor()>=512:
        estado_jogo["bola"]["Direção xx"] *=-1
    elif bola.xcor()<=-512:
        estado_jogo["bola"]["Direção xx"] *=-1
    elif bola.ycor()>=300:
        estado_jogo["bola"]["Direção yy"] *=-1
    elif bola.ycor()<=-300:
        estado_jogo["bola"]["Direção yy"] *=-1     



def replay(estado_jogo):
    valorv = str(estado_jogo['pontuacao_jogador_vermelho'])
    valora=str(estado_jogo['pontuacao_jogador_azul'])
    with open ("replay_golo_jv_" + valorv +"_ja_"+valora +".txt","w") as nome_arquivo: #coordenada bola
            for c in estado_jogo['var']['bola']:
                nome_arquivo.write(str(c).replace("(","").replace(")",";"))
            nome_arquivo.write("\n")  
            for a in estado_jogo['var']['jogador_vermelho']:
                nome_arquivo.write(str(a).replace("(","").replace(")",";"))
            nome_arquivo.write("\n")  
            for i in estado_jogo['var']['jogador_azul']:
                nome_arquivo.write(str(i).replace("(","").replace(")",";"))
                




    


def verifica_golo_jogador_vermelho(estado_jogo):
 
    # Obtém a posição da bola
    bola = estado_jogo["bola"]["objeto"]
    posy_bola=bola.ycor()
    posx_bola=bola.xcor()

    # Verifica se a bola ultrapassou a linha de gol do time vermelho
    if posy_bola < LADO_MAIOR_AREA/2 and posx_bola >= LARGURA_JANELA/2 and posy_bola>-LADO_MAIOR_AREA/2:
        # Atualiza a pontuação do jogador vermelho
        marcar_golo("ALEMANHA",estado_jogo)
        estado_jogo['pontuacao_jogador_vermelho'] += 1


        # Reinicia o jogo com a bola ao centro
        bola.goto(BOLA_START_POS)
        estado_jogo['bola']["Direção xx"] = random.uniform(-1, 1)
        estado_jogo['bola']["Direção yy"] = random.uniform(-1, 1)

        
        update_board(estado_jogo)
        # Atualiza o quadro de resultados
        replay(estado_jogo)
        
        return estado_jogo['pontuacao_jogador_vermelho']
    
   
        





    


                




    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
                


def verifica_golo_jogador_azul(estado_jogo):
    # Obtém a posição da bola
    bola = estado_jogo["bola"]["objeto"]
    posx_bola = bola.xcor()
    posy_bola = bola.ycor()

    # Verifica se a bola ultrapassou a linha 
    if posy_bola < LADO_MAIOR_AREA/2 and posx_bola <= -LARGURA_JANELA/2 and posy_bola>-LADO_MAIOR_AREA/2:
        # Atualiza a pontuação do jogador azul
        marcar_golo("POLONIA",estado_jogo)
        estado_jogo['pontuacao_jogador_azul'] += 1

        # Reinicia o jogo com a bola ao centro

        bola.goto(BOLA_START_POS)

        estado_jogo['bola']["Direção xx"] = random.uniform(-1, 1)
        estado_jogo['bola']["Direção yy"] = random.uniform(-1, 1)
        update_board(estado_jogo)
        replay(estado_jogo)
        

    return estado_jogo['pontuacao_jogador_azul']
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]_ja_[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    pass


def verifica_golos(estado_jogo):
    verifica_golo_jogador_vermelho(estado_jogo)
    verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    jogador_azul=estado_jogo['jogador_azul']
    bola=estado_jogo["bola"]["objeto"]
    posx_jogador=jogador_azul.xcor()
    posy_jogador=jogador_azul.ycor()
    posx_bola=bola.xcor()
    posy_bola=bola.ycor()



    distancia = math.sqrt((posx_bola-posx_jogador)**2) + ((posy_bola- posy_jogador)**2)
    if distancia <= RAIO_BOLA + RAIO_JOGADOR:
        estado_jogo["bola"]["Direção xx"] *=-1
        estado_jogo["bola"]["Direção yy"] *=-1





def verifica_toque_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    jogador_vemelho=estado_jogo['jogador_vermelho']
    bola=estado_jogo["bola"]["objeto"]
    posx_jogador=jogador_vemelho.xcor()
    posy_jogador=jogador_vemelho.ycor()
    posx_bola=bola.xcor()
    posy_bola=bola.ycor()



    distancia = math.sqrt((posx_bola-posx_jogador)**2) + ((posy_bola- posy_jogador)**2)
    if distancia <= RAIO_BOLA + RAIO_JOGADOR:
        estado_jogo["bola"]["Direção xx"] *=-1
        estado_jogo["bola"]["Direção yy"] *=-1
    else:
        estado_jogo["bola"]["Direção xx"] *=1
        estado_jogo["bola"]["Direção yy"] *=1
    pass

def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola']['objeto'].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())



def main():
   
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while True:
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        verifica_golos(estado_jogo)
        guarda_posicoes_para_var(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)

if __name__ == '__main__':
    main()



