
import os
import unittest
import json
import apicem_1

class Coding102TestCase(unittest.TestCase):

	def setUp(self):

		self.app = apicem_1

	def tearDown(self):

		print("tear down")

	def test_hello(self):

		result = self.app.hello()
		self.assertTrue(result is not None)

if __name__ == '__main__':
	unittest.main()
