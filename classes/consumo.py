class Consumo():
    def __init__(self, item_consumo, qt_consumo, valor_consumo, num_quarto):
        self.item_consumo = item_consumo
        self.qt_consumo = qt_consumo
        self.valor_consumo = valor_consumo
        self.num_quarto = num_quarto

    def mostra_item_consumo(self):
        return self.item_consumo
    
    def mostra_qt_consumo(self):
        return self.qt_consumo

    def mostra_valor_consumo(self):
        return self.valor_consumo

    def mostra_num_quarto(self):
        return self.num_quarto
