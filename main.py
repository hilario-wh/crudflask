from flaskcrud import create_app, db
from flask import redirect, url_for


# Inica la app
app = create_app()

with app.app_context():
    db.create_all()
    

@app.route('/')
def index():
    return redirect(url_for('books.list_books'))

if __name__ == '__main__':
    app.run()
