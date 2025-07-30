import locale

from vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, color: str, mileage: int, cost: float):
        super().__init__(color, mileage, cost)



    def get_type(self) -> str:
        return self.__class__.__name__


    def __str__(self):
        # notice that mileage is printed with commas for thousands separation and cost is formatted as currency (US)
        return (f'The {self.color} truck has {self.format_mileage(self.mileage)} miles and costs'
                f' {self.format_currency(self.cost)}.')
