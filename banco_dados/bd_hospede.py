import sqlite3

class HospedeBD():
    def __init__(self):
        self.conexao = sqlite3.connect('bd_hotel.db')
        self.cursor = self.conexao.cursor()

    def cadastrar_hospede(self, hospede):
        self.cursor.execute("INSERT OR IGNORE INTO hospede (nome, cpf, telefone, categoria, num_quarto, data_reserva, data_desocupa) VALUES ('"+str(hospede.mostra_nome())+"', '"+str(hospede.mostra_cpf())+"', '"+str(hospede.mostra_telefone())+"', '"+str(hospede.mostra_categoria())+"', '"+str(hospede.mostra_num_quarto())+"', '"+str(hospede.mostra_data_reserva())+"', '"+str(hospede.mostra_data_desocupa())+"')")
        self.conexao.commit()
    
    def listar_hospede(self):
        self.cursor.execute('SELECT * FROM hospede')
        for linha in self.cursor.fetchall():
            print(linha)

    def alterar_hospede(self, hospede, id):
        consulta = "UPDATE OR IGNORE hospede SET nome='"+str(hospede.altera_nome)+"', cpf='"+str(hospede.altera_cpf)+"', telefone='"+str(hospede.altera_telefone)+"', categoria='"+str(hospede.altera_categoria)+"', num_quarto='"+str(hospede.altera_num_quarto)+"',  data_reserva='"+str(hospede.altera_data_reserva)+"', cpf='"+str(hospede.altera_data_desocupa)+"' WHERE id="+str(id)
        self.cursor.execute(consulta, (hospede.nome, hospede.cpf, hospede.telefone, hospede.categoria, hospede.num_quarto, hospede.data_reserva, hospede.data_desocupa))
        self.conexao.commit()

    def deletar_hospede(self, id):
        self.cursor.execute('DELETE FROM hospede WHERE id = '+str(id))
        self.conexao.commit()
        print('Hóspede removido com sucesso!')

    def buscar_hospede(self, id):
        busca = self.cursor.execute('SELECT * FROM hospede WHERE id = '+str(id))
        return busca.fetchall()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()
    