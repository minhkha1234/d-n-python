"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """A basic animal with a name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """Return a generic sound for an animal."""
        return "Some sound"


class Dog(Animal):
    """A dog is an Animal and has its own speaking behavior."""

    def speak(self) -> str:
        """Return the sound a dog makes."""
        return "Woof!"


def main() -> None:
    """Create an animal and a dog to demonstrate inheritance."""
    animal = Animal("Animal")
    dog = Dog("Buddy")

    print(f"{animal.name}: {animal.speak()}")
    print(f"{dog.name}: {dog.speak()}")
    print("Dog is an Animal because Dog inherits Animal's shared attributes and behavior.")


if __name__ == "__main__":
    main()
