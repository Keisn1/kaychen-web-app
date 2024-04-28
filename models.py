from kaychen.orm import Table, Column


class Book(Table):
    author = Column(str)
    name = Column(str)
