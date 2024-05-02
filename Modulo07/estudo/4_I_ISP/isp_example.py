# SOLID - Interface Segragation Principle (ISP)

# pdf, txt, excel

from abc import ABC, abstractmethod


class Document(ABC):  # generic
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass


class DocumentPDF(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTXT(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel(ABC):  # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass
