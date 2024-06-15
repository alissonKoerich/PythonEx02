from datetime import date
from Person import Person
from Sex import Sex

class Employee(Person):
    def __init__(self, name: str, rg: str, cpf: str, birth_date: date, gender: Sex, salary: float, pis: str, ctps: str):
        super().__init__(name, rg, cpf, birth_date, gender)

        # chama o construtor da superclasse (Person). Isso inicializa os atributos name, rg...... etc

        self._salary = salary
        self._pis = pis
        self._ctps = ctps



    def calculateIncome(self) -> float:
        valueInss = self.getInss()
        valueIr = self.getIr()

        totalSalary = self._salary - valueInss - valueIr

        return totalSalary



    def getIr(self) -> float:
        if self._salary <= 2259.20:
            return 0
        elif self._salary <= 2826.65:
            return (self._salary * 0.075) - 142.80
        elif self._salary <= 3751.05:
            return (self._salary * 0.15) - 354.80
        elif self._salary <= 4664.68:
            return (self._salary * 0.225) - 636.13
        else:
            return (self._salary * 0.275) - 839.36





    def getInss(self) ->float:
        return self._salary * 0.11

    @property
    def salary(self) -> float:
        return self._salary

    @property
    def pis(self) -> str:
        return self._pis

    @property
    def ctps(self) -> str:
        return self._ctps

