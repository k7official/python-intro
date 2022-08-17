def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


#add_numbers(3, 6)
#add_numbers(34, 4, 6, 7, 9)

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        print(type(kwargs.items()))
        for k, v in kwargs.items():
            while v:
                self.contents.append(k)
                v -= 1
        print(self.contents)

hat1 = Hat(yellow=3, blue=2, green=6)
