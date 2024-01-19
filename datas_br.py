from datetime import datetime
class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_ano =["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"]
        mes_cadastro = self.momento_cadastro.month
        return meses_ano[mes_cadastro-1]

    def dia_semana(self):
        dias = ["DOM","SEG","TER","QUA","QUI","SEX","SAB"]
        semana = self.momento_cadastro.weekday()
        return dias[semana+1]


