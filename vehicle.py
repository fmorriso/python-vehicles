import locale
from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):

    def __init__(self, color: str, mileage: int, cost: Optional[float] = None):
        self.color: str = color
        self.mileage: int = mileage
        self.cost: float = cost
        # set locale to US
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


    @abstractmethod
    def get_type(self) -> str:
        pass


    @classmethod
    def format_currency(cls, amount: float | int) -> str:
        # format currency value
        return locale.currency(amount, grouping = True)


    @classmethod
    def format_mileage(cls, amount: float | int) -> str:
        # Format with grouping, no currency symbol
        return locale.format_string('%.1f', amount, grouping = True)
