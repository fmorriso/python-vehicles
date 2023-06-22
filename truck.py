import locale

class Truck:

    def __init__(self, color: str, mileage: int, cost: float):
        self.color: str = color
        self.mileage: int = mileage
        self.cost: float = cost

    @staticmethod
    def format_currency(amount: float) -> str:
        # set locale to US
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        # format currency value
        return locale.currency(amount, grouping=True)

    def __str__(self):
        # notice that mileage is printed with commas for thousands separation and cost is formatted as currency (US)
        return f'The {self.color} truck has {self.mileage:,} miles and costs {Truck.format_currency(self.cost)}.'
