import threading
import time
import queue

from streaming import StreamingPrices
from manager import Manager
from timeseries import TimeSeries

heartbeat = 0.5

def on_tick(events, manager):
    while True:
        try:
            event = events.get(False)
        except queue.Empty:
            pass
        else:
            manager.perform_trade(event)
        time.sleep(heartbeat)

if __name__ == "__main__":
    events = queue.Queue()
    timeseries = TimeSeries()

    price_src = StreamingPrices(events)

    status = dict() 
    status["is_sim"] = False

    manager = Manager(status, timeseries)

    trade_thread = threading.Thread(target=on_tick,
                                    args=[events, manager])

    price_thread = threading.Thread(target=price_src.begin)

    trade_thread.start()
    price_thread.start()
