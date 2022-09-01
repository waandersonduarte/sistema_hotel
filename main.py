from datetime import datetime
from banco_dados.bd_consumo import ConsumoBD
from banco_dados.bd_funcionario import FuncionarioBD
from banco_dados.bd_quarto import QuartoBD
from banco_dados.bd_servico import ServicoBD
from classes.consumo import Consumo
from classes.funcionario import Funcionario
from classes.hospede import Hospede
from banco_dados.bd_hospede import HospedeBD
from classes.quarto import Quarto
from classes.servico import Servico

def cadastrarHospede():
    nome = input("Digite o nome do Hospede: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone do Hospede: ")
    categoria = input("Informe a categoria do quarto (simples, duplo, casal e luxo): ")
    num_quarto = int(input("Informe o número do quarto: "))
    data_reserva = input("Digite a data da reserva: ")
    data_desocupa = input("Digite a data que irá desocupa o quarto: ")
    print('Deseja alocar mais um quarto? Se sim digite 1 caso contrário digite 0: ')
    
    hospede = Hospede(nome = nome, cpf = cpf, telefone = telefone, categoria= categoria, num_quarto= num_quarto, data_reserva= data_reserva, data_desocupa= data_desocupa)

    bd = HospedeBD()
    bd.cadastrar_hospede(hospede)

def listarHospede():
    bd = HospedeBD()
    resultado = bd.listar_hospede()
    print(resultado)

def alterarHospede():

    id = int(input('Digite o id do Hospede que deseja alterar: '))
    bd = HospedeBD()
    resultado = bd.alterar_hospede(id)
    print(resultado)
    nome = input("Digite o nome do Hospede: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone do Hospede: ")
    categoria = input("Informe a categoria do quarto (simples, duplo, casal e luxo): ")
    num_quarto = int(input("Informe o número do quarto: "))
    data_reserva = datetime(input("Digite a data da reserva: "))
    data_desocupa = datetime(input("Digite a data que irá desocupa o quarto: "))
    
    hospede = Hospede(nome = nome, cpf = cpf, telefone = telefone, categoria= categoria, num_quarto= num_quarto, data_reserva= data_reserva, data_desocupa= data_desocupa)

    bd = HospedeBD()
    bd.alterar_hospede(hospede)

def deletarHospede():
    id = int(input('Digite o id do Hospede para excluir: '))
    bd = HospedeBD()
    bd.deletar_hospede(id)

def buscarHospede():
    id = int(input("Digite o id do hospede buscado: "))
    bd = HospedeBD()
    busca = bd.buscar_hospede(id)
    print('Resultado da busca: ', busca)

##############################################################################################
def cadastrarQuarto():
    num_quarto = input("Informe o número do quarto: ")
    categoria_quarto = input("Informe a categoria do quarto (simples, duplo, casal e luxo): ")
    valor_diaria = float(input("Informe o valor da diária: "))
    
    quarto = Quarto(num_quarto = num_quarto, categoria_quarto = categoria_quarto, valor_diaria= valor_diaria)

    bd = QuartoBD()
    bd.cadastrar_quarto(quarto)

def listarQuarto():
    bd = QuartoBD()
    resultado = bd.listar_quarto()
    print(resultado)

def deletarQuarto():
    id = int(input('Digite o id do Quarto para excluir: '))
    bd = QuartoBD()
    bd.deletar_quarto(id)

def buscarQuarto():
    id = int(input("Digite o id do quarto buscado: "))
    bd = QuartoBD()
    busca = bd.buscar_quarto(id)
    print('Resultado da busca: ', busca)


##############################################################################################
def cadastrarFuncionario():
    nome = input("Digite o nome do Funcionário: ")
    cpf = input("Digite o CPF do Funcionário: ")
    telefone = input("Digite o telefone do Funcionário: ")
    matricula = input("Digite a matricula do Funcionário: ")
    
    funcionario = Funcionario(nome = nome, cpf = cpf, telefone = telefone, matricula= matricula)

    bd = FuncionarioBD()
    bd.cadastrar_funcionario(funcionario)

def listarFuncionario():
    bd = FuncionarioBD()
    resultado = bd.listar_funcionario()
    print(resultado)

def deletarFuncionario():
    id = int(input('Digite o id do Funcionario para excluir: '))
    bd = FuncionarioBD()
    bd.deletar_funcionario(id)

def buscarFuncionario():
    id = int(input("Digite o id do Funcionário buscado: "))
    bd = FuncionarioBD()
    busca = bd.buscar_funcionario(id)
    print('Resultado da busca: ', busca)

##############################################################################################
def cadastrarConsumoHospede():
    item_consumo = input("Digite o item de consumo do Hospede: ")
    qt_consumo = int(input("Digite a quantidade de item: "))
    valor_consumo = float(input("Digite o valor (R$): "))
    num_quarto = int(input("Digite o número do quarto: "))
    
    consumo = Consumo(item_consumo = item_consumo, qt_consumo = qt_consumo, valor_consumo = valor_consumo, num_quarto= num_quarto)

    bd = ConsumoBD()
    bd.cadastrar_consumo(consumo)

def listarConsumoHospede():
    bd = ConsumoBD()
    resultado = bd.listar_consumo()
    print(resultado)

##############################################################################################
def cadastrarServicoQuarto():
    print('Qual serviço de quarto deseja?\nPassar roupas\nLavanderia\nAmbos serviços\n')
    servico_quarto = input("Digite o servico desejado: ")
    num_quarto = int(input("Digite o número do quarto: "))

    servico = Servico(servico_quarto = servico_quarto, num_quarto= num_quarto)

    bd = ServicoBD()
    bd.cadastrar_servico(servico)


##############################################################################################
def main():

    sair = False

    while(sair == False):

        print("\tDigite\n| 1 - Cadastrar Hospede\n| 2 - Listar todos os Hospedes\n| 3 - Buscar um Hospede\n| 4 - Deletar Hospede\n| 5 - Alterar Hospede \n| 6 - Cadastrar Quarto\n| 7 - Listar Quarto\n| 8 - Deletar Quarto\n| 9 - Buscar Quarto\n| 10 - Cadastrar Funcionário\n| 11 - Listar Funcionário\n| 12 - Deletar Funcionário\n| 13 - Buscar Funcionário\n| 14 - Cadastrar Consumo do Hospede\n| 15 - Listar Consumo do Hospede\n| 16 - Registro Serviço de Quarto\n| 0 - Sair")
        opcao = int(input('Selecione a opção desejada: '))

        if(opcao == 1):
            cadastrarHospede()
        elif(opcao == 2):
             listarHospede()
        elif(opcao == 3):
             buscarHospede()
        elif(opcao == 4):
            deletarHospede()
        elif(opcao == 5):
            alterarHospede()
        elif(opcao == 6):
            cadastrarQuarto()
        elif(opcao == 7):
            listarQuarto()
        elif(opcao == 8):
            deletarQuarto()
        elif(opcao == 9):
            buscarQuarto()
        elif(opcao == 10):
            cadastrarFuncionario()
        elif(opcao == 11):
            listarFuncionario()
        elif(opcao == 12):
            deletarFuncionario()
        elif(opcao == 13):
            buscarFuncionario()
        elif(opcao == 14):
            cadastrarConsumoHospede()
        elif(opcao == 15):
            listarConsumoHospede()
        elif(opcao == 16):
            cadastrarServicoQuarto()
        elif(opcao == 0):
            sair = True
        else:
            print("opcao inválida!")

main()