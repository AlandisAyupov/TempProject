from flask import Flask, request, jsonify, current_app
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from Flashcard import Flashcard

load_dotenv()

app = Flask(__name__)

def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database="flashcards",
            auth_plugin=os.getenv('AUTH'),
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


@app.route("/flashcards/<flashcard_id>", methods=["GET"])
def get_flashcard(flashcard_id):
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        
        # SQL query to fetch flashcard by ID
        query = "SELECT * FROM flashcards WHERE id = %s"
        cursor.execute(query, (flashcard_id,))
        
        # Fetch the flashcard
        flashcard = cursor.fetchone()
        
        if flashcard:
            return jsonify(flashcard), 200
        return jsonify({"error": "Flashcard not found"}), 404
        
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

@app.  route("/flashcards/", methods=["POST"])
def create_flashcard():
   # Get data from request
    data = request.get_json()
    front = data.get('front')
    back = data.get('back')
    category = data.get('category')
    
    # Validate required fields
    if not all([front, back, category]):
        return jsonify({"error": "Missing required fields"}), 400
        
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS flashcards (
            id INT PRIMARY KEY,
            front VARCHAR(255) NOT NULL,
            back VARCHAR(255) NOT NULL,
            category VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()

        # Get max id from flashcards
        cursor.execute("SELECT MAX(id) as max_id FROM flashcards")
        result = cursor.fetchone()
        new_id = 1 if result['max_id'] is None else result['max_id'] + 1
        
        flashcard = Flashcard(
            id = new_id,
            front=data.get('front'),
            back=data.get('back'),
            category=data.get('category')
        )

        # SQL query to insert flashcard
        query = "INSERT INTO flashcards (id, front, back, category) VALUES (%s, %s, %s, %s)"
        values = (flashcard.id, flashcard.front, flashcard.back, flashcard.category)
        
        cursor.execute(query, values)
        connection.commit()
        
        # Return the created flashcard
        return jsonify(flashcard.to_dict()), 201
        
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(debug=True) 