class ControlTower:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Intializing Control Tower")
        return cls._instance

    def Manageflight(self, flight):
        print(f"Managing Flight {flight}")


tower1 = ControlTower()
tower2 = ControlTower()

tower1.Manageflight("Air India")
tower2.Manageflight("Indigo")

print(tower1 is tower2)
