class Pizza:
    def prepare(self):
        return NotImplementedError("This method should be overridden by subclasses")


class CheesePizza(Pizza):
    def prepare(self):
        return "Preparing Cheese Pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        return "Preparing Pepperoni Pizza"


class VeggiePizza(Pizza):
    def prepare(self):
        return "Preparing Veggie Pizza"


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Cheese":
            return CheesePizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
        elif pizza_type == "Veggie":
            return VeggiePizza()
        else:
            raise ValueError(f"Unknown Pizza Type: {pizza_type}")


def main():
    try:
        user_input = "Pepperoni"
        pizza = PizzaFactory.create_pizza(user_input)
        print(pizza.prepare())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
