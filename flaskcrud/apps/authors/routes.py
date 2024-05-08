from flask import Blueprint, render_template, redirect, url_for, flash

# Modelos
from ...models import Authors

# Forms
from ...forms import AuthorForm

# DB
from flaskcrud import db


authors_bp = Blueprint('authors', __name__, url_prefix='/authors')

@authors_bp.route('/')
def list_authors():
    authors = Authors.query.all()
    return render_template('authors/list.html', authors=authors)


def handle_author_form(form, author=None):
    if form.validate_on_submit():
        if not author:
            author = Authors()
        author.name = form.name.data
        author.lastname = form.lastname.data
        author.email = form.email.data
        db.session.add(author)
        db.session.commit()
        flash('El autor ha sido añadido correctamente.', 'success')
        return True
    return False


@authors_bp.route('/add-author/', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()
    if handle_author_form(form):
        return redirect(url_for('authors.list_authors'))
    return render_template('authors/form.html', title="Añadir autor", form=form)


@authors_bp.route('delete-author/<int:author_id>')
def delete_author(author_id):
    author = Authors.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash('El autor ha sido eliminado correctamente.', 'success')
    return redirect(url_for('authors.list_authors'))


@authors_bp.route('/edit-author/<int:author_id>', methods=['GET', 'POST'])
def edit_author(author_id):
    author = Authors.query.get_or_404(author_id)
    form = AuthorForm(obj=author)
    if handle_author_form(form, author):
        return redirect(url_for('authors.list_authors'))
    return render_template('authors/form.html', title="Editar autor", form=form, author=author, edit_mode=True)
