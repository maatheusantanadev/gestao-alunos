import json # Importa o módulo json para manipulação de arquivos JSON
from Aluno import Alunos    # Importa a classe Alunos do módulo Aluno, para criar objetos que representam os alunos

# Função para carregar dados de alunos a partir de um arquivo JSON
def carregar_alunos(caminho_arquivo):
    with open(caminho_arquivo, encoding="utf-8") as f:
        dados = json.load(f)    # Lê o conteúdo do arquivo e converte de JSON para um objeto Python (lista/dicionário)
    return [Alunos(valor["primeiro_nome"], valor["ultimo_nome"], valor["nota_1"], valor["nota_2"], valor["nota_3"], valor["nota_4"], valor["faltas"]) for valor in dados]


