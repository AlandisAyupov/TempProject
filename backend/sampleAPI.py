from flask import Flask, request, jsonify

app = Flask(__name__)

@app.  route("/flashcards/<flashcard_id>", methods=["GET"])
def get_flashcard(flashcard_id):
    return jsonify({"flashcard_id": flashcard_id}), 200

if __name__ == "__main__":
    app.run(debug=True) 