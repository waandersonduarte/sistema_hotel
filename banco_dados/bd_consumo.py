import sqlite3
class ConsumoBD():
    def __init__(self):
        self.conexao = sqlite3.connect('bd_hotel.db')
        self.cursor = self.conexao.cursor()

    def cadastrar_consumo(self, consumo):
        self.cursor.execute("INSERT OR IGNORE INTO consumo (item_consumo, qt_consumo, valor_consumo, num_quarto) VALUES ('"+str(consumo.mostra_item_consumo())+"', '"+str(consumo.mostra_qt_consumo())+"', '"+str(consumo.mostra_valor_consumo())+"', '"+str(consumo.mostra_num_quarto())+"')")
        self.conexao.commit()

    def listar_consumo(self):
        self.cursor.execute('SELECT * FROM consumo')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conexao.close()