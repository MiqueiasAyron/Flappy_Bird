# Como Funcionam Classes e Programação Orientada a Objetos (POO) em Python

# vendedor = 'Lira'

# vendas = 1000

# meta = 600

# if vendas >= meta:
#     print(f'{vendedor} bateu a meta!')
# else:
#     print(f'{vendedor} não bateu a meta')


'''

Imagine que você queira implementar esse programa numa empresa com vários vendedores.
Seria inviável criar todo esse script para cada um deles.Perceba que 'Lira' é apenas 
uma instância ( um elemento ) dentro de uma classe (conjunto) que são os vendedores. 
Se na empresa temos 'Lira', 'Marcos', 'Pedro', etc, por mais que sejam vendedores 
diferentes, com nomes e vendas distintas, ainda assim todos são VENDEDORES.

'''

'''
Então, o que nós vamos fazer é criar uma classe para os vendedores:
'''

# class Vendedor():
#     def __init__(self, nome):   # essa é a função de inicialização que cria Vendedor e atribui os parâmetros nescessários para definir esse vendedor. No caso, pra definir um vededor só precisamos do nome
#         self.nome = nome
#         self.vendas = 0 # quando o VENDEDOR é criado, ele começa com vendas = 0
      

#     def vendeu(self, vendas):
#         self.vendas = vendas # aqui editamos o VENDAS para o valor que vamos informar no parêntese (self, vendas)

#     def bateu(self, meta):
#         if self.vendas > meta:
#             print(self.nome , 'bateu a meta')
#         else:
#             print(self.nome , 'não bateu a meta')

'''
Agora você pode usar a classe construída para criar o código
'''

# vendedor1 = Vendedor('Lira')
# vendedor1.vendeu(1000)
# vendedor1.bateu(600)

# vendedor2 = Vendedor('Marcos')
# vendedor2.vendeu(450)
# vendedor2.bateu(600)

'''
Uma vantagem das classes é que podemos criar todas as classes de um programa em uma pasta separada e quando precisar
apenas importar.
'''
from classesad import Vendedor

vendedor1 = Vendedor('Lira')
vendedor1.vendeu(1000)
vendedor1.bateu(600)

vendedor2 = Vendedor('Marcos')
vendedor2.vendeu(450)
vendedor2.bateu(600)

'''
As características das instâncias dentro de uma classe são definidas dentro da função __init__  e os métodos 
(coisas que os elementos da classe podem fazer) são definidos como outras funções.
'''
