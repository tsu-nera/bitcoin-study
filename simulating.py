import matplotlib.pyplot as plt
import queue

# from execution import SimulatedExecutionHandler
from csv_parser import CoinCheckPriceHandler

#from parser import MetatraderCSVPriceHandler
# from portfolio import PortfolioLocal
from progressbar import ProgressBar
from timeseries import TimeSeries
from manager import Manager

def simulating(events, manager):
    p = ProgressBar()

    for i in p(range(events.qsize())):
        # キューからTickEvent取り出し
        event = events.get(False)

        # トレード実行
        manager.perform_trade(event)

        # 最後は決済して終了
        # check_and_close_last_order(event)

        p.update(i + 1)


# def check_and_close_last_order(event):
#     if events.empty():
#         if status["position"] < 0:
#             manager.order_and_calc_portfolio(event, True, True)
#         else:
#             manager.order_and_calc_portfolio(event, False, True)


# def show_result():
#     print("Total Order Count: %s" % portfolio.order_count)
#     print("Realized P&L     : %s" % round(status["realized_pnl"], 5))
#     print("win and lose     : %s / %s"
#          %(portfolio.win_count, portfolio.lose_count))
    # print("Profit Factor    : %s" % round(
    #     portfolio.total_profit/portfolio.total_loss, 5))
    # print("Profit/Loss      : %s/%s" % (
    #     portfolio.total_profit, portfolio.total_loss))


def plot_data(timeseries):
    plt.plot(timeseries.prices.index, timeseries.prices)

    # plt.plot(strategy.sma_long_ts.index, strategy.sma_long_ts)
    # plt.plot(strategy.sma_short_ts.index, strategy.sma_short_ts)
    # plt.plot(strategy.sma_ols_ts.index, strategy.sma_ols_ts)

    # plt.plot(strategy.knn_ts.index, strategy.knn_ts)

    # if not len(timeseries.buys) == 0:
    #     plt.plot(timeseries.buys.index, timeseries.buys, "g^", markersize=8)
    # if not len(timeseries.sells) == 0:
    #     plt.plot(timeseries.sells.index, timeseries.sells, "rv", markersize=8)
    # if not len(timeseries.close_wins) == 0:
    #     plt.plot(timeseries.close_wins.index, timeseries.close_wins, "yo", markersize=8)
    # if not len(timeseries.close_loses) == 0:
    #     plt.plot(timeseries.close_loses.index, timeseries.close_loses, "mo", markersize=8)

    # portfolio.rpnl.plot()

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    events = queue.Queue()  # 同期キュー

    status = dict()  # tick をまたいで記憶しておきたい情報
    status["is_sim"] = True

#    portfolio = PortfolioLocal(status)

#    execution = SimulatedExecutionHandler(status)

    timeseries = TimeSeries()

#    strategy = OLSTIME(status)    
#    strategy = SMAKNN(status)
#    strategy = MARTINRSI(status)
#    strategy = SMABOLPIPRSI(status)
#    strategy = SMABOLPIP(status)    
#    strategy = SMAPIP(status)
#    strategy = SMAPIPRSI(status)
#    strategy = SMAOLSPIP(status)
#    strategy = SMABOL(status)
#    strategy = SMARSIOLS(status)
#    strategy = WMA(status)
#    strategy = SMAOLS(status)
#    strategy = SMA(status)
#    strategy = RSI(status)
#    strategy = SMARSI(status)
#    strategy = Granville(status)
#    strategy = Momentum(status)
#    strategy = BolingerBand(status)

    manager = Manager(status, timeseries)

    print("=== Backtesting Start =================================== ")
    
    event_src = CoinCheckPriceHandler(events, "data/trades_coincheckJPY2.csv")
    event_src.stream_to_queue()

    simulating(events, manager)
    print("=== End .... v(^_^)v  =================================== ")

    # show_result()
    plot_data(timeseries)
