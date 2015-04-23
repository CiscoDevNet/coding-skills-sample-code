
import os
import unittest
import json

class Coding102TestCase(unittest.TestCase):

	def setUp(self):

		print("set up")

	def tearDown(self):

		print("tear down")

	def test_hello(self):
		
		self.assertTrue(1)

if __name__ == '__main__':
	unittest.main()
