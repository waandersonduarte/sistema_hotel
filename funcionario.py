from hospede import Hospede


class Funcionario(Hospede):
    def __init__(self, nome, cpf, telefone, matricula):
        super().__init__(nome, cpf, telefone)
        self.matricula = matricula