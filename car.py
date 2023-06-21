class Car:

    def __init__(self, color: str, mileage: int):
        self.color: str = color
        self.mileage: int = mileage

    def __str__(self):
        # notice that mileage is printed with commas for thousands separation
        return f'The {self.color} car has {self.mileage:,} miles.'

