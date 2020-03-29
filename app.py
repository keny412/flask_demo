from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
