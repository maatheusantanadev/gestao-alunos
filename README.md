# Gestão de Alunos

---

## 📌 Sistema de Gestão de Alunos – Tkinter (Python)

Este projeto é um **sistema desktop** desenvolvido em **Python** com **Tkinter**, que permite gerenciar informações de alunos, como **média de notas** e **faltas**, oferecendo filtros para facilitar a visualização de aprovados e reprovados.

---

### ✨ **Funcionalidades**

* **Carregamento de dados** a partir de um arquivo JSON.
* **Exibição em tabela** (`ttk.Treeview`) com colunas:

  * Primeiro Nome
  * Último Nome
  * Média
  * Faltas
  * Motivo (reprovação)
* **Filtros personalizáveis**:

  * Filtro por nome.
  * Filtro por média mínima.
  * Filtro por número máximo de faltas.
* **Botões de atalho**:

  * Mostrar apenas **Aprovados**.
  * Mostrar apenas **Reprovados**.
* **Mensagens de erro** amigáveis para entradas inválidas.

---

### 🛠 **Tecnologias utilizadas**

* **Python 3**
* **Tkinter** (interface gráfica)
* **ttk** para tabelas e widgets estilizados
* **messagebox** para exibição de mensagens
* Arquivos **JSON** para armazenamento dos dados

---

### 📂 **Estrutura do Projeto**

```
📁 projeto/
│── 📄 main.py          # Arquivo principal do sistema
|── 📄 Aluno.py         # Classe Aluno estruturada (ex.: calcular_media)
│── 📄 Service.py       # Funções auxiliares (ex.: carregar_alunos)
│── 📄 alunos.json      # Base de dados dos alunos
│── 📄 README.md        # Documentação do projeto
```

---

### ▶ **Como executar**

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório:

   ```bash
   git clone https://github.com/maatheusantanadev/gestao-alunos.git
   ```
3. Abra o terminal na pasta do projeto e execute:

   ```bash
   python main.py
   ```

---

### 📌 **Possíveis melhorias**

* Adicionar funcionalidade para **editar** e **adicionar alunos**.
* Implementar **salvamento automático** após edição.
* Adicionar **exportação de dados** para CSV ou Excel.
* Melhorar a **interface** com Tkinter.ttk e temas visuais.

---
