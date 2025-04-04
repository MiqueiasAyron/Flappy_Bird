# vamos criar uma classe para Clientes da Netflix

class Cliente():
    def __init__(self, nome, email, plano): #todas as variáveis da classe devem ser criadas dentro da função __init__. Uma vez criadas, essas variáves podem ser usadas dentro de outras funções da mesma classe
        self.NOME = nome
        self.EMAIL = email
        self.LIST_PLANOS = ['basic', 'premium'] # estou restringindo os planos que podem ser associados ao cliente
        if plano in self.LIST_PLANOS:
            self.PLANO = plano
        else:
            raise Exception('Plano Inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.LIST_PLANOS:
            self.PLANO = novo_plano
        else:
            print('Plano Inválido')
    
    def ver_filme(self, filme, plano_filme):
        if self.PLANO == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.PLANO == plano_filme:
            print(f'Ver filme {filme}')
        elif self.PLANO == 'basic' and plano_filme == 'premium':
            print('Faça um Upgrade premium para ver esse filme')
        else:
            print('Plano Inválido')

    


        '''
        Informações que são fixas para todos os clientes não precisam ser definidas como variáveis no __init__
        No nosso caso, por exemplo, o cliente só pode ter ou plano basic ou premium. 
        '''

cliente = Cliente('Lira', 'lira@gmail.com','basic')
print(cliente.NOME)
print(cliente.PLANO)
cliente.ver_filme('Harry Potter', 'premium')

#no botão UPGRADE
cliente.mudar_plano('premium')
print(cliente.PLANO)
cliente.ver_filme('Harry Potter', 'premium')