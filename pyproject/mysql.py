from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    books = [{"id": row[0], "title": row[1], "author": row[2]} for row in rows]
    cur.close()
    return jsonify(books)

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    
    data = request.get_json()
    title = data['title']
    author = data['author']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Book added successfully!"}), 201

# Route to update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    title = data['title']
    author = data['author']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE books SET title=%s, author=%s WHERE id=%s", (title, author, book_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Book updated successfully!"})

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
