import tkinter as tk    # Importa o módulo principal do Tkinter, usado para criar interfaces gráficas

# Importa o submódulo ttk (Themed Tk), que fornece widgets com visual mais moderno
# Também importa messagebox, usado para exibir caixas de diálogo (alertas, informações, erros, etc.)
from tkinter import ttk, messagebox

from Service import carregar_alunos # Importa a função do arquivo Service

class Sistema(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializa a janela principal herdando de Tk
        self.title("Sistema de Gestão de Alunos")   # Define o título da janela
        self.geometry("800x500")    # Define o tamanho da janela

        # Campo para filtrar alunos pelo nome
        label_nome = tk.Label(self, text="Nome:", fg="black")
        label_nome.pack(side=tk.TOP, padx=5, pady=0)
        self.filtro_nome = tk.Entry(self)
        self.filtro_nome.pack(side=tk.TOP, padx=5, pady=5)

        # Campo para filtrar alunos por média mínima
        label_media = tk.Label(self, text="Média mínima:", fg="black")
        label_media.pack(side=tk.TOP, padx=5, pady=0)
        self.filtro_media = tk.Entry(self)
        self.filtro_media.pack(side=tk.TOP, padx=5, pady=5)

        # Campo para filtrar alunos por faltas máximas
        label_faltas = tk.Label(self, text="Faltas máximas:", fg="black")
        label_faltas.pack(side=tk.TOP, padx=5, pady=0)
        self.filtro_faltas = tk.Entry(self)
        self.filtro_faltas.pack(side=tk.TOP, padx=5, pady=5)

        # Botões de ação para filtrar e exibir aprovados/reprovados
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(side=tk.TOP, pady=5)
        tk.Button(frame_botoes, text="Filtrar", command=self.executar_filtros, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Aprovados", command=lambda: self.carregar_tabela("aprovados"), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Reprovados", command=lambda: self.carregar_tabela("reprovados"), bg="#f44336", fg="white").pack(side=tk.LEFT, padx=5)

        # Tabela para exibir lista de alunos com colunas definidas
        colunas = ("Primeiro nome", "Ultimo nome", "Média", "Faltas", "Motivo")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")

        # Configuração dos cabeçalhos e largura das colunas da tabela
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=150, anchor=tk.CENTER)
        self.tabela.pack(fill=tk.BOTH, expand=True)


        self.alunos = carregar_alunos("alunos.json")    # Carrega a lista de alunos a partir de um arquivo JSON
        self.carregar_tabela()  # Exibe todos os alunos inicialmente


    # Carrega todos os alunos na tabela.
    # Se 'preset' for "aprovados", exibe apenas alunos com média >= 7 e faltas < 7.
    # Se 'preset' for "reprovados", exibe apenas alunos com média < 7 ou faltas >= 7.
    def carregar_tabela(self, preset=None):
        for i in self.tabela.get_children():
            self.tabela.delete(i)

        for aluno in self.alunos:
            media = aluno.calcular_media()
            motivo = ""

            if preset == "aprovados" and not (media >= 7.0 and aluno.faltas < 7):
                self.filtro_nome.delete(0, tk.END)
                self.filtro_media.delete(0, tk.END)
                self.filtro_faltas.delete(0, tk.END)
                continue
            if preset == "reprovados":
                self.filtro_nome.delete(0, tk.END)
                self.filtro_media.delete(0, tk.END)
                self.filtro_faltas.delete(0, tk.END)
                if media < 7.0 and aluno.faltas < 7:
                    motivo = "Média insuficiente!"
                elif aluno.faltas >= 7:
                    motivo = "Excesso de faltas!"

            self.tabela.insert("", tk.END, values=(aluno.primeiroNome, aluno.ultimoNome, round(media, 2), aluno.faltas, motivo))


    # Filtra alunos pelo nome digitado no campo de busca.
    # Aceita correspondência parcial tanto no primeiro quanto no último nome.
    def filtrarNome(self):
        nome_filtro = self.filtro_nome.get().lower().strip()

        if not nome_filtro:
            self.carregar_tabela()
            return

        for i in self.tabela.get_children():
            self.tabela.delete(i)

        for aluno in self.alunos:
            media = aluno.calcular_media()
            motivo = ""

            if nome_filtro in aluno.primeiroNome.lower():
                if media < 7 and aluno.faltas < 7:
                    motivo = "Média insuficiente!"
                elif aluno.faltas >= 7:
                    motivo = "Excesso de faltas!"
                self.tabela.insert("", tk.END, values=(aluno.primeiroNome, aluno.ultimoNome, round(aluno.calcular_media(), 2), aluno.faltas, motivo))
            elif nome_filtro in aluno.ultimoNome.lower():
                if media < 7 and aluno.faltas < 7:
                    motivo = "Média insuficiente!"
                elif aluno.faltas >= 7:
                    motivo = "Excesso de faltas!"
                self.tabela.insert("", tk.END, values=(aluno.primeiroNome, aluno.ultimoNome, round(aluno.calcular_media(), 2), aluno.faltas, motivo))


    # Filtra alunos pela média mínima digitada.
    # Mostra apenas alunos cuja média seja maior ou igual ao valor inserido.
    def filtrarMedia(self):
        media_filtro = self.filtro_media.get().strip()

        try:
            media_filtro = float(media_filtro) if media_filtro else None
        except ValueError:
            messagebox.showerror("Erro", "Média mínima inválida!")
            return

        self.tabela.delete(*self.tabela.get_children())

        for aluno in self.alunos:
            media = aluno.calcular_media()
            motivo = ""
            if media_filtro is None or media >= media_filtro:
                if media < 7 and aluno.faltas < 7:
                    motivo = "Média insuficiente!"
                elif aluno.faltas >= 7:
                    motivo = "Excesso de faltas!"
                self.tabela.insert("", tk.END, values=(aluno.primeiroNome, aluno.ultimoNome, round(media, 2), aluno.faltas, motivo))


    # Filtra alunos pelo número máximo de faltas digitado.
    # Mostra apenas alunos cuja quantidade de faltas seja menor ou igual ao valor inserido.
    def filtrarFaltas(self):
        faltas_filtro = self.filtro_faltas.get().strip()

        try:
            faltas_filtro = int(faltas_filtro) if faltas_filtro else None
        except ValueError:
            messagebox.showerror("Erro", "Falta mínima inválida!")
            return

        self.tabela.delete(*self.tabela.get_children())

        for aluno in self.alunos:
            media = aluno.calcular_media()
            motivo = ""
            if faltas_filtro is None or aluno.faltas <= faltas_filtro:
                if media < 7 and aluno.faltas < 7:
                    motivo = "Média insuficiente!"
                elif aluno.faltas >= 7:
                    motivo = "Excesso de faltas!"
                self.tabela.insert("", tk.END, values=(aluno.primeiroNome, aluno.ultimoNome, round(media, 2), aluno.faltas, motivo))


    # Executa apenas um filtro por vez, conforme o campo preenchido pelo usuário.
    # Se mais de um campo for preenchido, a prioridade de execução é:
    # Nome > Média > Faltas.
    def executar_filtros(self):
        if self.filtro_nome.get().strip():
            return self.filtrarNome()
        if self.filtro_media.get().strip():
            return self.filtrarMedia()
        if self.filtro_faltas.get().strip():
            return self.filtrarFaltas()


# Inicia a execução do sistema (janela principal) e mantém o loop da interface gráfica ativo.
# Caso ocorra qualquer erro durante a execução, exibe uma mensagem de erro na tela.
try:
    Sistema().mainloop()
except Exception as e:
    messagebox.showerror("Erro", str(e))
