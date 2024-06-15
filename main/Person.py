from abc import ABC, abstractmethod
from datetime import date
from Sex import Sex

class Person(ABC):
    def __init__(self, name: str, rg: str, cpf: str, birth_date: date, gender: Sex):
        self._name = name
        self._rg = rg
        self._cpf = cpf
        self._birth_date = birth_date
        self._gender = gender

    @abstractmethod
    def calculateIncome(self) -> float:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def rg(self) -> str:
        return self._rg

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @property
    def gender(self) -> Sex:
        return self._gender
