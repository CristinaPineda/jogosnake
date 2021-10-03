import pygame, random
from pygame.locals import *

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

def local_grid():
	x= random.randint(15,580)
	y= random.randint(25,580)
	return (x//10 * 10, y//10 * 10)

def encontro(x1, x2):
	return (x1[0] == x2[0]) and (x1[1] == x2[1])

def mudar_cor():
	cor1 = random.choice(CORES)
	cor2 = random.choice(CORES)
	cobra_tam.fill(cor1)
	alvo.fill(cor2)

def perdeu():
	frases = ["VOCÊ PERDEU!", "GAME OVER", "FIM DE JOGO"]
	frase = random.choice(frases)
	tela.fill((54,54,54))
	terminou = fonte.render(frase, True, VERMELHO)
	placar = fonte.render("Pontuação final: "+ str(pontos), True, VERDE)
	perdeu = pygame.mixer.Sound("music/som_perdeu.wav")
	pygame.mixer.music.pause()
	perdeu.play()
	tela.blit(terminou, [180, 300])
	tela.blit(placar, [130, 350])
	pygame.display.update() 
	pygame.time.wait(5000)

pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo da cobrinha")
fonte = pygame.font.SysFont(None,55)
fonte2 = pygame.font.SysFont(None, 25)

pygame.mixer.music.load("music/som_fundo.wav")
pygame.mixer.music.play(-1)

pontos = 0
placar = fonte2.render("Pontos: "+ str(pontos), True, AMARELO)

fase = 0
level = fonte2.render("Fase: " + str(fase), True, AZUL)

cobra = [(200,200),(210,200),(220,200)]
cobra_tam = pygame.Surface((10,10))
cobra_tam.fill(BRANCO)

alvo_posicao = local_grid()
alvo = pygame.Surface((10,10))
alvo.fill(VERMELHO)

velocidade = pygame.time.Clock()
velocidade_cobra = 5

game_over = False 

while not game_over:
	velocidade.tick(velocidade_cobra)
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()

		if evento.type == KEYDOWN:
			if evento.key == K_UP and direcao != ABAIXO:  
				direcao = ACIMA
			if evento.key == K_DOWN and direcao != ACIMA:
				direcao = ABAIXO 
			if evento.key == K_LEFT and direcao != DIREITA:
				direcao = ESQUERDA
			if evento.key == K_RIGHT and direcao != ESQUERDA:
				direcao = DIREITA

	if encontro(cobra[0], alvo_posicao): 
		alvo_posicao = local_grid()
		comida = pygame.mixer.Sound("music/som_alimento.wav")
		comida.play()
		mudar_cor()
		cobra.append((0,0))

		pontos = pontos + 10
		placar = fonte2.render("Pontos: "+ str(pontos), True, BRANCO)
		
		if pontos % 50 == 0:
			fase = fase + 1
			level = fonte2.render("Fase: " + str(fase), True, AZUL)
			velocidade_cobra = velocidade_cobra + 3
			velocidade.tick(velocidade_cobra)
		
	if cobra[0][0] >= 599 or cobra[0][1] >= 599 or cobra[0][0] < 0 or cobra[0][1] < 0:
		game_over = True
		
	for i in range(1, len(cobra) - 1):
		if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
			game_over = True

	if game_over:
		perdeu()
		
	for i in range(len(cobra) -1, 0, -1): 
		cobra[i] = (cobra[i-1][0], cobra[i-1][1]) 

	if direcao == ACIMA:
		cobra[0] = (cobra[0][0], cobra[0][1] -10) 

	if direcao == ABAIXO: 
		cobra[0] = (cobra[0][0], cobra[0][1] +10) 

	if direcao == DIREITA:
		cobra[0] = (cobra[0][0] +10, cobra[0][1])

	if direcao == ESQUERDA:
		cobra[0] = (cobra[0][0] -10, cobra[0][1])

	tela.fill(PRETO)
	tela.blit(alvo, alvo_posicao)
	tela.blit(placar,[350,5])
	tela.blit(level, [150,5])
	
	for posicao in cobra:
		tela.blit(cobra_tam, posicao)

	pygame.display.update()