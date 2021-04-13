import re

class ConsultaChave(object):
    def __init__(self):
        print ('Consultando Chaves...')
        
    def recuperaValorNumerico(self, conteudo, path, chaveConsulta, posIni, posFim): 
        self.conteudo = conteudo
        self.path = path
        self.chaveConsulta = chaveConsulta 
        self.posIni = posIni
        self.posFim = posFim
        index = 0
        valorChave = ''
        
        #Busca palavra chave
        posicaoChave=conteudo.find(chaveConsulta)#chave
        #Recupera o valor conforme as chaves e posicao de cada uma delas
        rangeValorChave = conteudo[posicaoChave+posIni:posicaoChave+posFim]  
        
        #print(rangeValorChave)
        #Recupera somente os numeros da string
        if rangeValorChave[0:2] == 'R$':
            for letra in rangeValorChave:
                if (letra == ','):
                    #valorChave = "".join(re.findall("\d+", rangeValorChave[0:index+3]))#Numeral com R$ sem formatacao
                    valorChave = rangeValorChave[0:index+3] #Numeral com R$ formatado
                    break
                index = index + 1
        else:
            for letra in rangeValorChave:
                if (letra == 'R'):
                    valorChave = "".join(re.findall("\d+", rangeValorChave[0:index]))#Numeral sem R$
                    break
                else:
                    valorChave = rangeValorChave[0:index+1]#Demais textos
                index = index + 1            
        
        return valorChave.strip()