class Person:
    """Create a new person"""
    def __init__(self, f_name, l_name):  # self parameter is reference to the current instance of the class
        self.f_name = f_name
        self.l_name = l_name

    def new(self):
        print("Hi, my name is " + self.f_name)
        print("Hi, my last name is " + self.l_name)


class Player(Person):
    def __init__(self, f_name, l_name, total):
        Person.__init__(self, f_name, l_name)
        self.total = total

    def get_details(self):
        return "%s %s has spent %s in total" % (self.f_name, self.l_name, self.total)


new_person = Person("Johnny", "English")
print(new_person)
print(new_person.f_name)
print(new_person.l_name)
new_person.new()
new_player = Player("Leo", "Messi", 2000)
print(new_player.get_details())


class Enemy:
    life = 3

    def attack(self):
        print("ouch")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
