import PyPDF2 as p2
import sys
import locale
from datetime import date
from entidades import PDF
from classes.ConsultaChave import ConsultaChave
from entidades.PDF import PDF

class LerPDF(object):
    def __init__(self):
        print('Lendo PDF...')

    def leitura (self, path, 
                valorNoModelo,	                        #0
                    posIniNoModelo,	                    #1
                    posFimNoModelo,	                    #2
                valorNoDataBaseCalculo,	                #3
                    posIniNoDataBaseCalculo,	        #4
                    posFimNoDataBaseCalculo,	        #5
                valorNoValorPrincipal,	                #6
                    posIniNoValorPrincipal,	            #7
                    posFimNoValorPrincipal,	            #8
                valorNoValorJuros,	                    #9
                    posIniNoValorJuros,	                #10
                    posFimNoValorJuros,	                #11
                valorNoQtdParcelasAnosAnteriores,	    #12
                    posIniNoQtdParcelasAnosAnteriores,	#13
                    posFimNoQtdParcelasAnosAnteriores,	#14
                valorNoAnoAtual,	                    #15
                    posIniNoAnoAtual,	                #16
                    posFimNoAnoAtual,	                #17
                valorNoValorAnosAnteriores,	            #18
                    posIniNoValorAnosAnteriores,	    #19
                    posFimNoValorAnosAnteriores,	    #20
                valorNoQtdParcelasAnoAtual,	            #21
                    posIniNoQtdParcelasAnoAtual,	    #22
                    posFimNoQtdParcelasAnoAtual,	    #23
                valorNoValorAnoAtual,	                #24
                    posIniNoValorAnoAtual,	            #25
                    posFimNoValorAnoAtual,	            #26
                valorNoDataMesBaseCalculo,	            #27
                    posIniNoDataMesBaseCalculo,	        #28
                    posFimNoDataMesBaseCalculo,	        #29
                valorNoDataAnoBaseCalculo,	            #30
                    posIniNoDataAnoBaseCalculo,	        #31
                    posFimNoDataAnoBaseCalculo,	        #32
                todasParcelasAnteriores,	            #33
                explanation	                            #34
                ):

        self.valorNoModelo = valorNoModelo
        self.posIniNoModelo = posIniNoModelo
        self.posFimNoModelo = posFimNoModelo
        self.valorNoDataBaseCalculo = valorNoDataBaseCalculo
        self.posIniNoDataBaseCalculo = posIniNoDataBaseCalculo
        self.posFimNoDataBaseCalculo = posFimNoDataBaseCalculo
        self.valorNoValorPrincipal = valorNoValorPrincipal
        self.posIniNoValorPrincipal = posIniNoValorPrincipal
        self.posFimNoValorPrincipal = posFimNoValorPrincipal
        self.valorNoValorJuros = valorNoValorJuros
        self.posIniNoValorJuros = posIniNoValorJuros
        self.posFimNoValorJuros = posFimNoValorJuros
        self.valorNoQtdParcelasAnosAnteriores = valorNoQtdParcelasAnosAnteriores
        self.posIniNoQtdParcelasAnosAnteriores = posIniNoQtdParcelasAnosAnteriores
        self.posFimNoQtdParcelasAnosAnteriores = posFimNoQtdParcelasAnosAnteriores
        self.valorNoAnoAtual = valorNoAnoAtual
        self.posIniNoAnoAtual = posIniNoAnoAtual
        self.posFimNoAnoAtual = posFimNoAnoAtual
        self.valorNoValorAnosAnteriores = valorNoValorAnosAnteriores
        self.posIniNoValorAnosAnteriores = posIniNoValorAnosAnteriores
        self.posFimNoValorAnosAnteriores = posFimNoValorAnosAnteriores
        self.valorNoQtdParcelasAnoAtual = valorNoQtdParcelasAnoAtual
        self.posIniNoQtdParcelasAnoAtual = posIniNoQtdParcelasAnoAtual
        self.posFimNoQtdParcelasAnoAtual = posFimNoQtdParcelasAnoAtual
        self.valorNoValorAnoAtual = valorNoValorAnoAtual
        self.posIniNoValorAnoAtual = posIniNoValorAnoAtual
        self.posFimNoValorAnoAtual = posFimNoValorAnoAtual 
        self.valorNoDataMesBaseCalculo = valorNoDataMesBaseCalculo
        self.posIniNoDataMesBaseCalculo = posIniNoDataMesBaseCalculo
        self.posFimNoDataMesBaseCalculo = posFimNoDataMesBaseCalculo
        self.valorNoDataAnoBaseCalculo = valorNoDataAnoBaseCalculo
        self.posIniNoDataAnoBaseCalculo = posIniNoDataAnoBaseCalculo
        self.posFimNoDataAnoBaseCalculo = posFimNoDataAnoBaseCalculo
        self.todasParcelasAnteriores = todasParcelasAnteriores
        self.explanation = explanation
        self.chave_valor = chave_valor = {}
        dataAtual = date.today()
         
        arquivoPdf = open(path, 'rb')
        pdf_reader = p2.PdfFileReader(arquivoPdf)
        n = pdf_reader.numPages

        for i in range(0, n): 
            page = pdf_reader.getPage(i)
            conteudo = page.extractText()
        
        #Matrix com as palavras chaves
        chavesPosicoes = [[valorNoModelo,posIniNoModelo,posFimNoModelo], 
                          [valorNoDataBaseCalculo,posIniNoDataBaseCalculo,posFimNoDataBaseCalculo],
                          [valorNoValorPrincipal,posIniNoValorPrincipal,posFimNoValorPrincipal],
                          [valorNoValorJuros,posIniNoValorJuros,posFimNoValorJuros],
                          [valorNoQtdParcelasAnosAnteriores,posIniNoQtdParcelasAnosAnteriores,posFimNoQtdParcelasAnosAnteriores],
                          [valorNoAnoAtual,posIniNoAnoAtual,posFimNoAnoAtual],
                          [valorNoValorAnosAnteriores,posIniNoValorAnosAnteriores,posFimNoValorAnosAnteriores],
                          [valorNoQtdParcelasAnoAtual,posIniNoQtdParcelasAnoAtual,posFimNoQtdParcelasAnoAtual],
                          [valorNoValorAnoAtual,posIniNoValorAnoAtual,posFimNoValorAnoAtual],
                          [valorNoDataMesBaseCalculo,posIniNoDataMesBaseCalculo,posFimNoDataMesBaseCalculo],
                          [valorNoDataAnoBaseCalculo,posIniNoDataAnoBaseCalculo,posFimNoDataAnoBaseCalculo]
                         ]
        
        #Inicia a classe de Consulta
        consultaChave = ConsultaChave()
   
        for i in range(0, len(chavesPosicoes)): 
            chaveConsulta = chavesPosicoes[i][0]
            posIni = int(chavesPosicoes[i][1])
            posFim = int(chavesPosicoes[i][2])
              
            #Verifica se existe a chave e retorna o valor se existir
            retornoConsulta = consultaChave.recuperaValorNumerico(conteudo, 
                                                                  path, 
                                                                  chaveConsulta, 
                                                                  posIni, posFim)                        
            #Verifica retorno da consulta
            if retornoConsulta != '':
                #Inclui no dicionario o valor correspondente a cada chave
                chave_valor[chaveConsulta] = retornoConsulta
            else:
                chave_valor[chaveConsulta] = ''
 
        #Concatena o dia no fim do PDF com o mes e ano da data base calculo, 
        chave_valor[valorNoDataBaseCalculo] = chave_valor[valorNoDataBaseCalculo]+'/'+chave_valor[valorNoDataMesBaseCalculo]+'/'+chave_valor[valorNoDataAnoBaseCalculo]
        
        #Verifica o ano atual (data corrente) com o ano da data base
        if ((int(chave_valor[valorNoAnoAtual])) == int(dataAtual.strftime('%Y'))):
            #print ('igual')
            ##############################################################################
            #  Se o ano de "Ano atual (AAAA)" for igual ao ano da data corrente,         #
            #  preenche os campos conforme os valores anteriores e atual                 #
            ##############################################################################
            NMExercicioAnterior = int(chave_valor[valorNoQtdParcelasAnosAnteriores])
            NMExercicioAtual = int(chave_valor[valorNoQtdParcelasAnoAtual])
            chave_valor['explanation'] = '  OBS.: O ano no PDF em ' + '\033[1m' + 'Ano Atual'+ '\033[0m (' + chave_valor[valorNoAnoAtual] +') é igual ao ano corrente (' +dataAtual.strftime('%Y')+ '). A Qtd. Parcela em Anos Anteriores deve ser preenchida em ' + '\033[1m' + 'NM Exercícios Anteriores'+ '\033[0m e Qtd. Parcelas em Ano Atual (' + chave_valor[valorNoAnoAtual] + '), preencher em ' + '\033[1m' + 'NM Exercício Corrente'+ '\033[0m.'
            chave_valor['todasParcelasAnteriores'] = 0   
        else: 
            #################################################################################
            #  Se o ano de "Anos anteriores" e o ano de "Ano atual(AAAA)",                  #
            #  forem anteriores ao ano da data corrente, soma-se as quantidades de parcelas.#                                                              #
            ################################################################################# 
            NMExercicioAnteriorAtual = int(chave_valor[valorNoQtdParcelasAnosAnteriores]) + int(chave_valor[valorNoQtdParcelasAnoAtual])
            chave_valor['explanation'] = '  OBS.: O ano no PDF em ' + '\033[1m' + 'Ano Atual'+ '\033[0m (' + chave_valor[valorNoAnoAtual] +') é anterior ao ano corrente (' +dataAtual.strftime('%Y')+ '). Por este motivo a Qtd. Parcela em Anos Anteriores e a Qtd. Parcelas em Ano Atual (' + chave_valor[valorNoAnoAtual] + '), foram somadas e consideradas como ' + '\033[1m' + 'NM Exercícios Anteriores'+ '\033[0m.'
            chave_valor['todasParcelasAnteriores'] = NMExercicioAnteriorAtual
    
        #Gravando na entidade PDF 
        pdf = PDF(path,
                 chave_valor.get(valorNoModelo),
                 chave_valor.get(valorNoDataBaseCalculo),
                 chave_valor.get(valorNoValorPrincipal),
                 chave_valor.get(valorNoValorJuros),
                 chave_valor.get(valorNoQtdParcelasAnosAnteriores),
                 chave_valor.get(valorNoValorAnosAnteriores),
                 chave_valor.get(valorNoQtdParcelasAnoAtual),
                 chave_valor.get(valorNoValorAnoAtual),
                 chave_valor.get(valorNoDataMesBaseCalculo),
                 chave_valor.get(valorNoDataAnoBaseCalculo),
                 chave_valor.get(todasParcelasAnteriores),
                 chave_valor.get(explanation),
                )
                
        return pdf