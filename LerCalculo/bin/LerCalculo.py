from classes.LerXML import LerXML
from classes.LerPDF import LerPDF
from classes.ImpressaoTela import ImpressaoTelaPDF
from entidades.XML import XML
import os

#Carregar Configuração
lerXML = LerXML()

#Caminho od OS
path = os.path.dirname(os.path.realpath(__file__))

#Caminho do XML
xmlPath = path + '/xml/config.xml'

#Para teste local 
dadosXML = lerXML.retornaEntidadeXML(xmlPath)   


#print(dadosXML)

#Ler PDF
lerPDF = LerPDF()
entidadePDF = lerPDF.leitura(dadosXML.pathPDF,
                dadosXML.valorNoModelo,
                dadosXML.posIniNoModelo,
                dadosXML.posFimNoModelo,
                dadosXML.valorNoDataBaseCalculo,
                dadosXML.posIniNoDataBaseCalculo,
                dadosXML.posFimNoDataBaseCalculo,
                dadosXML.valorNoValorPrincipal,
                dadosXML.posIniNoValorPrincipal,
                dadosXML.posFimNoValorPrincipal,
                dadosXML.valorNoValorJuros,
                dadosXML.posIniNoValorJuros,
                dadosXML.posFimNoValorJuros,
                dadosXML.valorNoQtdParcelasAnosAnteriores,
                dadosXML.posIniNoQtdParcelasAnosAnteriores,
                dadosXML.posFimNoQtdParcelasAnosAnteriores,
                dadosXML.valorNoAnoAtual,
                dadosXML.posIniNoAnoAtual,
                dadosXML.posFimNoAnoAtual,
                dadosXML.valorNoValorAnosAnteriores,
                dadosXML.posIniNoValorAnosAnteriores,
                dadosXML.posFimNoValorAnosAnteriores,
                dadosXML.valorNoQtdParcelasAnoAtual,
                dadosXML.posIniNoQtdParcelasAnoAtual,
                dadosXML.posFimNoQtdParcelasAnoAtual,
                dadosXML.valorNoValorAnoAtual,
                dadosXML.posIniNoValorAnoAtual,
                dadosXML.posFimNoValorAnoAtual,
                dadosXML.valorNoDataMesBaseCalculo,
                dadosXML.posIniNoDataMesBaseCalculo,
                dadosXML.posFimNoDataMesBaseCalculo,
                dadosXML.valorNoDataAnoBaseCalculo,
                dadosXML.posIniNoDataAnoBaseCalculo,
                dadosXML.posFimNoDataAnoBaseCalculo,
                dadosXML.todasParcelasAnteriores,
                dadosXML.explanation)
  
#Imprime os dados da entidade PDF
impressao = ImpressaoTelaPDF(entidadePDF)