
import tkinter as tk
from tkinter import messagebox
 

class ImpressaoTelaPDF(object):
    def __init__(self, pdf):
        self.pdf = pdf

        if (pdf.todasParcelasAnteriores == 0):
            messagebox.showinfo("Dados do Cálculo", pdf.modelo + "\n" + "\n"+ 
                                "Data-base de Cáculo: " + pdf.dataBaseCalculo + "\n"+
                                "Valor (com Honorários Contratuais/Cessão):" + "\n"+
                                "  Valor Principal: " + pdf.valorPrincipal + "\n"+
                                "  Valor Juros: " + pdf.valorJuros + "\n"+
                                "NM Exercícios Anteriores: " + str(pdf.qtdParcelasAnosAnteriores) + "\n"+
                                "Valor Exercícios Anteriores: Atenção: Recuperar valor calculado na tela do CRETA." + "\n"+
                                "NM Exercício Corrente: " + str(pdf.qtdParcelasAnoAtual) + "\n"+
                                "Valor Exercício Corrente:" +  "\n" + "  (Recuperar valor calculado na tela do CRETA.)" + "\n"
                                )
        else:
            messagebox.showinfo("Dados do Cálculo", pdf.modelo + "\n" + "\n"+ 
                                "Data-base de Cáculo: " + pdf.dataBaseCalculo + "\n"+
                                "Valor (com Honorários Contratuais/Cessão):" + "\n"+
                                "  Valor Principal: " + pdf.valorPrincipal + "\n"+
                                "  Valor Juros: " + pdf.valorJuros + "\n"+
                                "NM Exercícios Anteriores: " + str(pdf.todasParcelasAnteriores) + "\n"+
                                "Valor Exercícios Anteriores:" +  "\n" + "  (Recuperar valor calculado na tela do CRETA.)" + "\n"
                                )
