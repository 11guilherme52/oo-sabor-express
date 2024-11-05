from modelos.avaliacao import Avaliacao

class Restaurante:
    
    '''Definição da classe Restaurante e suas atribuições'''
    
    restaurantes =[]
    
    def __init__(self, nome, categoria):
        
        '''
        Inicializa a classe, fazendo atribuições às instâncias que seram criadas.
        
        Parâmetros:
        -nome (string): Nome do restaurante
        -categoria (string): Categoria do restaurante

        '''
        self.nome = nome.title()
        self.categoria = categoria
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        
        '''Retorna uma representação em string do restaurante.'''
        
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        
        '''Faz a listagem de todos os restaurantes já criados. '''
        
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_ava).ljust(25)} | {restaurante.status} ')
    
    @property
    def status(self):
        
        '''Modifica a forma de visualização do status do restaurante.'''
        
        return 'V' if self._status else 'F' 

    def alternar_estado(self):
        
        '''Faz alteração do status de um restaurante, entre ativo ou inativo.'''
        
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        
        '''Recebe avaliações de acordo com a condicional atribuida a ela e armazena na lista de avaliações.'''
        
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente , nota)
            self._avaliacao.append(avaliacao)

    @property #torna possivel a leitura da media das avaliaçoes para cada 'objeto'
    def media_ava(self):
        
        '''Realiza o cálculo de média das avaliações recebidas de cada restaurante'''
        
        if not self._avaliacao:
            return '-'
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


