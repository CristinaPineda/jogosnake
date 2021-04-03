import pygame, random
from pygame.locals import *

#variáveis
ACIMA = 0
DIREITA = 1
ABAIXO = 2
ESQUERDA = 3

AMARELO = (255,255,0)
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERDE = (0,128,0)
VERDE2 = (127,255,0)
CHOCOLATE = (210,105,30)
FUSCIA = (255,0,255)
INDIGO = (75,0,130)
VERMELHO = (255,0,0)
VERMELHO2 = (139,0,0)
OURO =(255,215,0)
AZUL = (0,0,255)

CORES = [AMARELO,BRANCO,VERDE,VERDE2,VERMELHO,VERMELHO2,CHOCOLATE,FUSCIA,INDIGO,OURO,AZUL]

direcao = ESQUERDA

global cor_new

#função que define o campo de inserção da comidinha da cobra 
def local_grid():
	x= random.randint(15,580) #posiciona aleatóriamente a comidinha nos parametros do eixo x e y
	y= random.randint(25,580)
	return (x//10 * 10, y//10 * 10) # retorna a comidinha alinhada com a cobrinha

#função que define o encontro com a comidinha
def encontro(x1, x2):
	return (x1[0] == x2[0]) and (x1[1] == x2[1]) # verifica se os parametros da cobrinha e da comidinha se encontraram

#cada vez que a cobrinha comer ela muda de cor! (ahh é fofinho vai! :) 
def mudar_cor():
	cor1 = random.choice(CORES)
	cor2 = random.choice(CORES)
	cobra_tam.fill(cor1)
	alvo.fill(cor2)


#função que define a tela de game over
def perdeu():
	frases = ["VOCÊ PERDEU!", "GAME OVER", "FIM DE JOGO"] #frase de fim de jogo
	frase = random.choice(frases) # escolhe uma frase
	tela.fill((54,54,54)) # renderiza uma tela na cor escolhida
	terminou = fonte.render(frase, True, VERMELHO) # diz como vai ser a frase de fim de jogo
	perdeu = pygame.mixer.Sound("music/som_perdeu.wav")
	pygame.mixer.music.pause() # pausa a música de fundo que inicializou na linha 64
	perdeu.play() # executa a música de game over
	tela.blit(terminou, [180, 300]) #escreve a frase escolhida de fim de jogo na posição escolhida dentro da tela
	pygame.display.update() #atualiza a tela 
	pygame.time.wait(5000) #tempo para a saída depois do game over

pygame.init() #inicia o pygame
pygame.mixer.init() # inicia o módulo de reprodução de sons do pygame
tela = pygame.display.set_mode((600,600)) #tamanho que a tela de jogo irá ter
pygame.display.set_caption("Jogo da cobrinha") # coloca um nome no jogo que aparecerá na aba
fonte = pygame.font.SysFont(None,55) # variavel de uso de fontes 
fonte2 = pygame.font.SysFont(None, 25) #variavel de uso de fontes

#som de fundo do jogo
pygame.mixer.music.load("music/som_fundo.wav") # mixer é o módulo do pygame para musica, music pq é o que eu vou carregar e load para carregar, dentro do paranteses indico o caminho do arquivo de música
pygame.mixer.music.play(-1) # usamos o play para executar a música e  o -1 para indicar que a música é para ficar tocando sempre

pontos = 0 #pontuação inicial
placar = fonte2.render("Pontos: "+ str(pontos), True, AMARELO) # variavel que diz como será escrito o placar

fase = 0 # fase inicial
level = fonte2.render("Fase: " + str(fase), True, AZUL) # variavel que diz como será escrito a fase

global cobra
cobra = [(200,200),(210,200),(220,200)] # desenha a cobrinha inicial
cobra_tam = pygame.Surface((10,10)) # variável que diz o quanto a cobra ira crescer
cobra_tam.fill(BRANCO) # desenha a cobra e dá a cor inicial

alvo_posicao = local_grid() # local que a comidinha irá aparecer, a variável usa a função escrita na linha 26 que escolhe randomicamente o local
alvo = pygame.Surface((10,10)) # tamanho da comidinha, que também usa o tamanho da cobrinha!
alvo.fill(VERMELHO) # cor da comidinha

velocidade = pygame.time.Clock() # objeto que controla o tempo 
velocidade_cobra = 5 # velocidade inicial da cobrinha 

game_over = False # para iniciar o jogo ele precisa estar "valendo"

while not game_over: # enquanto o jogo estiver "valendo" todos os comandos abaixo serão executados
	velocidade.tick(velocidade_cobra) # a cobrinha precisa de uma velocidade inicial né! :)
	for evento in pygame.event.get(): # se acontecer o evento a seguir: 
		if evento.type == QUIT: # no caso esse evento é o evento de saída
			pygame.quit() # o pygame irá encerrar a execução e saíra do jogo

		if evento.type == KEYDOWN: # se a teclas seguintes forem pressionadas:
			if evento.key == K_UP and direcao != ABAIXO:  
				direcao = ACIMA # a cobrinha anda para cima (usamos o operador 'and' para que a cobrinha ande sempre para frente e não começe a ander de marcha ré por ai :)
			if evento.key == K_DOWN and direcao != ACIMA: # tecla para baixo e a direção não for para cima 
				direcao = ABAIXO # a cobrinha anda para baixo
			if evento.key == K_LEFT and direcao != DIREITA: # tecla para esquerda e a direção não for para direita 
				direcao = ESQUERDA # a cobrinha anda para a esquerda 
			if evento.key == K_RIGHT and direcao != ESQUERDA: # tecla para direira e a direção não for para esquerda 
				direcao = DIREITA # a cobrinha anda para a direita

# vamos definir a dinamica do jogo!! 
	if encontro(cobra[0], alvo_posicao): # se a cobrinha (cabeça da cobrinha) encontrar a comida  
		alvo_posicao = local_grid() # a comidinha vai pra outro lugar
		comida = pygame.mixer.Sound("music/som_alimento.wav") # busca e carrega o som da comidinha
		comida.play() #executa o som da comidinha
		mudar_cor()  # a cobrinha muda de cor
		cobra.append((0,0)) # a cobrinha cresce

		pontos = pontos + 10 # cada vez que a cobrinha se alimentar a pontuação aumenta! ebaaa! 
		placar = fonte2.render("Pontos: "+ str(pontos), True, BRANCO) # atualiza a pontuação no placar escrito na tela
		
		if pontos % 50 == 0: # cada vez que a pontuação for um multiplo sem resto (a divisão da pontuação for 0) de 50
			fase = fase + 1 # o jogo sobe de fase
			level = fonte2.render("Fase: " + str(fase), True, AZUL) # atualiza a fase escrita na tela
			velocidade_cobra = velocidade_cobra + 3 # aumenta a velocidade da cobrinha 
			velocidade.tick(velocidade_cobra) # conforme a fase muda a velocidade aumenta, afinal de contas tem que ir ficando mais dificil né!
		
# se a cobrinha "bater" nas bordas do jogo ele acaba 
	if cobra[0][0] >= 599 or cobra[0][1] >= 599 or cobra[0][0] < 0 or cobra[0][1] < 0: # aqui são definidos os limites dos quatro lados do jogo de acordo com os seus eixos 
		game_over = True # já era né, não tá valendo mais
		
# quando a cobrinha decidir que pode passar por dentro dela mesmo (antropofagismo? hahahaha)
	for i in range(1, len(cobra) - 1): # verifica cada pedacinho do corpo da cobrinha
		if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]: # se a cabeça da cobrinha encontrar alguma outra parte do corpo dela:
			game_over = True # acabou também né! 

	if game_over: # se nada deu certo:
		perdeu() # perdeu amiguxos e a função escrita na linha 43 é chamada pra jogar isso na sua cara 

# aqui são as informações que o pygame vai usar para saber onde é cada direção que ele vai usar, tem que ensinar pra ele hein!			
	for i in range(len(cobra) -1, 0, -1):  # para cada posição da cobrinha em seu comprimento ela vai receber uma nova, mas vamos começar do fim da cobrinha
		cobra[i] = (cobra[i-1][0], cobra[i-1][1]) # assim a nova posição é a anterior e assim por diante
		# lembre que a cobrinha está em movimento e é como se fossem seus passos, um após o outro, ocupando espaço a sua frente e desocupando espaços atrás

	if direcao == ACIMA: # se a cobrinha andar pra cima: 
		cobra[0] = (cobra[0][0], cobra[0][1] -10) # a cabeça da cobra recebe um novo parametro e passa a ocupar os os próximos 10 pixels (-10) no eixo y

	if direcao == ABAIXO: # se a cobrinha andar pra baixo: 
		cobra[0] = (cobra[0][0], cobra[0][1] +10) # a cabeça da cobra recebe um novo parametro e passa a ocupar os os próximos 10 pixels (+10) no eixo y

	if direcao == DIREITA:  # se a cobrinha andar para a direita: 
		cobra[0] = (cobra[0][0] +10, cobra[0][1]) # a cabeça da cobra recebe um novo parametro e passa a ocupar os os próximos 10 pixels (+10) no eixo x

	if direcao == ESQUERDA:  # se a cobrinha andar para a esquerda: 
		cobra[0] = (cobra[0][0] -10, cobra[0][1]) # a cabeça da cobra recebe um novo parametro e passa a ocupar os os próximos 10 pixels (+10) no eixo x

	tela.fill(PRETO) # a cor de fundo que a tela terá
	tela.blit(alvo, alvo_posicao) # desenha na tela a comidinha e o local aleatório 
	tela.blit(placar,[350,5]) # escreve as informações do placar
	tela.blit(level, [150,5]) # escreve as informações do nivel
	
	for posicao in cobra: # para cada posição dentro da tela que cobrinha ocupar: (lembre-se que a cobrinha está 'andando' na tela)
		tela.blit(cobra_tam, posicao) # a tela será atualizada

	pygame.display.update() # faz a atualização da tela 