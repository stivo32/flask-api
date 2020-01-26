from flask import Flask
from flask_restful import Api
from quote_controller import Quote

app = Flask(__name__)
api = Api(app)
api.add_resource(Quote, "/quotes", "/quotes/", "/quotes/<int:id>")


@app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
