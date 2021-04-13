from xml.dom import minidom
from entidades.XML import XML


class LerXML(object):
    def __init__(self):
        print('Lendo XML...')

    def retornaEntidadeXML(self, xml):
        self.xml = xml
        self.camposEntidade = camposEntidade = []
        self.xmlEntidade = ''

        xmldoc = minidom.parse(xml)
        chavelist = xmldoc.getElementsByTagName('chave')
       
    
        index = 0
        for s in chavelist:
            valueAtribute = s.attributes['value'].value
            posIniAtribute = s.attributes['posIni'].value
            posFimAtribute = s.attributes['posFim'].value
            
            camposEntidade.append([valueAtribute,posIniAtribute,posFimAtribute])
            index = index + 1    

        xmlEntidade = XML(camposEntidade[0][0],	    #0
                            camposEntidade[0][1],	#1
                            camposEntidade[0][2],	#2
                            camposEntidade[1][0],	#3
                            camposEntidade[1][1],	#4
                            camposEntidade[1][2],	#5
                            camposEntidade[2][0],	#6
                            camposEntidade[2][1],	#7
                            camposEntidade[2][2],	#8
                            camposEntidade[3][0],	#9
                            camposEntidade[3][1],	#10
                            camposEntidade[3][2],	#11
                            camposEntidade[4][0],	#12
                            camposEntidade[4][1],	#13
                            camposEntidade[4][2],	#14
                            camposEntidade[5][0],	#15
                            camposEntidade[5][1],	#16
                            camposEntidade[5][2],	#17
                            camposEntidade[6][0],#CHAVE_ANO_ATUAL_SOMENTE /18	
                            camposEntidade[6][1],#CHAVE_ANO_ATUAL_SOMENTE /29	
                            camposEntidade[6][2],#CHAVE_ANO_ATUAL_SOMENTE /20	
                            camposEntidade[7][0], 	#21
                            camposEntidade[7][1],	#22
                            camposEntidade[7][2],	#23
                            camposEntidade[8][0],#CHAVE_VALOR_ANO_ATUAL /24	
                            camposEntidade[8][1],#CHAVE_VALOR_ANO_ATUAL /25	
                            camposEntidade[8][2],#CHAVE_VALOR_ANO_ATUAL /26	
                            camposEntidade[9][0],	#27
                            camposEntidade[9][1],	#28
                            camposEntidade[9][2],	#29
                            camposEntidade[10][0],	#30
                            camposEntidade[10][1],	#31
                            camposEntidade[10][2],	#32
                            camposEntidade[11][0],	#33
                            camposEntidade[12][0],	#34
                            camposEntidade[13][0]	#34
                            )

        return xmlEntidade