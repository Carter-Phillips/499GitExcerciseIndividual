
def main():

	sortString()


	return

def sortString():

	string = ['some', 'string','some other', 'aaaaaaaaaaa']

	print("Unsorted strings:", string)

	string.sort()

	print("Sorted strings:", string)

if __name__ == '__main__':
	main()