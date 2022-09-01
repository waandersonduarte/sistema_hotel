import sqlite3
from classes.funcionario import Funcionario
class FuncionarioBD():
    def __init__(self):
        self.conexao = sqlite3.connect('bd_hotel.db')
        self.cursor = self.conexao.cursor()
        
    def cadastrar_funcionario(self, funcionario):
        self.cursor.execute("INSERT OR IGNORE INTO funcionario (nome, cpf, telefone, matricula) VALUES ('"+str(funcionario.mostra_nome())+"', '"+str(funcionario.mostra_cpf())+"', '"+str(funcionario.mostra_telefone())+"', '"+str(funcionario.mostra_matricula())+"')")
        self.conexao.commit()

    def listar_funcionario(self):
        self.cursor.execute('SELECT * FROM funcionario')
        for linha in self.cursor.fetchall():
            print(linha)

    def deletar_funcionario(self, id):
        self.cursor.execute('DELETE FROM funcionario WHERE id = '+str(id))
        self.conexao.commit()
        print('Funcionario removido com sucesso!')

    def buscar_funcionario(self, id):
        busca = self.cursor.execute('SELECT * FROM funcionario WHERE id = '+str(id))
        return busca.fetchall()

    def fechar(self):
        self.cursor.close()
        self.conexao.close()