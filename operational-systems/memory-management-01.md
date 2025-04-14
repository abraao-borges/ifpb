Aqui estão as respostas para as questões teóricas e um esboço da implementação da parte prática:

---

### **1. Diferença entre Alocação Contígua e Não Contígua**
- **Alocação Contígua:** A memória de um processo é armazenada em blocos contíguos na RAM. Isso pode levar a fragmentação externa e dificulta a expansão do processo.
- **Alocação Não Contígua:** A memória de um processo pode estar espalhada em diferentes partes da RAM, permitindo melhor aproveitamento e uso de técnicas como **paginação** e **segmentação**.

---

### **2. Tipos de Fragmentação e Impacto no Desempenho**
- **Fragmentação Externa:** Ocorre quando há pequenos blocos de memória livres espalhados, mas nenhum é grande o suficiente para alocar um novo processo.
- **Fragmentação Interna:** Ocorre quando a memória alocada para um processo é maior do que o necessário, desperdiçando espaço dentro do próprio bloco.

A fragmentação pode reduzir a eficiência da memória, aumentando a necessidade de técnicas como **compaction** (realocação dos processos na RAM).

---

### **3. Comparação entre Paginação e Segmentação**
| Característica   | Paginação  | Segmentação |
|-----------------|-----------|-------------|
| **Divisão da Memória** | Dividida em páginas de tamanho fixo | Dividida em segmentos de tamanhos variáveis |
| **Fragmentação** | Interna (devido ao tamanho fixo das páginas) | Externa (devido ao tamanho variável dos segmentos) |
| **Mapeamento** | Tabela de páginas | Tabela de segmentos |
| **Uso** | Facilita a gestão da memória, evitando fragmentação externa | Permite alocar memória de forma mais lógica e eficiente para processos |

---

### **4. Função da Tabela de Páginas**
A **tabela de páginas** é usada para mapear **endereços lógicos** em **endereços físicos**. Ela mantém informações sobre quais páginas lógicas correspondem a quais quadros da memória RAM, possibilitando acesso eficiente e evitando que processos acessem áreas de memória que não lhes pertencem.

---

### **5. Vantagens da Segmentação sobre a Paginação**
- **Organização lógica:** A segmentação permite dividir a memória de um programa em segmentos lógicos (código, pilha, dados), melhorando a organização.
- **Maior flexibilidade:** Como os segmentos têm tamanhos variáveis, a memória pode ser alocada de forma mais eficiente para diferentes necessidades do programa.
