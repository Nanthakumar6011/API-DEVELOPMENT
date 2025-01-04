from flask import Flask,jsonify,request

app=Flask(__name__)

books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe"},
    {"id": 2, "title": "Flask for Beginners", "author": "Jane Smith"}
]
@app.route('/books',methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books/<int:book_id>',methods=['GET'])
def get_book_by_id(book_id):
    book_id_no=next(( book for book in books if book["id"]==book_id),None)

    if book_id_no:
        return jsonify(book_id_no)
    else:
        return jsonify({"error":"Key error in Data"}),404

@app.route('/books',methods=['POST'])
def add_book(book_id):
    new_book=request.get_json()
    books.append(new_book)
    return jsonify(new_book),201





























if __name__=='__main__':
    app.run(debug=True)