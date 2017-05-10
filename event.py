class Event(object):
    pass

class TickEvent(Event):
    def __init__(self, instrument, time, bid, ask):
        self.type = 'TICK'
        self.instrument = instrument
        self.time = time
        self.bid = bid
        self.ask = ask

    def show(self):
        print("instrument:" + self.instrument +
              ", time:" + self.time +
              ", bid:" + str(self.bid) +
              ", ask:" + str(self.ask))

class SignalEvent(Event):
    def __init__(self, instrument, time, order_type, side, price):
        self.type = 'SIGNAL'
        self.instrument = instrument
        self.time = time
        self.order_type = order_type
        self.side = side
        self.price = price
