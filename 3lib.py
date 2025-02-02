class Libmanagement:
    def __init__(self):
        self.dict={}
    def details(self,title,author,isbn):
        self.dict[isbn]={'title':title,'author':author}
    def display(self):
        for isbn,book in self.dict.items():
            print(f"title: {book['title']}, author: {book['author']}, ISBN: {isbn}")
title=input('enter the title')
author=input('enter the author')
isbn=int(input('enter isbn'))
c=Libmanagement()
c.details(title,author,isbn)
c.display()
