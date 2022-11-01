from app import db
from app.models.book import Book 
from flask import Blueprint, jsonify, make_response, request

# class Book:
#     def __init__(self, id, title, description): 
#         self.id = id 
#         self.title = title 
#         self.description = description 

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods= ["GET"])
def read_all_books(): 
    books = Book.query.all() 
    books_response = [] 
    for book in books: 
        books_response.append({
            "id": book.id, 
            "title": book.title,
            "description": book.description,
            })
    return jsonify(books_response)

@books_bp.route("", methods= ["POST"])
def create_books(): 
    request_body = request.get_json() 
    new_book = Book(
        title=request_body["title"],
        description= request_body["description"],
    )
    db.session.add(new_book)
    db.session.commit()
    
    return make_response(
        f"Book {new_book.title} created",201
    )



# books = [
#     Books(1, "Harry Potter", "a fairytale of sneaky witches, wizards and all matter of magical creatures that unite to defeat an evil magical overlord"), 
#     Books(2, "Twilight", "A tale of romance centering an emo vegan vampire who falls in love with a human and tries not to eat her"),
#     Books(3, "Oh the Places You'll Go!","A book about adventure, travel, and the many wonderful places that exist in the universe"),
# ]


# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in BOOKS:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))



# @books_bp.route("", methods = ["GET"])
# def get_all_books():
#     books_response = [] 
#     for book in BOOKS: 
#         books_response.append({
#             "id": book.id, 
#             "title": book.title,
#             "description": book.description,
#             })
#     return jsonify(books_response)



# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }






