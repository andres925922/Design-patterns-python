"""
Sumary

Also called separation of concerns.

A class should have it primary responsability whatever its meant to be doing and it should not take any aditional responsabilities

You do not want to overload your objects with too many responsabilities

Antipattern -> God object -> Massive class

"A class should have a single reason to change and that change should be somehow related to its primary responsability.

"""

class Journal():

    def __init__(self) -> None:
        self.entries: list = []
        self.counter: int = 0

    def add_entry(self, entry: str):
        self.counter += 1
        self.entries.append(entry)

    def remove_entry(self, pos: int):
        self.counter -= 1
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)
    

class Journal_Persitence_Manager():

    @staticmethod
    def persist_journal(
        filename: str, 
        journal: Journal
    ):
        """ Persistence methodes must be in an other class """
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Hello there")
j.add_entry("General Kenobi")

print(j)

file = r"C:\Users\andre\Documents\GitHub\Design-patterns-python\SOLID\SRP\test"
Journal_Persitence_Manager.persist_journal(file, j)

with open(file) as file_handler:
    print(file_handler.read())