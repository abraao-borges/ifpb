from collections import deque

# Configuração da memória física
NUM_QUADROS = 16  # Número total de quadros disponíveis
TAMANHO_PAGINA = 4  # KB (cada página tem 4 KB)
PROCESSO_TAMANHO = 16  # KB (cada processo ocupa 16 KB, ou seja, 4 páginas)

class GerenciadorMemoria:
    def __init__(self):
        self.memoria_fisica = [None] * NUM_QUADROS  # Inicializa memória com quadros vazios
        self.fila_fifo = deque()  # Fila para gerenciar substituição FIFO
        self.tabelas_paginas = {}  # Tabelas de páginas por processo

    def alocar_processo(self, pid):
        """Aloca um processo na memória usando paginação."""
        if pid in self.tabelas_paginas:
            print(f"Erro: Processo {pid} já está alocado.")
            return
        
        tabela_paginas = {}  # Tabela de páginas do processo
        for pagina in range(PROCESSO_TAMANHO // TAMANHO_PAGINA):
            if None in self.memoria_fisica:
                quadro = self.memoria_fisica.index(None)  # Encontra um quadro vazio
                self.memoria_fisica[quadro] = (pid, pagina)
                tabela_paginas[pagina] = quadro
            else:
                # Substituição de página FIFO
                pid_vitima, pagina_vitima = self.fila_fifo.popleft()
                quadro = next(i for i, v in enumerate(self.memoria_fisica) if v == (pid_vitima, pagina_vitima))
                print(f"Substituindo página {pagina_vitima} do processo {pid_vitima} pelo processo {pid}.")
                self.memoria_fisica[quadro] = (pid, pagina)
                tabela_paginas[pagina] = quadro
        
            self.fila_fifo.append((pid, pagina))  # Adiciona a página nova à fila

        self.tabelas_paginas[pid] = tabela_paginas
        print(f"Processo {pid} alocado.")

    def exibir_memoria(self):
        """Exibe o estado atual da memória física e das tabelas de páginas."""
        print("\nEstado da Memória Física:")
        for i, quadro in enumerate(self.memoria_fisica):
            if quadro:
                print(f"Quadro {i}: Processo {quadro[0]}, Página {quadro[1]}")
            else:
                print(f"Quadro {i}: [Vazio]")

        print("\nTabelas de Páginas:")
        for pid, tabela in self.tabelas_paginas.items():
            print(f"Processo {pid}: {tabela}")

# Simulação
gerenciador = GerenciadorMemoria()
gerenciador.alocar_processo(1)
gerenciador.alocar_processo(2)
gerenciador.alocar_processo(3)
gerenciador.alocar_processo(4)
gerenciador.alocar_processo(5)  # Este processo acionará a substituição FIFO
gerenciador.exibir_memoria()