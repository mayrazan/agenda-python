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
        print("Selecione uma opção: ")
        print("1. Editar contato por nome: ")
        print("2. Editar contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(agenda): 
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
                            agenda[posicao][0] = a
                            break
                        elif op == "2":
                            b = input("Novo e-mail: ")
                            agenda[posicao][1] = b  
                            break
                        elif op == "3":
                            c = input("Nova idade: ")
                            agenda[posicao][2] = c
                            break
                        elif op == "4":
                            d = input("Novo telefone: ")
                            agenda[posicao][3] = d
                            break

        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(agenda): 
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
                            agenda[posicao][0] = a
                            break
                        elif op == "2":
                            b = input("Novo e-mail: ")
                            agenda[posicao][1] = b  
                            break
                        elif op == "3":
                            c = input("Nova idade: ")
                            agenda[posicao][2] = c
                            break
                        elif op == "4":
                            d = input("Novo telefone: ")
                            agenda[posicao][3] = d
                            break

    def excluir(self):
        print("Selecione uma opção: ")
        print("1. Excluir contato por nome: ")
        print("2. Excluir contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(agenda):
                for j in i:
                    if nome == j:
                        agenda.pop(posicao)
                        break
        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(agenda):
                for j in i:
                    if telefone == j:
                        agenda.pop(posicao)  
                        break 

    def exibir(self):
        if len(agenda) == 0:
            print("Agenda vazia.")
        else:
            print(agenda)

    def buscar(self):
        print("Selecione uma opção: ")
        print("1. Buscar contato por nome: ")
        print("2. Buscar contato por telefone: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for posicao, i in enumerate(agenda): 
                for j in i:
                    if nome == j:
                        print(i)
                        break
        elif opcao == "2":
            telefone = input("Digite o telefone: ")
            for posicao, i in enumerate(agenda): 
                for j in i:
                    if telefone == j:
                        print(i)
                        break  

