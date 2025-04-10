import unittest, requests

class InventoryApiTestCase(unittest.TestCase):

    def test_get_all(self):
        url = 'http://localhost:8000/getAll'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_product(self):
        url = 'http://localhost:8000/getSingleProduct?id=AUTO0001'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_add_new(self):
        url = 'http://localhost:8000/addNew?ProductID=TEST9999&Name=TestProduct&UnitPrice=12.99&StockQuantity=10&Description=Test+Product'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_delete_one(self):
        url = 'http://localhost:8000/deleteOne?id=TEST9999'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_starts_with(self):
        url = 'http://localhost:8000/startsWith?letter=A'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_paginate(self):
        url = 'http://localhost:8000/paginate?start=AUTO0001&end=AUTO0010'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_convert(self):
        url = 'http://localhost:8000/convert?id=AUTO0001'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
   with open("test_results.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)