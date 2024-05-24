from flask import request, jsonify, current_app
from . import db
from .models import Book, Epoch, Genre, Kind, Author
from .services import add_book, add_categories, filter_books


def init_routes(app):
    @app.route('/books', methods=['POST'])
    def create_book():
        data = request.json
        current_app.logger.info('Received data: %s', data)
        if not data:
            current_app.logger.error('No input data provided')
            return jsonify({"error": "No input data provided"}), 400

        required_fields = ['title', 'epoch_id', 'genre_id', 'kind_id', 'author_id']
        for field in required_fields:
            if field not in data:
                current_app.logger.error('Missing field: %s', field)
                return jsonify({"error": f"Missing field: {field}"}), 400

        try:
            book = add_book(data)
            current_app.logger.info('Book created: %s', book)
            return jsonify(book), 201
        except Exception as e:
            current_app.logger.error('Error creating book: %s', e)
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/categories', methods=['POST'])
    def create_categories():
        data = request.json
        current_app.logger.info('Received data: %s', data)
        if not data:
            current_app.logger.error('No input data provided')
            return jsonify({"error": "No input data provided"}), 400

        try:
            categories = add_categories(data)
            current_app.logger.info('Categories created: %s', categories)
            return jsonify(categories), 201
        except Exception as e:
            current_app.logger.error('Error creating categories: %s', e)
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/books', methods=['GET'])
    def get_books():
        filters = request.args
        current_app.logger.info('Received filters: %s', filters)
        try:
            books = filter_books(filters)
            return jsonify(books), 200
        except Exception as e:
            current_app.logger.error('Error getting books: %s', e)
            return jsonify({"error": "Internal Server Error"}), 500
