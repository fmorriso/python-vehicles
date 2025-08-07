from vehicle import Vehicle


class Truck(Vehicle):
    """A class to represent a truck."""

    def __init__(self, color: str, mileage: int, cost: float):
        super().__init__(color, mileage, cost)


    def get_type(self) -> str:
        return self.__class__.__name__
