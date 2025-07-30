from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, color: str, mileage: int):
        super().__init__(color, mileage)


    def __str__(self):
        # notice that mileage is printed with commas for thousands separation
        return f'The {self.color} car has {self.format_mileage(self.mileage)} miles.'


    def get_type(self) -> str:
        return self.__class__.__name__
