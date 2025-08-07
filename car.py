from vehicle import Vehicle


class Car(Vehicle):
    """A class to represent a car."""

    def __init__(self, color: str, mileage: int):
        super().__init__(color, mileage)


    def get_type(self) -> str:
        return self.__class__.__name__
