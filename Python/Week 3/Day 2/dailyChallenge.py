class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = dict()

    def addAnimal(self, animal, q=1):
        if animal in self.animals:
            self.animals[animal] += q
        else:
            self.animals[animal] = q

    def getInfo(self):
        print("{}'s farm".format(self.name))
        print()
        for key, value in self.animals.items():
            print('{}:{}'.format(key, value))
        print()
        print('E-I-E-I-0!')

    def getAnimalTypes(self):
        animals = list()
        for key, value in self.animals.items():
            animals.append(key)
        return(sorted(animals))

    def getShortInfo(self):
        animals = self.getAnimalTypes()
        info = "{}'s farm has ".format(self.name)
        if len(animals) == 1:
            info += (animals[0] + 's')
        elif len(animals) == 2:
            first = True
            for a in animals:
                if first:
                    info += (animals[0] + 's')
                    first = False
                else:
                    info += ('and ' + animals[0] + 's')
        else:
            first = True
            last = animals[-1]
            for a in animals:
                if first:
                    info += (a + 's')
                    first = False
                elif last == a:
                    info += (' and ' + a + 's')
                else:
                    info += (', ' + a + 's')
        print(info)

f = Farm("McDonald")
f.addAnimal('cow',5)
f.addAnimal('sheep')
f.addAnimal('sheep')
f.addAnimal('goat', 12)
print(f.getInfo())

print(f.getAnimalTypes())
f.getShortInfo()