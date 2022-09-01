class Funcionario():
    def __init__(self, nome, cpf, telefone, matricula):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.matricula = matricula

    def mostra_nome(self):
        return self.nome

    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def mostra_cpf(self):
        return self.cpf

    def altera_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def mostra_telefone(self):
        return self.telefone

    def altera_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def mostra_matricula(self):
        return self.matricula

    def altera_matricula(self, nova_matricula):
        self.matricula = nova_matricula