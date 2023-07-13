class Animal:
    def __init__(self, name: str, type_animal: str):
        self.name = name
        self.type_animal = type_animal

    def get_unic_attr(self):
        temp = ()
        for k, v in self.__dict__.items():
            if k not in ("_name", "_type_animal"):
                temp += (k, v)
        print(temp)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def type_animal(self) -> str:
        return self._type_animal

    @type_animal.setter
    def type_animal(self, type_animal: str):
        self._type_animal = type_animal

    def __str__(self):
        return  str(self.__dict__)


class Cat(Animal):
    def __init__(self, wild: bool, *args):
        super(Cat, self).__init__(*args)
        self.wild = wild

    @property
    def wild(self) -> bool:
        return self._wild

    @wild.setter
    def wild(self, wild: bool):
        self._wild = wild


class Dog(Animal):
    def __init__(self, *args):
        super(Dog, self).__init__(*args)
        self.commands = []

    @property
    def commands(self) -> list:
        return self._commands

    @commands.setter
    def commands(self, command: (str)):
        if isinstance(command, list):
            if command:
                [self._commands.append(i) for i in command]
            else:
                self._commands = []
        elif isinstance(command, str):
            self._commands.append(command)


class Fish(Animal):
    def __init__(self, predator: bool, *args):
        super(Fish, self).__init__(*args)
        self.predator = predator

    @property
    def predator(self) -> bool:
        return self._predator

    @predator.setter
    def predator(self, predator: bool):
        self._predator = predator


if __name__ == '__main__':
    fish = Fish(True, "Валера", "Сом")
    cat = Cat(False, "Семён", "Сфинкс")
    dog = Dog("Луна", "Хаски")
    dog.commands = ["сидеть", "служить"]
    fish.get_unic_attr()
    cat.get_unic_attr()
    dog.get_unic_attr()