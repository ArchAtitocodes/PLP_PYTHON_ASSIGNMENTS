# Base class
class Superhero:
    def __init__(self, name, power, origin, level):
        self.name = name
        self.power = power
        self.origin = origin
        self.level = level

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")

    def fight(self, enemy):
        print(f"{self.name} fights {enemy} using {self.power}!")

    def train(self):
        self.level += 1
        print(f"{self.name} is training... Level is now {self.level}")

# Subclass using inheritance
class Villain(Superhero):
    def __init__(self, name, power, origin, level, evil_plan):
        super().__init__(name, power, origin, level)
        self.evil_plan = evil_plan

    def reveal_plan(self):
        print(f"{self.name} reveals their evil plan: {self.evil_plan}")

    # Method override (polymorphism)
    def fight(self, enemy):
        print(f"{self.name} sneakily attacks {enemy} with {self.power}... Muahaha!")

# Example usage
hero = Superhero("Nova Girl", "Light Manipulation", "Star City", 5)
villain = Villain("Darkshade", "Shadow Control", "Underrealm", 6, "Plunge the world into darkness")

hero.introduce()
villain.introduce()
hero.fight("Darkshade")
villain.fight("Nova Girl")
hero.train()
villain.reveal_plan()
