import unittest

def sortNumbers():

	numbers = [2, 6,4,2,1,5,7,4,34,745,123,45,3,2]

	print("Unsorted numbers:", numbers)

	numbers.sort()

	print("Sorted numbers:", numbers)

def sortString():

	strings = ['some', 'string','some other', 'aaaaaaaaaaa']

	print("Unsorted strings:", strings)

	strings.sort()

	print("Sorted strings:", strings)

	return strings

class TestStringSort(unittest.TestCase):
	def testSortNumbers(self):
		self.assertEqual([1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 34, 45, 123, 745], sortNumbers())
	def testSortStrings(self):
		self.assertEqual(['aaaaaaaaaaa', 'some', 'some other', 'string'], sortString())



if __name__ == '__main__':
	unittest.main()

	