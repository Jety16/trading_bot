from datetime import datetime, timezone
import os
import requests
import pandas as pd

class Stock():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.last_update = datetime.now(timezone.utc)
        self.api_key = os.environ.get("STOCK_API_KEY")
        self.to_buy = False
        self.to_sell = False

    def _get_data(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={self.id}&apikey={self.api_key}'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if "Weekly Time Series" in data:
                return data["Weekly Time Series"]
            else:
                print("Error: 'Weekly Time Series' not found in response")
        else:
            print(f"Error: API request failed with status code {r.status_code}")
        return None

    def _moving_average(self, data, window_size):
        return data.rolling(window=window_size).mean()

    def _generate_signals(self, prices, short_window, long_window):
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['short_mavg'] = self._moving_average(prices, short_window)
        signals['long_mavg'] = self._moving_average(prices, long_window)
        signals['signal'] = 0

        signals['signal'][short_window:] = (
            (signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:]).astype(int) -
            (signals['short_mavg'][short_window:] < signals['long_mavg'][short_window:]).astype(int)
        )
        signals['positions'] = signals['signal'].diff()
        return signals

    def _evaluate_signals(self, signals):
        last_signal = signals['signal'].iloc[-1]
        if last_signal > 0:
            return "Buy"
        elif last_signal < 0:
            return "Sell"
        else:
            return "Hold"

    def update_stock(self):
        weekly_data = self._get_data()
        if weekly_data:
            # Extract the close prices
            prices = pd.Series({datetime.strptime(date, '%Y-%m-%d'): float(data['4. close']) for date, data in weekly_data.items()})
            prices = prices.sort_index()

            # Filter data for the current year
            current_year = datetime.now().year
            prices = prices[prices.index.year == current_year]

            # Define short and long window sizes
            short_window = 5
            long_window = 20

            # Generate signals and evaluate
            signals = self._generate_signals(prices, short_window, long_window)
            decision = self._evaluate_signals(signals)

            # Update the stock's buy/sell recommendation
            if decision == "Buy":
                self.to_buy = True
                self.to_sell = False
            elif decision == "Sell":
                self.to_buy = False
                self.to_sell = True
            else:
                self.to_buy = False
                self.to_sell = False

            print(f"The recommendation for {self.name} is to: {decision}")
            print(signals)
        else:
            print("Failed to retrieve data for the stock.")

# Example usage
stock = Stock(id="IBM", name="IBM")
stock.update_stock()
