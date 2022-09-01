class Quarto():
    def __init__(self, num_quarto, categoria_quarto, valor_diaria):
        self.num_quarto = num_quarto
        self.categoria_quarto = categoria_quarto
        self.valor_diaria = valor_diaria

    def mostra_num_quarto(self):
        return self.num_quarto

    def altera_num_quarto(self, novo_num_quarto):
        self.qt_quarto = novo_num_quarto

    def mostra_categoria_quarto(self):
        return self.categoria_quarto

    def altera_categoria_quarto(self, nova_categoria_quarto):
        self.categoria_quarto = nova_categoria_quarto

    def mostra_valor_diaria(self):
        return self.valor_diaria

    def altera_valor_diaria(self, novo_valor_diaria):
        self.valor_diaria = novo_valor_diaria


    