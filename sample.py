import pybitflyer
import json

api = pybitflyer.API()

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

while True:
    data = json.dumps(api.ticker(product_code = "BTC_JPY"))
    data_dict = json.loads(data)
    event = TickEvent(data_dict['product_code'], 
                      data_dict['timestamp'],
                      data_dict['best_bid'],
                      data_dict['best_ask'])
    event.show()
