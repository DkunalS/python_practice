def addBook():
    title = input("Enter the Title: ")
    author = input("Enter the Author: ")
    genre = input("Enter the Genre: ")
    year = input("Enter the Year: ")
    add_list.append(author)
    add_list.append(genre)
    add_list.append(year)
    bookCollection[title] = add_list
    print(f"{title} Book is added into Book Collection")
    print(f"Book details are {bookCollection}\n")

def search():
    searchItem = input("Search the book by Genre or Author Name: ")
    if searchItem in bookCollection.values():
        print(f"{searchItem} Book is present in the Book Collection!!")
        print(f"Book details are {bookCollection[searchItem]}\n")

    else:
        print(f"{search} Book is not exist in the Book Collection!!\n")

def delete():
    title = input("Enter the Book title you want to delete: ")
    bookCollection.pop(title)
    print(f"{title} Book is deleted from the Book Collection!!\n")

bookCollection ={}
add_list = []
while True:
    choice = int(input("""Enter the operation you want to perform
    1. Add Book
    2. Search Book
    3. Remove Book
    4. Exit \n"""))
    match choice:
        case 1:
            addBook()
        case 2:
            search()
        case 3:
            deleteBook()
        case 4:
            print("Exited Successfully!!")
            break
        case _:
            print("You have entered wrong input\n")