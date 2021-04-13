class XML(object):
    def __init__(self, 
                valorNoModelo,                              #0
                    posIniNoModelo,                         #1
                    posFimNoModelo,                         #2
                valorNoDataBaseCalculo,                     #3
                    posIniNoDataBaseCalculo,                #4
                    posFimNoDataBaseCalculo,                #5
                valorNoValorPrincipal,                      #6
                    posIniNoValorPrincipal,                 #7
                    posFimNoValorPrincipal,                 #8
                valorNoValorJuros,                          #9
                    posIniNoValorJuros,                     #10
                    posFimNoValorJuros,                     #11
                valorNoQtdParcelasAnosAnteriores,           #12
                    posIniNoQtdParcelasAnosAnteriores,      #13
                    posFimNoQtdParcelasAnosAnteriores,      #14
                valorNoAnoAtual,                            #15
                    posIniNoAnoAtual,                       #16
                    posFimNoAnoAtual,                       #17
                valorNoValorAnosAnteriores,      #CHAVE_ANO_ATUAL_SOMENTE 18
                    posIniNoValorAnosAnteriores, #CHAVE_ANO_ATUAL_SOMENTE 19
                    posFimNoValorAnosAnteriores, #CHAVE_ANO_ATUAL_SOMENTE 20
                valorNoQtdParcelasAnoAtual,                 #21
                    posIniNoQtdParcelasAnoAtual,            #22
                    posFimNoQtdParcelasAnoAtual,            #23
                valorNoValorAnoAtual,              #CHAVE_VALOR_ANO_ATUAL 24
                    posIniNoValorAnoAtual,         #CHAVE_VALOR_ANO_ATUAL 25
                    posFimNoValorAnoAtual,         #CHAVE_VALOR_ANO_ATUAL 26
                valorNoDataMesBaseCalculo,                  #27
                    posIniNoDataMesBaseCalculo,             #28
                    posFimNoDataMesBaseCalculo,             #29
                valorNoDataAnoBaseCalculo,                  #30
                    posIniNoDataAnoBaseCalculo,             #31
                    posFimNoDataAnoBaseCalculo,             #32
                todasParcelasAnteriores,                    #33
                explanation,                                #34
                pathPDF):                                   #35
    
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

        self.valorNoValorAnosAnteriores = valorNoValorAnosAnteriores    #CHAVE_ANO_ATUAL_SOMENTE 18
        self.posIniNoValorAnosAnteriores = posIniNoValorAnosAnteriores  #CHAVE_ANO_ATUAL_SOMENTE 19
        self.posFimNoValorAnosAnteriores = posFimNoValorAnosAnteriores  #CHAVE_ANO_ATUAL_SOMENTE 20

        self.valorNoQtdParcelasAnoAtual = valorNoQtdParcelasAnoAtual
        self.posIniNoQtdParcelasAnoAtual = posIniNoQtdParcelasAnoAtual
        self.posFimNoQtdParcelasAnoAtual = posFimNoQtdParcelasAnoAtual

        self.valorNoValorAnoAtual = valorNoValorAnoAtual    #CHAVE_VALOR_ANO_ATUAL 24
        self.posIniNoValorAnoAtual = posIniNoValorAnoAtual  #CHAVE_VALOR_ANO_ATUAL 25
        self.posFimNoValorAnoAtual = posFimNoValorAnoAtual  #CHAVE_VALOR_ANO_ATUAL 26

        self.valorNoDataMesBaseCalculo = valorNoDataMesBaseCalculo
        self.posIniNoDataMesBaseCalculo = posIniNoDataMesBaseCalculo
        self.posFimNoDataMesBaseCalculo = posFimNoDataMesBaseCalculo

        self.valorNoDataAnoBaseCalculo = valorNoDataAnoBaseCalculo
        self.posIniNoDataAnoBaseCalculo = posIniNoDataAnoBaseCalculo
        self.posFimNoDataAnoBaseCalculo = posFimNoDataAnoBaseCalculo

        self.todasParcelasAnteriores = todasParcelasAnteriores
        self.explanation = explanation
        self.pathPDF = pathPDF