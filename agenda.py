agenda = []

class Agenda:

    def inserir(self):
        nome = input("Insira um nome: ")
        email = input("Insira um e-mail: ")
        idade = int(input("Insira uma idade: "))
        telefone = input("Insira um telefone: ")

        lista = []
        lista.append(nome)
        lista.append(email)
        lista.append(idade)
        lista.append(telefone)

        agenda.append(lista)

    def editar(self):
        print("b")

    def excluir(self):
        print("Selecione uma opção: ")
        print("1. Excluir por nome: ")
        print("2. Excluir por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(agenda):
                for j in i:
                    if nome == j:
                        agenda.pop(posicao)
        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(agenda):
                for j in i:
                    if telefone == j:
                        agenda.pop(posicao)    

    def exibir(self):
        print(agenda)

    def buscar(self):
        print("e")

