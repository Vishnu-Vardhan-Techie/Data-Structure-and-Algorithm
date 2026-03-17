class House:
    def __init__(
        self,
        bedrooms,
        bathrooms,
        kitchen,
        garden,
        garage,
        pool,
        solar_panels,
        smart_home,
    ):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.kitchen = kitchen
        self.garden = garden
        self.garage = garage
        self.pool = pool
        self.solar_panels = solar_panels
        self.smart_home = smart_home

    def __str__(self):
        features = [
            f"Bedrooms: {self.bedrooms}",
            f"Bathrooms: {self.bathrooms}",
            f"Kitchen: {self.kitchen}",
            f"Garden: {self.garden}",
            f"Garage: {self.garage}",
            f"Pool: {self.pool}",
            f"Solar_panels: {self.solar_panels}",
            f"smart_home: {self.smart_home}",
        ]
        return " | ".join(features)


class HouseBuilder:
    def __init__(self):
        self.bedrooms = 1
        self.bathrooms = 1
        self.kitchen = True
        self.garden = False
        self.garage = False
        self.pool = False
        self.solar_panels = False
        self.smart_home = False

    def set_bedrooms(self, count):
        self.bedrooms = count
        return self

    def set_bathrooms(self, count):
        self.bathrooms = count
        return self

    def add_garden(self):
        self.garden = True
        return self

    def add_garage(self):
        self.garage = True
        return self

    def add_pool(self):
        self.pool = True
        return self

    def add_solar_panels(self):
        self.solar_panels = True
        return self

    def add_smart_home(self):
        self.smart_home = True
        return self

    def build(self):
        return House(
            self.bedrooms,
            self.bathrooms,
            self.kitchen,
            self.garden,
            self.garage,
            self.pool,
            self.solar_panels,
            self.smart_home,
        )


house_builder = HouseBuilder()

custom_house = (
    house_builder.set_bedrooms(1)
    .set_bathrooms(1)
    .add_garden()
    .add_garage()
    .add_pool()
    .add_solar_panels()
    .add_smart_home()
    .build()
)

print("Custom_house: ", custom_house)
