import random

class SimuladorDeDados:

    def __init__(self):
        
        self.ValorMinimo = 1
      
        self.Mensagem = 'Digite qual o número maximo :'

        self.Mensagem2 = 'Digite Sim para que o numero seja gerado: '

        self.Saida = 'Obrigado por participar!'

        self.Mensagem3 = 'Digite Sim para tentar de novo ou Sair para sair: '

        self.Again = 'Digite Sim ou Sair!'

        self.MensagemError = 'Ocorreu um erro na leitura, reinicie o programa!'
        
    
    
    def Escolha(self):

        escolha = int(input(self.Mensagem))

        self.ValorMaximo = escolha


    def inicio (self):

        resposta = str(input(self.Mensagem2))

        if resposta == 'Sim' or resposta == 'sim':

            self.GravarValorDoDado( )   

        elif resposta != 'sim' or resposta != 'Sim':

            print(self.mensagemErrorInicio) 

            return simulador.inicio( )

        else:

            print(self.Again)

            return simulador.inicio() 

    def Denovo(self):
        
        
        resposta2 = str(input(self.Mensagem3))
        
        try:

                if resposta2 == 'Sim' or resposta2 == 'sim': 

                    self.GravarValorDoDado( )

                    return simulador.Denovo( )
                
                               
                elif resposta2 == 'Sair' or resposta2 =='sair':

                    print(self.Saida)


                else:

                    print(self.Again)

                    return simulador.Denovo( )


        except: 
            
            print(self.MensagemError)

    def GravarValorDoDado(self):

        print(random.randint(self.ValorMinimo, self.ValorMaximo))


simulador = SimuladorDeDados( )

simulador.Escolha( )

simulador.inicio( )

simulador.Denovo( )