from data import *
from strategies import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv


class Simulation:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def run_simulation(self):
        results = self.strategy.strategy()
        total_profits = 0

        positive_trades_count = 0
        for result in results:
            total_profits += result
            if result >= 0:
                positive_trades_count += 1

        win_rate = positive_trades_count / len(results) * 100
        return f"Profits: {total_profits}, Winrate: {win_rate}, Number of trades: {len(results)}"

    @staticmethod
    def change_dates_by_a_month(start_date : str, end_date : str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        current_date = start_date
        all_dates = []

        while current_date <= end_date:
            all_dates.append(current_date.strftime("%Y-%m-%d"))
            current_date += relativedelta(months=1)

        return all_dates

    @staticmethod
    def write_CSV(file_name: str, start_period: str, end_period: str, percentage_gain: int, risk_reward_ratio: int, ticker: str):
        with open(file_name, "a") as f:
            dates = Simulation.change_dates_by_a_month(start_period, end_period)
            i = 0
            while i < len(dates) - 1:
                start_date = dates[i]
                end_date = dates[i + 1]
                data = Data(
                    ticker=ticker,
                    timespan="minute",
                    start_date=start_date,
                    end_date=end_date,
                    multiplier=5,
                    sort="asc",
                    limit=50000,
                )
                csv.writer(f, delimiter=",").writerow([f"From {start_date} to {end_date}", Simulation(Hammer(data, percentage_gain, risk_reward_ratio)).run_simulation()])
                i += 1



