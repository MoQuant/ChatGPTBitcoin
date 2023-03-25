import requests
import matplotlib.pyplot as plt

url = 'https://api.pro.coinbase.com/products/BTC-USD/book?level=2'

response = requests.get(url)

if response.status_code == 200:
    book = response.json()
    bids = book['bids'][:5]
    asks = book['asks'][:5]

    cumulative_bid_volume = [sum([float(bid[1]) for bid in bids[:i+1]]) for i in range(len(bids))]
    cumulative_ask_volume = [sum([float(ask[1]) for ask in asks[:i+1]]) for i in range(len(asks))]

    bids_prices = [float(bid[0]) for bid in bids]
    asks_prices = [float(ask[0]) for ask in asks]

    reversed_bids = bids[::-1]
    reversed_bids_prices = bids_prices[::-1]
    reversed_cumulative_bid_volume = cumulative_bid_volume[::-1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
    fig.suptitle('Orderbook Summary', fontsize=16)

    ax1.plot(reversed_bids_prices, reversed_cumulative_bid_volume, color='blue')
    ax1.set_title('Cumulative Bid Volume vs. Bid Prices')
    ax1.set_xlabel('Bid Prices')
    ax1.set_ylabel('Cumulative Bid Volume')

    ax2.plot(asks_prices, cumulative_ask_volume, color='red')
    ax2.set_title('Cumulative Ask Volume vs. Ask Prices')
    ax2.set_xlabel('Ask Prices')
    ax2.set_ylabel('Cumulative Ask Volume')

    plt.show()
else:
    print("Failed to retrieve Level 2 orderbook from Coinbase Pro")
