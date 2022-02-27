from datetime import datetime


class Datas_BR:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana_cadastro(self):
        dias_da_semana = [
            "Segunda-Feira", "Terça-Feira", "Quarta-Feira",
            "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias_da_semana[dia_cadastro]
