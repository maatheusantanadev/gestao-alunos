class Alunos:
    # Inicializa os atributos do aluno
    def __init__(self, primeiroNome, ultimoNome, nota_1, nota_2, nota_3, nota_4, faltas):
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
        self.notas = (nota_1 or 0, nota_2 or 0, nota_3 or 0, nota_4 or 0)   # Armazena as notas em uma só variavél e se alguma for None ou vazia, substitui por 0
        self.faltas = faltas

    #Calcula a média aritmética das notas do aluno
    # Retorna 0 se não houver notas.
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
