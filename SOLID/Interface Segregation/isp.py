"""
Sumary

The goal here is you don't really want to many elements and methods into an interface.

Making interfaces which feature too many elements is not a good idea because you are forcing your clients to define and implment methods and properties which they might not even need.

"""

from abc import abstractmethod


class Printer:
    @abstractmethod
    def print(self, document): print(document)

class Fax:
    @abstractmethod
    def sed_fax(self, document): print(document)

class Scanner:
    @abstractmethod
    def scan(self, document): print(document)


class MultiFunctionMachine(Printer, Scanner, Fax):

    def print(self, document):
        Printer.print(self, document)

    def scan(self, document):
        Scanner.scan(self, document)

    def sed_fax(self, document):
        Fax.sed_fax(self, document)

mf = MultiFunctionMachine()
mf.print(document="this is a print")
mf.scan(document="this is a scan")
mf.sed_fax(document="this is a fax")
