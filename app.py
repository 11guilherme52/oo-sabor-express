from modelos.restaurante import Restaurante 

restaurante_priscila = Restaurante('D` Priscila','Italiana')
restaurante_priscila.receber_avaliacao('Gui',2)
restaurante_priscila.receber_avaliacao('John',2)
restaurante_priscila.receber_avaliacao('Breno',5)
restaurante_priscila._status = True


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()