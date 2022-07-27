from linkedlist import LinkedList

def main():
	myLinkedList = LinkedList()

	myLinkedList.append(4)
	myLinkedList.printList()
	myLinkedList.remove(0)
	print("----")
	myLinkedList.printList()

if __name__ == "__main__":
	main()
