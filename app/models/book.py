from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(title = book_data["title"], 
                        description=book_data["description"])
        return new_book

    def to_dict(self): 
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict

    # Claire's idea 
    # def update(self, book_data):
    #     self.id = book_data["id"]
    #     self.title = book_data["title"]
    #     self.description = book_data["description"]



