from flask import Blueprint, jsonify 


class Books():
    def __init__(self, id, title, description): 
        self.id = id 
        self.title = title 
        self.description = description 

books_bp = Blueprint(Books, __name__, url_prefix="/books")


BOOKS = [
    Books(1, "Harry Potter", "a fairytale of sneaky witches, wizards and all matter of magical creatures that unite to defeat an evil magical overlord"), 
    Books(2, "Twilight", "A tale of romance centering an emo vegan vampire who falls in love with a human and tries not to eat her"),
    Books(3, "Oh the Places You'll Go!","A book about adventure, travel, and the many wonderful places that exist in the universe"),
]

@books_bp.route("", methods = ["GET"])
def get_all_books():
    books_response = [] 
    for book in BOOKS: 
        books_response.append({
            "id": book.id, 
            "title": book.title,
            "description": book.description,
            })
    return jsonify(books_response) 






