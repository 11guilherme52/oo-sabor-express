from modelos.avaliacao import Avaliacao

class Restaurante:
    
    restaurantes =[]
    
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_ava).ljust(25)} | {restaurante.status} ')
    
    @property
    def status(self):
        return 'V' if self._status else 'F' 

    def alternar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente , nota)
        self._avaliacao.append(avaliacao)

    @property #torna possivel a leitura da media das avaliaçoes para cada 'objeto'
    def media_ava(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media










#print(restaurantes)
#[<__main__.Restaurante object at 0x00000156FF4F6A50>] ( Nao mostra detalhes, apenas o local da memoria onde esta o objeto)

#print(restaurante_pizza)
#<__main__.Restaurante object at 0x000001AAD69E6A50>

#print(dir(restaurante_pizza)) #FUNÇÃO PARA VER MÉTODOS E ATRIBUTOS / QUANDO NÃO CONHECEMOS UMA CLASSE

#print(vars(restaurante_pizza))# DICIONARIO DOS ATRIBUTOS E METODOS
#{'nome': 'Pizza', 'categoria': 'Gourmet'}


