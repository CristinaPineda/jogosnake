import pygame, random
from pygame.locals import *

def local_grid():
	x= random.randint(0, 590)
	y= random.randint(0, 590)
	return (x//10 * 10, y//10 * 10)

def encontro(x1, x2):
    return (x1[0] == x2[0]) and (x1[1] == x2[1])

ACIMA = 0
DIREITA = 1
ABAIXO = 2
ESQUERDA = 3

pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo da cobrinha")

cobra = [(200,200),(210,200),(220,200)]
cobra_tam = pygame.Surface((10,10))
cobra_tam.fill((255,255,255))

alvo_posicao = local_grid()
alvo = pygame.Surface((10,10))
alvo.fill((255,0,0))

direcao = ESQUERDA

velocidade = pygame.time.Clock()

while True:
	velocidade.tick(10)
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()

		if evento.type == KEYDOWN:
			if evento.key == K_UP:
				direcao = ACIMA
			if evento.key == K_DOWN:
				direcao = ABAIXO
			if evento.key == K_LEFT:
				direcao = ESQUERDA
			if evento.key == K_RIGHT:
				direcao = DIREITA

	if encontro(cobra[0], alvo_posicao):
		alvo_posicao = local_grid()
		cobra.append((0,0))

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

	tela.fill((0,0,0))
	tela.blit(alvo, alvo_posicao)

	for posicao in cobra:
		tela.blit(cobra_tam, posicao)

	pygame.display.update()