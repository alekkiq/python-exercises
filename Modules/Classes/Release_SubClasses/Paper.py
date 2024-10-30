from Classes.Release import Release

class Paper(Release):
    def __init__(self, name: str, chief_reporter: str):
        self.chief_reporter = chief_reporter
        super().__init__(name)
    
    def get_information(self):
        return print(f"Paper '{self.name}', chief reporter: '{self.chief_reporter}'")
