from random import randint


class Frame:
    def __init__(self):
        self.num_pins_dropped = 0
        self.delivery_1 = None
        self.delivery_2 = None
        self.strike = False
        self.spare = False

    def deliver(self):
        self.delivery_1 = randint(0, 10)

        # if strike
        if self.delivery_1 == 10:
            self.strike = True
            self.num_pins_dropped = 10
            return
        else:
            self.delivery_2 = randint(
                0, 10 - self.delivery_1)
            if self.delivery_2 == 10 - self.delivery_1:
                self.spare = True
                self.num_pins_dropped = 10
                return
            else:
                self.num_pins_dropped = self.delivery_1 + self.delivery_2
