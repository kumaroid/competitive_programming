from threading import Lock

class DiningPhilosophers:
    def __init__(self) -> None:
        self.locks = [Lock() for _ in range(5)]


    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

                   
        next_phil = (philosopher + 1) % 5


        self.locks[(philosopher + (philosopher %2)) % 5].acquire()
        self.locks[(philosopher + ((philosopher + 1) %2 )) % 5].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.locks[(philosopher + (philosopher %2)) % 5].release()
        self.locks[(philosopher + ((philosopher + 1) %2 )) % 5].release()
