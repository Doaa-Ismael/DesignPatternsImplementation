from abc import abstractmethod


class Furniture:

    @abstractmethod
    def show(self):
        print('show colorful furniture')


class NewFurniture(Furniture):
    def show(self):
        print('show colorful furniture')


class OldFurniture(Furniture):
    def show(self):
        print('show gold furniture')


class Home:

    @abstractmethod
    def create_furniture(self):
        pass

    def show_furniture(self):
        furniture = self.create_furniture()
        return furniture.show()


class NewHome(Home):
    def create_furniture(self):
        return NewFurniture()


class OldHome(Home):
    def create_furniture(self):
        return OldFurniture()


if __name__ == "__main__":

    home = OldHome()
    home.show_furniture()