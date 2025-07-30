from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, color: str, mileage: int):
        super().__init__(color, mileage)


    def get_type(self) -> str:
        return self.__class__.__name__
