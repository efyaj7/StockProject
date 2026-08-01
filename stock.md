# Stock Portfolio Tracker

A command-line portfolio tracker built in Python. It lets you buy and sell
stocks with real market data (via `yfinance`), tracks your cash balance,
and shows profit/loss on each position as prices move.

> **Note on scope:** this is currently a *portfolio tracker*, not a *stock
> picker* — it records and values trades you've already decided to make,
> rather than helping you decide what to buy. See "Roadmap" below for where
> it's headed.

## Features

- **Add Stock** — buy shares of any valid ticker (including indices like
  `^GSPC` and multi-part symbols like `BRK.B` or `BTC-USD`). Buying more of
  a stock you already own merges it into the existing position with a
  weighted-average cost.
- **Sell Stock** — sell part or all of a position.
- **Refresh Price** — re-fetch the latest price for every stock you hold.
- **View Portfolio** — prints a table of all holdings (ticker, shares,
  purchase price, current price, profit/loss, % return), plus your cash
  balance and total net worth. Also saves a chart to `portfolio.png`.

## How prices work

Since `yfinance` isn't a real-time feed, this project simulates a simple
"you bought a few days ago" scenario:

- **`purchase_price`** — the closing price from ~3 trading days ago
  (`fetch_historical_price`), used as the cost basis when you buy.
- **`current_price`** — today's most recent close (`fetch_price`), used for
  valuing your position and for profit/loss.

## Architecture

Roughly MVC:

| Layer | File | Responsibility |
|---|---|---|
| Model | `Stock.py` | A single holding — shares, prices, and the profit/loss/percentage/value math. No I/O. |
| Data access | `data.py` (`DataManager`) | Talks to `yfinance`, reads/writes `portfolio.json`. |
| Controller | `Portfolio.py` | Orchestrates buys/sells/refreshes — fetches data via `DataManager`, updates `Stock` objects, persists state. |
| View | `main.py` | The CLI menu loop — all user input/output. |

## Data persistence

Portfolio state (cash + holdings) is stored in `portfolio.json`, rewritten
in full on every trade. There's no transaction history yet — only current
state.

## Requirements

- `yfinance`
- `pandas`
- `matplotlib`

## Running it

```
python main.py
```

## Known limitations / Roadmap

**Bugs to fix:**
- `remove_stock` computes sale proceeds off the full holding instead of the
  number of shares actually sold.
- Selling an entire position leaves a zero-share entry behind instead of
  removing it.
- No guard against selling a stock whose `current_price` is still unset.

**Cleanup:**
- Unused Alpha Vantage API key in `DataManager`.
- Broad `except` in `data.py` treats every failure (network error, bad
  ticker, rate limit) identically.
- No validation against zero/negative share counts.
- Redundant price fetches on every purchase.

**Planned features:**
- Transaction history (log of every buy/sell, not just current state).
- A watchlist, separate from owned positions.
- Simple screening rules to compare candidate tickers against each other —
  the first step toward being an actual stock *picker*.
