import unittest

def main():

	sortString()


	return

def sortString():

	strings = ['some', 'string','some other', 'aaaaaaaaaaa']

	print("Unsorted strings:", strings)

	strings.sort()

	print("Sorted strings:", strings)

	return strings

class TestStringSort(unittest.TestCase):
	def testSort(self):
		self.assertEqual(['aaaaaaaaaaa', 'some', 'some other', 'string'], sortString())

if __name__ == '__main__':
	main()
	unittest.main()


