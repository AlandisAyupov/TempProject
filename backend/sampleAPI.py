from flask import Blueprint

api_bp = Blueprint('api', __name__)

def setup_routes(app):

    @api_bp.route('/flashcards', methods=['GET'])
    def get_flashcard(flashcard_id):
        return "200"

    @api_bp.route('/flashcards', methods=['POST'])
    def create_flashcard():
        return "200"

    app.register_blueprint(api_bp)