"""
Simple example of class composition.
"""


class CombustionEngine:
    def __init__(self):
        print("Create CombustionEngine.")

    def changeSparkPlug(self):
        pass


class ElectricEngine:
    def __init__(self):
        print("Create ElectricEngine.")


class Vehicle:
    def __init__(self):
        print("Create Vehicle.")
        self.engine = CombustionEngine()  # Default engine.


class LunarRover(Vehicle):
    changeSparkPlug = None  # Override method from Vehicle.

    def __init__(self):
        print("Create LunarRover.")
        self.engine = ElectricEngine()


my_vehicle = LunarRover()
