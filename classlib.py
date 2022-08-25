class Library:
    def __init__(self,name,address,phone_number):
             self.name=name
             self.address=address
             self.phone_number=phone_number
             self.books=[]
    def book_taken(self,book):
        self.books.append(book)
    def book_returned(self,book):
        self.books.remove(book)
    def display(self):
        print(self.name,self.address,self.phone_number)
        print("Books")
        print(self.books)
obj=Library("ASWATHI","KOZHIKODE","9876543210")
obj.book_taken("python")
obj.display()
obj.book_taken("java")
obj.display()
obj.book_taken("css")
obj.display()
obj.book_returned("python")
obj.display()



