class PDF(object):   
    def __init__(self, path, modelo, dataBaseCalculo, valorPrincipal, 
                 valorJuros, qtdParcelasAnosAnteriores, valorAnosAnteriores,
                 qtdParcelasAnoAtual, valorAnoAtual, mesBaseCalculo, anoBaseCalculo, 
                 todasParcelasAnteriores, explanation):
        self.path = path
        self.modelo = modelo
        self.dataBaseCalculo = dataBaseCalculo
        self.valorPrincipal = valorPrincipal
        self.valorJuros = valorJuros
        self.qtdParcelasAnosAnteriores = qtdParcelasAnosAnteriores 
        self.valorAnosAnteriores = valorAnosAnteriores
        self.qtdParcelasAnoAtual = qtdParcelasAnoAtual
        self.valorAnoAtual = valorAnoAtual 
        self.mesBaseCalculo = mesBaseCalculo
        self.anoBaseCalculo = anoBaseCalculo
        self.todasParcelasAnteriores = todasParcelasAnteriores
        self.explanation = explanation