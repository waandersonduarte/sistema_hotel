class Hospede():
    def __init__(self, nome, cpf, telefone, categoria, num_quarto, data_reserva, data_desocupa):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.categoria = categoria
        self.num_quarto = num_quarto
        self.data_reserva = data_reserva
        self.data_desocupa = data_desocupa

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

    def mostra_categoria(self):
        return self.categoria

    def altera_categoria(self, nova_categoria):
        self.categoria = nova_categoria

    def mostra_num_quarto(self):
        return self.num_quarto

    def altera_num_quarto(self, novo_num_quarto):
        self.num_quarto = novo_num_quarto

    def mostra_data_reserva(self):
        return self.data_reserva

    def altera_data_reserva(self, nova_data_reserva):
        self.data_reserva = nova_data_reserva

    def mostra_data_desocupa(self):
        return self.data_desocupa

    def altera_data_desocupa(self, nova_data_desocupa):
        self.data_desocupa = nova_data_desocupa