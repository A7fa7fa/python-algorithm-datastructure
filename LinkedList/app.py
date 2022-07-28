from linkedlist import LinkedList

def main():
	myLinkedList = LinkedList()

	for i in range(100):
		myLinkedList.append(i)
	myLinkedList.printList()
	myLinkedList.reverse()
	print("----")
	myLinkedList.printList()

if __name__ == "__main__":
	main()
