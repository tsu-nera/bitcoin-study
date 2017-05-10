from event import SignalEvent
from timeseries import TimeSeries

class Manager():
    def __init__(self, status, timeseries):
        # self.execution = execution
        # self.portfolio = portfolio
        self.status = status
        self.ts = timeseries
        # self.strategy = strategy
        self.status["close_time"] = 0

    def perform_trade(self, event):
        # 時系列データに追加
        self.ts.add_tick_event(event)

        # ストラテジチェック
        # self.strategy.calc_indicator(self.ts, event)

        # ストラテジ判定
        # self.check_condition(event, self.strategy)
