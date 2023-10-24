from No import No
class Agenda_Telefonica:
    
    def __init__(self):
        self.__inicio = None

    def is_vazia(self):
        return self.__inicio is None

    def inserir_novocontato(self, contato):
        novo_no = No(contato)
        novo_no.prox = self.__inicio
        self.__inicio = novo_no

    def listar_contatos(self):
        atual = self.__inicio
        while atual is not None:
            print(atual.contato)
            atual = atual.prox

    def remover_contato_nome (self, nome):
        anterior = None
        atual = self.__inicio
        while atual != None:
          if anterior is None:
            self.__inicio = atual.prox
          else:
            anterior.prox = atual.prox
          return
        anterior = atual
        atual = atual.prox

    def buscar_contato_por_nome(self, nome):
        atual = self.__inicio
        while atual is not None:
            if atual.contato.nome == nome:
                return atual.contato
            atual = atual.prox
        return None

    def listar_agenda(self):
        self.listar_contatos()

    def apagar_agenda(self):
        self.__inicio = None