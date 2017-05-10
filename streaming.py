from coincheck import market
import json
import queue
from datetime import datetime

from event import TickEvent

class StreamingPrices():
    def __init__(self, event_queue, api_key = None, api_secret = None):
        self.event_queue = event_queue
        self.api = market.Market()
        self.dt_format = "%Y-%m-%d %H:%M:%S"

    def begin(self):
        while True:
            data = json.dumps(self.api.ticker())
            dict_data = json.loads(data)
            time, symbol, bid, ask = self.parse_tick_data(dict_data)
            event = TickEvent(symbol, time, bid, ask)
            self.event_queue.put(event)

    def parse_tick_data(self, dict_data):
        posix_time = dict_data["timestamp"]
        time = datetime.utcfromtimestamp(posix_time).strftime(self.dt_format)
        instrument = "BTC_JPY"
        ask = float(dict_data["ask"])
        bid = float(dict_data["bid"])
        return time, instrument, bid, ask

if __name__ == '__main__':
    prices = StreamingPrices(queue.Queue())
    prices.begin()
