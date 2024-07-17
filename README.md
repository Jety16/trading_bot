
# Trade Bot

Trade Bot is a Python application that helps users make informed stock trading decisions using the moving average crossover strategy. The bot fetches stock data from the [Alpha Vantage](https://www.alphavantage.co/) API, calculates short-term and long-term moving averages, and provides buy/sell/hold recommendations based on the signals generated.

## Features

- Fetches weekly stock data using the Alpha Vantage API
- Calculates short-term and long-term moving averages
- Generates trading signals based on moving average crossovers
- Provides buy, sell, or hold recommendations
- Allows users to check specific stocks or multiple stocks at once

## Prerequisites

- Python 3.x
- An Alpha Vantage API key (you can get one by signing up [here](https://www.alphavantage.co/support/#api-key))

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/trade_bot.git
cd trade_bot
```
2. Create a virtual environment and activate it:
```sh
python3 -m venv .venv
source .venv/bin/activate
```
3. Install the required packages:

```sh

pip install -r requirements.txt
```
4. Set up your Alpha Vantage API key:

```sh
export STOCK_API_KEY='your_api_key'
```

## Usage

Run the Trade Bot:

```sh
    python3 trade_bot.py
```
- Follow the on-screen prompts:

- Check specific stock: Enter a single stock symbol to get a recommendation.
- Get all your stock data: Enter multiple stock symbols separated by commas to get recommendations for each.

## Project Structure
```sh
    trade_bot.py: Main script to run the Trade Bot.
    stock.py: Contains the Stock class that handles fetching and processing stock data.
    requirements.txt: Lists the required Python packages.
```