import pandas as pd

def _moving_average(data, window_size):
    return data.rolling(window=window_size).mean()

def _generate_signals(prices, short_window, long_window):
    signals = pd.DataFrame(index=prices.index)
    signals['price'] = prices
    signals['short_mavg'] = _moving_average(prices, short_window)
    signals['long_mavg'] = _moving_average(prices, long_window)
    signals['signal'] = 0

    signals['signal'][short_window:] = (
        (signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:]).astype(int) -
        (signals['short_mavg'][short_window:] < signals['long_mavg'][short_window:]).astype(int)
    )
    signals['positions'] = signals['signal'].diff()
    return signals

def _evaluate_signals(signals):
    last_signal = signals['signal'].iloc[-1]
    if last_signal > 0:
        return "Buy"
    elif last_signal < 0:
        return "Sell"
    else:
        return "Hold"


def get_moving_average_result(data=None):
    # Example usage
    # Simulated monthly price data for a stock
    price_data = pd.Series(
        [150, 152, 153, 155, 158, 160, 162, 161, 159, 158, 157, 156, 154, 152, 151, 150, 149, 148, 147, 145, 144, 143, 142, 140, 139, 138, 137, 136, 135, 134],
        index=pd.date_range(start='2023-05-01', periods=30, freq='D')
    )

    short_window = 5
    long_window = 20

    signals = _generate_signals(price_data, short_window, long_window)
    decision = _evaluate_signals(signals)
    print(f"The recommendation is to: {decision}")

    # Optionally print the signals DataFrame for inspection
    print(signals)

print(get_moving_average_result())