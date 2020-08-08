from abc import abstractmethod


class Furniture:

    def __init__(self, home_type):
        self._home_type = home_type

    def show(self):
        if self._home_type == 'new':
            print('show colorful furniture')
        else:
            print('show gold furniture')


class NewHome:
    def show_furniture(self):
        furniture = Furniture('new')
        return furniture.show()


class OldHome:
    def show_furniture(self):
        furniture = Furniture('old')
        return furniture.show()


if __name__ == "__main__":

    home = NewHome()
    home.show_furniture()