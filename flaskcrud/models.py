from . import db


books_authors = db.Table(
    'books_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'Author: {self.name}'


# Region Models
class Publishers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(60), nullable=True)
    state = db.Column(db.String(30), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    website = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return F'Editorial: {self.name}'
    

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    authors = db.relationship('Authors', secondary=books_authors, backref=db.backref('books', lazy=True))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))
    publisher = db.relationship('Publishers', backref=db.backref('books', lazy=True))
    pub_date = db.Column(db.Date)

    def __repr__(self):
        return F'Libro: {self.title}'
    
# END Region Models

