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
                            c = int(input("Nova idade: "))
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
                            c = int(input("Nova idade: "))
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
    
    def ordenar_contatos(self, lista):
        print("Selecione uma opção: ")
        print("1. Ordenar por nome: ")
        print("2. Ordenar por idade: ")
        opcao = input("> ")
 
        if opcao == "1":
            for i in range(len(lista)):       
                menor = i
                for j in range(i, len(lista)):
                    if lista[j][0] < lista[menor][0]:
                        menor = j
                (lista[i], lista[menor]) = (lista[menor], lista[i])
            return lista
        elif opcao == "2":
            for i in range(len(lista)):       
                menor = i
                for j in range(i, len(lista)):
                    if lista[j][2] < lista[menor][2]:
                        menor = j
                (lista[i], lista[menor]) = (lista[menor], lista[i])
            return lista
    
    def ordenar(self):
        print(self.ordenar_contatos(self.agenda))
    
    def busca_binaria(self):
        print("Selecione uma opção: ")
        print("1. Buscar contato por nome: ")
        print("2. Buscar contato por idade: ")
        opcao = input("> ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            for i in range(len(self.agenda)):
                ini = i
                for j in range(i, len(self.agenda)-1):
                    fim = j - 1
                    meio = (ini + fim) - 1
                    print(meio)
                    #print(self.agenda[meio][0])
                    if self.agenda[meio][0] == nome:
                        print("Sucesso: %r encontrado" %nome)
                        return meio
                    elif self.agenda[meio][0] < nome:
                        ini = meio + 1
                    else:
                        fim = meio - 1
            print("Não encontrado")
            return -1
        elif opcao == "2":
            idade = int(input("Digite a idade: "))
            for i in range(len(self.agenda)):
                ini = i
                for j in range(i, len(self.agenda)-1):
                    fim = j - 1
                    meio = (ini + fim) - 1 
                    if self.agenda[meio][2] == idade:
                        print("Sucesso: %r encontrado" %idade)
                        return meio
                    elif self.agenda[meio][2] < idade:
                        ini = meio + 1
                    else:
                        fim = meio - 1
            print("Não encontrado")
            return -1

