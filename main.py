import sys

from car import Car
from truck import Truck


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')

    car1 = Car('blue', 20000)
    print(car1)

    car2 = Car('red', 30000)
    print(car2)

    car3 = Car('white', 999)
    print(car3)

    truck1 = Truck('black', 2000, 72000.61)
    print(truck1)
