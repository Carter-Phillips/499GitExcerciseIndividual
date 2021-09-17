
def main():

	sortNumbers()


	return

def sortNumbers():

	numbers = [2, 6,4,2,1,5,7,4,34,745,123,45,3,2]

	print("Unsorted numbers:", numbers)

	numbers.sort()

	print("Sorted numbers:", numbers)

if __name__ == '__main__':
	main()