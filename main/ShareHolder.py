from datetime import date
from Person import Person
from Sex import Sex


class ShareHolder(Person):
    def __init__(self, name: str, rg: str, cpf: str, birth_date: date, gender: Sex, share: float, stock_value: float):
        super().__init__(name, rg, cpf, birth_date, gender)

        self._share = share
        self._stock_value = stock_value

    def get_capital(self) -> float:
        return self._stock_value * self._share

    def calculateIncome(self) -> float:
        capital = self.get_capital()

        if self._share <= 25.0:
            return capital * 0.01
        elif self._share <= 50.0:
            return capital * 0.05
        else:
            return capital * 0.10

    @property
    def share(self) -> float:
        return self._share


    @property
    def stock_value(self) -> float:
        return self.stock_value