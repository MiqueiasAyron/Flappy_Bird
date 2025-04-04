#CLASSE VENDEDOR

class Vendedor():
    def __init__(self, nome):   # essa é a função de inicialização que cria Vendedor e atribui os parâmetros nescessários para definir esse vendedor. No caso, pra definir um vededor só precisamos do nome
        self.nome = nome
        self.vendas = 0 # quando o VENDEDOR é criado, ele começa com vendas = 0
      

    def vendeu(self, vendas): # função da classe Vendedor
        self.vendas = vendas # aqui editamos o VENDAS para o valor que vamos informar no parêntese (self, vendas)

    def bateu(self, meta): # função da classe Vendedor
        if self.vendas > meta:
            print(self.nome , 'bateu a meta')
        else:
            print(self.nome , 'não bateu a meta')
