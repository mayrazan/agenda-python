class Agenda:
    def __init__(self):
        self.agenda = []
        self.fila = []

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

        self.agenda.append(lista)

    def editar(self):
        print("Selecione uma opção: ")
        print("1. Editar contato por nome: ")
        print("2. Editar contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(self.agenda): 
                for j in i:
                    if nome == j:
                        print("Selecione a opção que você quer editar: ")
                        print("1. Editar nome: ")
                        print("2. Editar e-mail: ")
                        print("3. Editar idade: ")
                        print("4. Editar telefone: ")
                        op = input("> ")

                        if op == "1":
                            a = input("Novo nome: ")
                            self.agenda[posicao][0] = a
                            break
                        elif op == "2":
                            b = input("Novo e-mail: ")
                            self.agenda[posicao][1] = b  
                            break
                        elif op == "3":
                            c = input("Nova idade: ")
                            self.agenda[posicao][2] = c
                            break
                        elif op == "4":
                            d = input("Novo telefone: ")
                            self.agenda[posicao][3] = d
                            break

        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(self.agenda): 
                for j in i:
                    if telefone == j:
                        print("Selecione a opção que você quer editar: ")
                        print("1. Editar nome: ")
                        print("2. Editar e-mail: ")
                        print("3. Editar idade: ")
                        print("4. Editar telefone: ")
                        op = input("> ")

                        if op == "1":
                            a = input("Novo nome: ")
                            self.agenda[posicao][0] = a
                            break
                        elif op == "2":
                            b = input("Novo e-mail: ")
                            self.agenda[posicao][1] = b  
                            break
                        elif op == "3":
                            c = input("Nova idade: ")
                            self.agenda[posicao][2] = c
                            break
                        elif op == "4":
                            d = input("Novo telefone: ")
                            self.agenda[posicao][3] = d
                            break

    def excluir(self):
        print("Selecione uma opção: ")
        print("1. Excluir contato por nome: ")
        print("2. Excluir contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(self.agenda):
                for j in i:
                    if nome == j:
                        self.agenda.pop(posicao)
                        break
        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(self.agenda):
                for j in i:
                    if telefone == j:
                        self.agenda.pop(posicao)  
                        break 

    def exibir(self):
        if len(self.agenda) == 0:
            print("Agenda vazia.")
        else:
            print(self.agenda)

    def buscar(self):
        print("Selecione uma opção: ")
        print("1. Buscar contato por nome: ")
        print("2. Buscar contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(self.agenda): 
                for j in i:
                    if nome == j:
                        print(i)
                        self.contatos_acessados(i)
                        break
        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(self.agenda): 
                for j in i:
                    if telefone == j:
                        print(i)
                        self.contatos_acessados(i)
                        break  

    def contatos_acessados(self, contato):
        if len(self.fila) < 5:
            self.fila.append(contato)
        else:
            self.fila.pop(0)
            self.fila.append(contato)

    def ultimos_acessados(self):
        if len(self.fila) == 0:
            print("Nenhum contato buscado.")
        else:
            print(self.fila)