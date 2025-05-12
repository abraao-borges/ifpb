import pygame
import sys
import queue

# Configurações iniciais da janela e da grade
LARGURA, ALTURA = 800, 850
LINHAS, COLUNAS = 20, 20
TAMANHO_CELULA = LARGURA // COLUNAS

# Cores usadas
BRANCO = (245, 245, 245)
CINZA = (220, 220, 220)
AZUL = (100, 149, 237)
VERDE = (144, 238, 144)
PRETO = (30, 30, 30)
COR_EXPLORADO = (200, 230, 255)
FUNDO_INFO = (240, 240, 255)
COR_BOTAO = (180, 180, 255)
COR_HOVER = (160, 160, 240)
COR_TEXTO = (40, 40, 60)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulação do Robô de Limpeza")
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 18)

def iniciar_simulacao():
    return {
        "grade": [['vazio' for _ in range(COLUNAS)] for _ in range(LINHAS)],  # Matriz de strings representando o chão
        "inicio": (0, 0),  # Posição inicial do robô
        "pos_robo": (0, 0),
        "limpo": set(),  # Células que foram limpas
        "explorado": set(),  # Células que já foram exploradas
        "alvos_robo": [],  # Lista com os próximos alvos do robô
        "caminho_robo": [],  # Caminho atual planejado
        "modo_robo": "explorar",
        "mapa_conhecido": set(),
        "indice_alvo": 0,
        "desenhando": True,
        "passos": 0
    }

sim = iniciar_simulacao()

def desenhar_grade():
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Cada célula é um retângulo da matriz (linha, coluna)
            retangulo = pygame.Rect(coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pos = (linha, coluna)
            cor = BRANCO
            if sim["grade"][linha][coluna] == 'parede':  # Acesso à matriz de grade
                cor = PRETO
            elif pos in sim["limpo"]:
                cor = VERDE
            elif pos in sim["explorado"]:
                cor = COR_EXPLORADO
            pygame.draw.rect(tela, cor, retangulo, border_radius=4)
            pygame.draw.rect(tela, CINZA, retangulo, 1, border_radius=4)

def desenhar_robo(pos):
    x = pos[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2
    y = pos[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2
    pygame.draw.circle(tela, AZUL, (x, y), TAMANHO_CELULA // 3)

def desenhar_informacoes():
    fundo_info = pygame.Rect(0, ALTURA - 150, LARGURA, 150)
    pygame.draw.rect(tela, FUNDO_INFO, fundo_info)

    estatisticas = [
        f"Modo: {'Exploração' if sim['modo_robo'] == 'explorar' else 'Limpeza'}",
        f"Explorados: {len(sim['explorado'])}",
        f"Limpos: {len(sim['limpo'])}",
        f"Acessíveis: {len(sim['mapa_conhecido']) if sim['mapa_conhecido'] else 'Desconhecido'}",
        f"Passos dados: {sim['passos']}"
    ]

    for i, texto in enumerate(estatisticas):
        render = fonte.render(texto, True, COR_TEXTO)
        tela.blit(render, (10, ALTURA - 140 + i * 25))

def desenhar_botao(texto, retangulo, mouse):
    cor = COR_HOVER if retangulo.collidepoint(mouse) else COR_BOTAO
    pygame.draw.rect(tela, cor, retangulo, border_radius=6)
    pygame.draw.rect(tela, CINZA, retangulo, 2, border_radius=6)
    label = fonte.render(texto, True, COR_TEXTO)
    label_ret = label.get_rect(center=retangulo.center)
    tela.blit(label, label_ret)

def ordem_limpeza_bfs(inicio):
    fila = queue.Queue()
    fila.put(inicio)
    visitado = set()
    visitado.add(inicio)
    ordem = []

    while not fila.empty():
        atual = fila.get()
        ordem.append(atual)
        for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            nova_linha, nova_coluna = atual[0] + d[0], atual[1] + d[1]
            if 0 <= nova_linha < LINHAS and 0 <= nova_coluna < COLUNAS:
                if sim["grade"][nova_linha][nova_coluna] != 'parede' and (nova_linha, nova_coluna) not in visitado:
                    fila.put((nova_linha, nova_coluna))
                    visitado.add((nova_linha, nova_coluna))
    return ordem

def encontrar_caminho(inicio, objetivo):
    fila = queue.Queue()
    fila.put((inicio, [inicio]))
    visitado = set()
    visitado.add(inicio)

    while not fila.empty():
        atual, caminho = fila.get()
        if atual == objetivo:
            return caminho[1:]  # Retorna o caminho sem incluir a posição atual

        for d in [(0,1), (1,0), (-1,0), (0,-1)]:
            nova_linha, nova_coluna = atual[0] + d[0], atual[1] + d[1]
            vizinho = (nova_linha, nova_coluna)
            if 0 <= nova_linha < LINHAS and 0 <= nova_coluna < COLUNAS:
                if sim["grade"][nova_linha][nova_coluna] != 'parede' and vizinho not in visitado:
                    fila.put((vizinho, caminho + [vizinho]))
                    visitado.add(vizinho)
    return []

def planejar_caminho_otimo(inicio, alvos):
    caminho = []
    visitado = set()
    atual = inicio
    a_visitar = list(alvos)

    while a_visitar:
        # Ordena os alvos pela distância de Manhattan (caminho mais curto ignorando paredes)
        a_visitar.sort(key=lambda pos: abs(pos[0] - atual[0]) + abs(pos[1] - atual[1]))
        proximo = a_visitar.pop(0)
        if proximo not in visitado:
            caminho.append(proximo)
            visitado.add(proximo)
            atual = proximo
    return caminho

def atualizar_robo():
    if sim["modo_robo"] == "explorar":
        if not sim["caminho_robo"]:
            if sim["indice_alvo"] == 0:
                sim["alvos_robo"] = ordem_limpeza_bfs(sim["inicio"])
            sim["indice_alvo"] += 1
            if sim["indice_alvo"] < len(sim["alvos_robo"]):
                sim["caminho_robo"] = encontrar_caminho(sim["pos_robo"], sim["alvos_robo"][sim["indice_alvo"]])
            else:
                sim["modo_robo"] = "limpar"
                sim["alvos_robo"] = planejar_caminho_otimo(sim["pos_robo"], sim["mapa_conhecido"])
                sim["indice_alvo"] = 0
                if sim["alvos_robo"]:
                    sim["caminho_robo"] = encontrar_caminho(sim["pos_robo"], sim["alvos_robo"][sim["indice_alvo"]])
        if sim["caminho_robo"]:
            proximo = sim["caminho_robo"].pop(0)
            sim["pos_robo"] = proximo
            sim["mapa_conhecido"].add(sim["pos_robo"])
            sim["explorado"].add(sim["pos_robo"])
            sim["passos"] += 1

    elif sim["modo_robo"] == "limpar":
        if not sim["caminho_robo"]:
            sim["indice_alvo"] += 1
            if sim["indice_alvo"] < len(sim["alvos_robo"]):
                sim["caminho_robo"] = encontrar_caminho(sim["pos_robo"], sim["alvos_robo"][sim["indice_alvo"]])
            else:
                sim["alvos_robo"] = []
        if sim["caminho_robo"]:
            proximo = sim["caminho_robo"].pop(0)
            sim["pos_robo"] = proximo
            sim["limpo"].add(sim["pos_robo"])
            sim["passos"] += 1

def principal():
    global sim
    rodando = True
    botao_resetar = pygame.Rect(LARGURA - 120, ALTURA - 60, 100, 35)

    while rodando:
        tela.fill(BRANCO)
        desenhar_grade()
        desenhar_robo(sim["pos_robo"])
        desenhar_informacoes()
        desenhar_botao("Resetar", botao_resetar, pygame.mouse.get_pos())
        pygame.display.flip()
        relogio.tick(10)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_resetar.collidepoint((mouse_x, mouse_y)):
                    sim = iniciar_simulacao()

            if sim["desenhando"]:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    linha, coluna = y // TAMANHO_CELULA, x // TAMANHO_CELULA
                    if linha < LINHAS and (linha, coluna) != sim["inicio"]:
                        sim["grade"][linha][coluna] = 'parede'
                if pygame.mouse.get_pressed()[2]:
                    x, y = pygame.mouse.get_pos()
                    linha, coluna = y // TAMANHO_CELULA, x // TAMANHO_CELULA
                    if linha < LINHAS and sim["grade"][linha][coluna] != 'parede':
                        sim["inicio"] = (linha, coluna)
                        sim["pos_robo"] = sim["inicio"]
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        sim["desenhando"] = False 
                        sim["alvos_robo"] = ordem_limpeza_bfs(sim["inicio"])
                        sim["indice_alvo"] = 0
                        if sim["alvos_robo"]:
                            sim["caminho_robo"] = encontrar_caminho(sim["pos_robo"], sim["alvos_robo"][sim["indice_alvo"]])
                    if evento.key == pygame.K_r:
                        sim = iniciar_simulacao()

        if not sim["desenhando"]:
            atualizar_robo()

principal()
