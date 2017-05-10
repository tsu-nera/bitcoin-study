from event import TickEvent
import pandas as pd
from datetime import datetime
import queue

class CoinCheckPriceHandler():
    def __init__(self, events_queue=queue.Queue(), file_path=None):
        self.events_queue = events_queue
        self.file_path = file_path
        self.data = []
        self.dt_format = "%Y-%m-%d %H:%M:%S"

    def stream_to_queue(self):
        self._open_convert_csv_files()
        for index, row in self.data.iterrows():
            posix_time = row["UnixTime"]
            time = datetime.utcfromtimestamp(posix_time).strftime(self.dt_format)
            event = TickEvent("BTC_JPY", time,
                              float(row["Price"]), float(row["Price"]))
            self.events_queue.put(event)

    def _open_convert_csv_files(self):
        self.data = pd.read_csv(self.file_path,
                                names=("UnixTime","Price","Amount"))
        self.data = self.data.sort_values(by='UnixTime')

if __name__ == '__main__':
    parser = CoinCheckPriceHandler(file_path="data/trades_coincheckJPY.csv")
    parser.stream_to_queue()
