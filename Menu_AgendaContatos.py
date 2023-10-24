from Agenda_Contatos import Agenda_Telefonica
from No import No
from Contato import Contato

lista_agenda = Agenda_Telefonica()

while True:
    print("\n\t\t ____BEM_VINDOS_A_LISTA_DE_CONTATOS_____")
    print("\t\t ---------------------------------------")
    print("\t\t| 1. Adicionar Contato:\t\t\t|")
    print("\t\t| 2. Listar Contatos\t\t\t|")
    print("\t\t| 3. Remover Contato pelo \'NOME\'\t|")
    print("\t\t| 4. Buscar Contato pelo \'NOME\'\t\t|")
    print("\t\t| 5. Listar Agenda\t\t\t|")
    print("\t\t| 6. Apagar toda a Agenda\t\t|")
    print("\t\t| 0. Sair\t\t\t\t|")
    print("\t\t ---------------------------------------")
    opcao = int(input("Digite uma OPÇÃO: "))
    if opcao == 1:
      print("\tVAMOS INSERIR UM NOVO CONTATO")
      nome = input("Me informe o nome do CONTATO: ")
      telefone = int(input("Agora o número do CONTATO: "))
      contato = Contato (nome, telefone)
      print("Novo contato adicionado")
      lista_agenda.inserir_novocontato(contato)

    elif opcao == 2:
      print("Contatos na Agenda")
      lista_agenda.listar_contatos()

    elif opcao == 3:
      nome = input("Nome do contato a ser removido: ")
      lista_agenda.remover_contato_nome(nome)
      print(f"Contato com o nome {nome} removido, se existir.")

    elif opcao == 4:
      nome = input("Nome do contato a ser buscado: ")
      contato = lista_agenda.buscar_contato_por_nome(nome)
      if contato:
          print(f"Contato encontrado: {contato}")
      else:
          print(f"Contato com o nome {nome} não encontrado.")

    elif opcao == 5:
      print("Agenda completa:")
      lista_agenda.listar_agenda()

    elif opcao == 6:
      lista_agenda.apagar_agenda()
      print("Toda a agenda foi apagada!")
      
    elif opcao == 0:
       print("\tSystem: \'ENCERRANDO AGENDA DE CONTATO\'")
       break
    else:
      print("Comando inválido!!!")