from Classes.Release import Release

class Book(Release):
    def __init__(self, name: str, author: str, pages: int = 0):
        self.author = author
        self.pages = pages
        super().__init__(name)
        
    def get_information(self):
        return print(f"Book '{self.name}', author: '{self.author}', number of pages: {self.pages}")
        
