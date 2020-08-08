from abc import abstractmethod


class EntertainmentStrategy:
    @abstractmethod
    def entertain(self):
        pass


class WatchingTvStrategy(EntertainmentStrategy):
    def entertain(self):
        print('watch tv')


class GoForAWalkStrategy(EntertainmentStrategy):
    def entertain(self):
        print('go for a walk with someone')


class AttendAConcert(EntertainmentStrategy):
    def entertain(self):
        print('attend concert for Amr Diab')


class EntertainmentTime:

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> EntertainmentStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def entertain(self):
        return self._strategy.entertain()


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    entertainmentTime = EntertainmentTime(WatchingTvStrategy())
    entertainmentTime.entertain()
    entertainmentTime.strategy = GoForAWalkStrategy()
    entertainmentTime.entertain()
