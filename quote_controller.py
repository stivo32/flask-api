from flask_restful import Resource, reqparse
import random
from data import quotes


class Quote(Resource):
    def get(self, id):
        if id == 0:
            return random.choice(quotes), 200
        for quote in quotes:
            if quote["id"] == id:
                return quote, 200
        return "Quote not found", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        _id = sorted([quote['key'] for quote in quotes])[-1] + 1
        print(_id)
        new_quote = {
                'id': _id,
                'author': params["author"],
                'quote': params["quote"],
            }
        quotes.append(new_quote)
        return new_quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in quotes:
            if id == quote["id"]:
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200

        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }

        quotes.append(quote)
        return quote, 201

    def delete(self, id):
        for i, quote in enumerate(quotes):
            if id == quote["id"]:
                quotes.pop(i)
                return "quote deleted", 200
        return f"Quote with {id} is not exist", 404

