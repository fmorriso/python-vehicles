class Car:

    def __init__(self, color: str, mileage: int):
        self.color: str = color
        self.mileage: int = mileage

    @staticmethod
    def format_with_comma_separator(amount: float | int) -> str:
        return f"{amount:,}"

    def __str__(self):
        # notice that mileage is printed with commas for thousands separation
        return f'The {self.color} car has {Car.format_with_comma_separator(self.mileage)} miles.'
