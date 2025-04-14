### **1 - O que é uma Thread e como ela difere de um Processo?**
- **Thread:** É a menor unidade de execução dentro de um processo. Uma thread compartilha o mesmo espaço de memória e recursos do processo ao qual pertence.
- **Processo:** É uma instância de um programa em execução que possui seu próprio espaço de memória e recursos.

🔹 **Principais diferenças:**  
| Característica  | Processo | Thread |
|----------------|---------|--------|
| Espaço de memória | Independente | Compartilhado dentro do processo |
| Comunicação entre eles | Difícil e lenta (IPC - Inter Process Communication) | Fácil e rápida |
| Tempo de criação | Maior (precisa alocar memória) | Menor (aproveita o espaço do processo) |
| Isolamento | Maior segurança | Pode afetar outras threads do mesmo processo |

---

### **2 - Principais Vantagens do Uso de Threads**
✅ **Eficiência:** Como as threads compartilham memória, não há necessidade de troca de contexto pesada como nos processos.  
✅ **Paralelismo:** Permite a execução simultânea de múltiplas tarefas.  
✅ **Menos uso de recursos:** Criar e gerenciar threads consome menos recursos do que criar processos.  
✅ **Melhor uso de CPU:** Threads podem aproveitar múltiplos núcleos do processador para rodar tarefas simultaneamente.

---

### **3 - Tipos de Threads**
- **Threads de Usuário:** Gerenciadas pelo próprio programa, sem intervenção direta do sistema operacional.
- **Threads de Kernel:** Gerenciadas pelo sistema operacional, proporcionando mais controle, mas com maior custo de desempenho.

---