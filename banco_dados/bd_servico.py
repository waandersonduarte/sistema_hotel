import sqlite3

class ServicoBD():
    def __init__(self):
        self.conexao = sqlite3.connect('bd_hotel.db')
        self.cursor = self.conexao.cursor()

    def cadastrar_servico(self, servico):
        self.cursor.execute("INSERT OR IGNORE INTO servico (servico_quarto, num_quarto) VALUES ('"+str(servico.mostra_servico_quarto())+"', '"+str(servico.mostra_num_quarto())+"')")
        self.conexao.commit()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()