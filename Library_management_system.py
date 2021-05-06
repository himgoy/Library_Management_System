def listToUpperCase(inputList):
    return [x.upper() for x in inputList]


class Library:

    def __init__(self, listofbooks, lib_name):
        self.bookList = listToUpperCase(listofbooks)
        self.name = lib_name
        self.lendDict = {}

    def display_book(self):
        print(f"These are the following Books in our library : ")
        for books in self.bookList:
            print(books)

    def lend_book(self, user, book):
        if book in self.bookList:
            self.bookList.remove(book)
            self.lendDict.update({book: user})
            print("Book has been given to you")
            pass
        else:
            if self.lendDict.get(book) is None:
                print(f"Sorry!, the book you requested is not present in the library")
            else:
                print(
                    f"{self.lendDict.get(book)} currently have the book you Need, So kindly wait for it to be Returned")

    def add_book(self, book_name):
        self.bookList.append(book_name)
        self.bookList = listToUpperCase(self.bookList)
        print("Book has been added to the Library")

    def return_book(self, book):
        self.bookList.append(book)
        self.lendDict.pop(book)
        print("The book has been safely Returned")


def main():
    book_list = ['Aarushi Agarwal', 'Mehul Agarwal', 'Niharika Agarwal', 'Hitesh Goyal']
    name_lib = "HIMGOY's BookStore"

    lib = Library(book_list, name_lib)

    while True:
        print(f"\nWelcome to {lib.name}. Choose a relevant option\n"
              f"Press 1 to Display Books in Store\n"
              f"Press 2 to Lend a Book from Store\n"
              f"Press 3 to Return a lent Book\n"
              f"Press 4 to Donate/Add Book to the Store\n"
              f"Press 5 to Exit()")

        try:
            userchoice = int(input())
            if userchoice == 1:
                lib.display_book()

            elif userchoice == 2:
                book = input("Enter Book name : ")
                user = input("Enter your name : ")
                lib.lend_book(user, book.upper())

            elif userchoice == 3:
                book = input("Enter Book name : ")
                lib.return_book(book)

            elif userchoice == 4:
                book = input("Enter Book name : ")
                lib.add_book(book)

            elif userchoice == 5:
                break

            else:
                print("Invalid choice!, Select again\n")
                continue

        except Exception as e:
            print(f"An ERROR came, Kindly look into it\n"
                  f"{e}")


if __name__ == '__main__':
    main()
