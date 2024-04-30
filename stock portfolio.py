import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                total_value += price * quantity
        return total_value

    def get_stock_price(self, symbol):
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'Global Quote' in data:
                return float(data['Global Quote']['05. price'])
        return None

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price:
                print(f"{symbol}: Quantity - {quantity}, Price - ${price:.2f}, Total Value - ${price * quantity:.2f}")
            else:
                print(f"{symbol}: Quantity - {quantity}, Price - Unknown")

# Example usage
if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.display_portfolio()
    print("Total Portfolio Value:", portfolio.get_portfolio_value())
