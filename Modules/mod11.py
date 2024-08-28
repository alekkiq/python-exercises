# the 2. part of this module modifies the 


# 1
class Release:
    def __init__(self, name: str = ""):
        self.name = name
        
class Book(Release):
    def __init__(self, name: str = "", author: str = "", pages: int = 0):
        self.author = author
        self.pages = pages
        super().__init__(name)
        
    def get_information(self):
        return print(f"Book '{self.name}', author: '{self.author}', number of pages: {self.pages}")
        
class Paper(Release):
    def __init__(self, name: str = "", chief_reporter: str = ""):
        self.chief_reporter = chief_reporter
        super().__init__(name)
    
    def get_information(self):
        return print(f"Paper '{self.name}', chief reporter: '{self.chief_reporter}'")

def releases_main():
    releases = [
        Paper("Aku Ankka", "Aki Hyyppä"),
        Book("Hytti n:o 6", "Rosa Liksom", 200)
    ]
    
    for release in releases:
        release.get_information()
        
#   releases_main()
