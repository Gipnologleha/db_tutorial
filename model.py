from app import db

class Book (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    pages = db.Column (db.Integer, nullable=False)
    book_name = db.Column (db.String(15), nullable=False)
    author = db.Column (db.String(40), nullable=False)

    def __repr__(self):
        return '<Book {}>'.format(self.book_name) 




class Library (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    library_name = db.Column (db.String(45), nullable=False)
    books_quantity = db.Column (db.String(45), nullable=False)
    visitors_quantity = db.Column (db.String(45), nullable=False)