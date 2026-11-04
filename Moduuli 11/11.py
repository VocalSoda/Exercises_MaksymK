

class Book():
    
    def __init__(self, name, author, pages):
        
        self.name = name
        self.author = author
        self.pages = pages
        
    def print_info(self):
        
        print(self.name)
        print(self.author)
        print(self.pages)

            

class Magazine():
    
    def __init__(self, name, author):
        
        self.name = name
        self.author = author
        
    def print_info(self):
        
        print(self.name)
        print(self.author)
        
        

magazine = Magazine("Aku Ankka", "Aki Hyyppä")
book = Book("Hytti n:o 6", "Rosa Liksom", 200)

magazine.print_info()

print()

book.print_info()     
        
     