#Create classes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Empty")
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.data

def clean(c):
    return "".join(char.lower() for char in c if char.isalnum())

#Checker and reversed for the sentence
def checker(sentence):
    stack = Stack()
    cleaned = clean(sentence)

    for char in cleaned:
        stack.push(char)

    reverse = "".join(stack.pop() for _ in cleaned)

    return cleaned, reverse

#Display function where the ouput of the code will be displayed
def display():

    #Create options, to check and to exit
    while True:
        print("\n\t\t\t\t\tWelcome to Palindrome Checker!")
        print(f"{'=' * 70}")
        print("1. Palindrome Checker")
        print("2. Exit")
        choice = int(input("\nSelect an option (1) Palindrome checker and (2) Exit: "))

        #Ask the user if he/she really wants to exit the program
        if choice == 2:
            exit_choice = input("\nAre you sure you want to exit? (Yes or No): ")
            if exit_choice.lower() == "yes":
                print("Exiting Palindrome Program!!!")
                break
            elif exit_choice.lower() == "no":
                continue

            #Will be displayed if the user input an invalid option
            else:
                print("Invalid Option. Please enter 'Yes' or 'No'")
        elif choice == 1:
            #Asked the user to input a sentence or a word
            sentence = input("\nEnter a sentence or word to check if it is a palindrome or not: ")
            cleaned, reverse = checker(sentence)

            #Will be displayed if the sentence or word is a palindrome or not
            if cleaned == reverse:
                status = "a Palindrome"
            else:
                status = "Not a Palindrome"

            #print all the output
            print(f"{'-' * 70}")
            print("\n\t\t\t\t\t\t\t\tRESULT")
            print(f"{'-' * 70}")
            print("Original Sentence:", sentence)
            print("Cleaned Sentence:", cleaned)
            print("Reversed Sentence:", reverse)
            print(f'The sentence "{sentence}" is {status}.')
        else:
            print("Enter a valid Option!")
display()
