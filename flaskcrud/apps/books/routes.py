from flask import Blueprint, render_template, redirect, url_for, flash

# Modelos
from ...models import Books, Authors, Publishers

# Forms
from ...forms import BookForm

# DB
from flaskcrud import db


books_bp = Blueprint('books', __name__, url_prefix='/books')

def get_authors_and_publishers():
    authors = Authors.query.all()
    publishers = Publishers.query.all()
    return authors, publishers

@books_bp.route('/')
def list_books():
    books = Books.query.all()
    return render_template('books/list.html', books=books)


@books_bp.route('/add-book/', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    authors, publishers = get_authors_and_publishers()
    form.authors.choices = [(author.id, f'{author.name} {author.lastname}') for author in authors]
    form.publisher_id.choices = [(publisher.id, publisher.name) for publisher in publishers]

    if form.validate_on_submit():
        book = Books(
            title=form.title.data,
            pub_date=form.pub_date.data,
            publisher_id=form.publisher_id.data
        )
        selected_author_ids = form.authors.data
        selected_authors = Authors.query.filter(Authors.id.in_(selected_author_ids)).all()
        book.authors.extend(selected_authors)
        db.session.add(book)
        db.session.commit()
        flash('El libro ha sido añadido correctamente.', 'success')
        return redirect(url_for('books.list_books'))

    return render_template('books/form.html', title="Añadir Libro", form=form)


@books_bp.route('/delete-book/<int:book_id>')
def delete_book(book_id):
    book = Books.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('El libro ha sido eliminado correctamente.', 'success')
    return redirect(url_for('books.list_books'))


@books_bp.route('/edit-book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Books.query.get_or_404(book_id)
    form = BookForm(obj=book)
    authors, publishers = get_authors_and_publishers()
    form.authors.choices = [(author.id, author.name) for author in authors]
    form.publisher_id.choices = [(publisher.id, publisher.name) for publisher in publishers]

    if form.validate_on_submit():
        book.title = form.title.data
        book.pub_date = form.pub_date.data
        book.publisher_id = form.publisher_id.data
        selected_author_ids = form.authors.data
        selected_authors = Authors.query.filter(Authors.id.in_(selected_author_ids)).all()
        book.authors = selected_authors
        db.session.commit()
        flash('El libro ha sido editado correctamente.', 'success')
        return redirect(url_for('books.list_books'))

    form.authors.data = [author.id for author in book.authors]

    return render_template('books/form.html', title="Editar Libro", book=book, form=form, edit_mode=True)

