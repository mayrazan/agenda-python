from agenda import Agenda
import sys

class Menu:

    def menu(self):
        print("Selecione uma opção: ")
        print("1. Inserir contato: ")
        print("2. Editar contato: ")
        print("3. Excluir contato: ")
        print("4. Exibir contatos: ")
        print("5. Buscar contato: ")
        print("6. Acessados recentemente: ")
        print("7. Ordenar contatos: ")
        print("8. Busca binária: ")
        print("0. Sair. ")
        opcao = input("> ")

        while opcao == "1":
            a.inserir()
            self.menu()
        while opcao == "2":
            a.editar()
            self.menu()
        while opcao == "3":
            a.excluir()
            self.menu()
        while opcao == "4":
            a.exibir()
            self.menu()
        while opcao == "5":
            a.buscar()
            self.menu()
        while opcao == "6":
            a.ultimos_acessados()
            self.menu()
        while opcao == "7":
            a.ordenar()
            self.menu()
        while opcao == "8":
            a.busca_binaria()
            self.menu()
        while opcao == "0":
            sys.exit()
        if opcao > "8" or opcao < "0":
            print("Opção inválida.")

a = Agenda()
  
