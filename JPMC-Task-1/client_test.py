import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (quote.get('top_ask').get('price') + quote.get('top_bid').get('price'))/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote.get('stock'), quote.get('top_bid').get('price'),
                                              quote.get('top_ask').get('price'), (quote.get('top_ask').get('price') +
                                                                                 quote.get('top_bid').get('price'))/2))

  def test_getRatio(self):
    price_a = [0, 1, 2, 5, 3, 1, 2]
    price_b = [3, 1, 2, 0, 6, 3, 1]
    correct = [0, 1, 1, None, 0.5, 0.3333333333333333, 2]
    for val in range(len(price_b)):
        result = getRatio(price_a[val], price_b[val])
        self.assertEqual(result, correct[val])


if __name__ == '__main__':
    unittest.main()
