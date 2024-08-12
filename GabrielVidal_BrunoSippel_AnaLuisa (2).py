import pygame as pg
import random
import time 

# Cores do jogo
branco = (255, 255, 255)
preto = (0, 0, 0)

# Setup da tela do Jogo
window = pg.display.set_mode((1000, 600))
pg.display.set_caption('Jogo da forca')

# Inicializando fonte
pg.font.init()
# Escolhendo uma fonte e tamanho
fonte = pg.font.SysFont("arial", 45)
fonte_rb = pg.font.SysFont("arial", 35)

lista = ['LIMAO','ABACAXI','JABUTICABA','UVA','MELANCIA','ABACATE','MORANGO','PERA','BANANA','MANGA','MARACUJA','JACA']

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
jogo_terminado = False
letra = ' '
click_last_status = False
# Função para desenhar texto

def Texto_Voce_Perdeu(window, texto, pos_x, pos_y, cor):
    texto_surface = fonte.render(texto, True, cor)
    window.blit(texto_surface, (pos_x, pos_y))

def Texto_Voce_Ganhou(window, texto, pos_x, pos_y, cor):
    texto_surface = fonte.render(texto, True, cor)
    window.blit(texto_surface, (pos_x, pos_y))
    


def Desenho_da_Forca(window, chance):
    # Desenho da Forca
    pg.draw.rect(window, branco, (0, 0, 1000, 600)) 
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)   
    #pg.draw.line(janela que é desenhado, cor, (x do ponto inicial, y do ponto que a linha começa), (x do ponto final, y do ponto final), largura em pixeis da line) se line for substituido pro circle no pg.drawn.CIRCLE ele desenha um circulo e não uma linha.
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    if chance >= 1:
        # Cabeça
        pg.draw.circle(window, preto, (300, 200), 50, 10)
    if chance >= 2:
        # Tronco
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
    if chance >= 3:
        # Braço Direito
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
    if chance >= 4:
        # Braço Esquerdo
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
    if chance >= 5:
        # Perna Direita
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
    if chance >= 6:
        # Perna Direita
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)

    if chance >= 7:
        # Outra pessoinha
        pg.draw.circle(window, preto, (700, 200), 50, 10)
        pg.draw.line(window, preto, (700, 250), (700, 350), 10)
        pg.draw.line(window, preto, (700, 260), (625, 350), 10)
        pg.draw.line(window, preto, (700, 260), (775, 350), 10)
        pg.draw.line(window, preto, (700, 350), (775, 450), 10)
        pg.draw.line(window, preto, (700, 350), (775, 450), 10)
        pg.draw.line(window, preto, (700, 350), (625, 450), 10)
        #pedra
        pg.draw.circle(window, preto, (625, 350), 20, 10)

    if chance >= 8:
    # Limpando a tela
        window.fill(branco)


 # Desenho da Forca
        pg.draw.rect(window, branco, (0, 0, 1000, 600)) 
        pg.draw.line(window, preto, (100, 500), (100, 100), 10)
        pg.draw.line(window, preto, (50, 500), (150, 500), 10)   
        pg.draw.line(window, preto, (100, 100), (300, 100), 10)
        pg.draw.line(window, preto, (300, 100), (300, 150), 10)
        # Primeiro boneco
        pg.draw.circle(window, preto, (300, 200), 50, 10)
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)

    # Tronco
        pg.draw.line(window, preto, (700, 250), (700, 350), 10)
    # Cabeça
        pg.draw.circle(window, preto, (700, 200), 50, 10)
    # Braço direito
        pg.draw.line(window, preto, (700, 260), (800, 200), 10)
    # Braço esquerdo com pedra
        pg.draw.line(window, preto, (700, 260), (600, 200), 10)
    # Pedra na mão esquerda
        pg.draw.circle(window, preto, (580, 200), 15, 10)
    # Perna direita
        pg.draw.line(window, preto, (700, 350), (750, 450), 10)
    # Perna esquerda
        pg.draw.line(window, preto, (700, 350), (650, 450), 10)


    if chance >= 9:
        pg.draw.rect(window, branco, (0, 0, 1000, 600)) #Pinta de branco]

# Desenho da Forca
        pg.draw.line(window, preto, (100, 500), (100, 100), 10)
        pg.draw.line(window, preto, (50, 500), (150, 500), 10)   
        pg.draw.line(window, preto, (100, 100), (300, 100), 10)
        pg.draw.line(window, preto, (300, 100), (300, 150), 10)

# Primeiro boneco
        pg.draw.circle(window, preto, (300, 200), 50, 10)
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)

# atirador de pedra
    # Tronco
        pg.draw.line(window, preto, (700, 250), (700, 350), 10)
    # Cabeça
        pg.draw.circle(window, preto, (700, 200), 50, 10)
    # Braço direito
        pg.draw.line(window, preto, (700, 260), (800, 300), 10)
    # Braço esquerdo com pedra
        pg.draw.line(window, preto, (700, 260), (600, 300), 10)
    # Pedra no ar
        pg.draw.circle(window, preto, (480, 200), 15, 10)
    # Perna direita
        pg.draw.line(window, preto, (700, 350), (750, 450), 10)
    # Perna esquerda
        pg.draw.line(window, preto, (700, 350), (650, 450), 10)



    if chance >= 10:
        pg.draw.rect(window, branco, (0, 0, 1000, 600)) #Pinta de branco]
        global jogo_terminado
        jogo_terminado = True
# Desenho da Forca
        pg.draw.line(window, preto, (100, 500), (100, 100), 10)
        pg.draw.line(window, preto, (50, 500), (150, 500), 10)   
        pg.draw.line(window, preto, (100, 100), (300, 100), 10)
        pg.draw.line(window, preto, (300, 100), (300, 150), 10)

# Primeiro boneco
        pg.draw.circle(window, preto, (300, 200), 50, 10)
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)

# atirador de pedra
    # Tronco
        pg.draw.line(window, preto, (700, 250), (700, 350), 10)
    # Cabeça
        pg.draw.circle(window, preto, (700, 200), 50, 10)
    # Braço direito
        pg.draw.line(window, preto, (700, 260), (800, 300), 10)
    # Braço esquerdo com pedra
        pg.draw.line(window, preto, (700, 260), (600, 300), 10)
    # Pedra
        pg.draw.circle(window, preto, (350, 200), 15, 10)
    # Perna direita
        pg.draw.line(window, preto, (700, 350), (750, 450), 10)
    # Perna esquerda
        pg.draw.line(window, preto, (700, 350), (650, 450), 10)
        Texto_Voce_Perdeu(window, "Você perdeu", 400, 300, preto)



      

def Desenho_Reiniciar_Button(window):
    pg.draw.rect(window, preto, (700, 100, 200, 65))
    texto = fonte_rb.render('reiniciar', 1, branco)
    window.blit(texto, (740, 120))

def Sorteando_Palavra(lista, palavra_escolhida, end_game):
    if end_game == True:
        palavra_n = random.randint(0, len(lista) - 1)
        palavra_escolhida = lista[palavra_n]
        end_game = False
        chance = 0
    return palavra_escolhida, end_game

def Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '#')
    return palavra_camuflada

def Verificar_Vitoria(window, palavra_camuflada):
    global jogo_terminado
    if '#' not in palavra_camuflada:
        Texto_Voce_Ganhou(window, "Você ganhou", 400, 300, preto)
        jogo_terminado = True
        return True
    return False



def Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras and jogo_terminado == False:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance

def Palavra_do_Jogo(window, palavra_camuflada):
    palavra = fonte.render(palavra_camuflada, 1, preto)
    window.blit(palavra, (200, 500))

def Reiniciar_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '#':
            count += 1
    if click_last_status == False and click[0] == True:
        print('Ok')
        if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas_de_letras = [' ', '-']
            end_game = True
            chance = 0
            letra = ' '
    return end_game, chance, tentativas_de_letras, letra
#LOOP principal do game/jogouuu
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper()

    # Declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declarando variavel do click do mouse
    click = pg.mouse.get_pressed()

       # Jogo
    Desenho_da_Forca(window, chance)
    Desenho_Reiniciar_Button(window)
    palavra_escolhida, end_game = Sorteando_Palavra(lista, palavra_escolhida, end_game)
    palavra_camuflada = Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance = Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance)
    Palavra_do_Jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = Reiniciar_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_position_x, mouse_position_y)

    # Verificar vitória
    if Verificar_Vitoria(window, palavra_camuflada):
        Texto_Voce_Ganhou(window, "Você ganhou", 400, 300, preto)
        

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()