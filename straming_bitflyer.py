import pybitflyer
import json
import queue
from datetime import datetime

from event import TickEvent

class StreamingPrices():
    def __init__(self, event_queue, api_key = None, api_secret = None):
        self.event_queue = event_queue
        self.api = pybitflyer.API(api_key, api_secret)
        self.dt_format = "%Y-%m-%dT%H:%M:%S.%f"

    def begin(self, instruments="BTC_JPY"):
        while True:
            data = json.dumps(self.api.ticker(product_code = instruments))
            dict_data = json.loads(data)
            time, symbol, bid, ask = self.parse_tick_data(dict_data)
            event = TickEvent(symbol, time, bid, ask)
            self.event_queue.put(event)

    def parse_tick_data(self, dict_data):
        time = datetime.strptime(dict_data["timestamp"], self.dt_format)
        #time = dict_data["timestamp"]
        instrument = dict_data["product_code"]
        ask = float(dict_data["best_ask"])
        bid = float(dict_data["best_bid"])
        return time, instrument, bid, ask

if __name__ == '__main__':
    prices = StreamingPrices(queue.Queue())
    prices.begin()
