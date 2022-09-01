import sqlite3
from classes.quarto import Quarto
class QuartoBD():
    def __init__(self):
        self.conexao = sqlite3.connect('bd_hotel.db')
        self.cursor = self.conexao.cursor()
        
    def cadastrar_quarto(self, hotel):
        self.cursor.execute("INSERT OR IGNORE INTO quarto (num_quarto, categoria_quarto, valor_diaria) VALUES ('"+str(hotel.mostra_num_quarto())+"', '"+str(hotel.mostra_categoria_quarto())+"', '"+str(hotel.mostra_valor_diaria())+"')")
        self.conexao.commit()

    def listar_quarto(self):
        self.cursor.execute('SELECT * FROM quarto')
        for linha in self.cursor.fetchall():
            print(linha)

    def deletar_quarto(self, id):
        self.cursor.execute('DELETE FROM quarto WHERE id = '+str(id))
        self.conexao.commit()
        print('Quarto removido com sucesso!')

    def buscar_quarto(self, id):
        busca = self.cursor.execute('SELECT * FROM quarto WHERE id = '+str(id))
        return busca.fetchall()



    def fechar(self):
        self.cursor.close()
        self.conexao.close()