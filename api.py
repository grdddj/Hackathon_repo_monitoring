from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

import aggregator

app = Flask(__name__)
api = Api(app)

# Enabling CORS, to use this API everywhere
CORS(app)

class BranchWatcher(Resource):
    def get(self):
        result = aggregator.aggregate_branches()
        return result

class LanguagesWatcher(Resource):
    def get(self):
        result = aggregator.aggregate_languages()
        return result

class CommitsWatcher(Resource):
    def get(self):
        result = aggregator.aggregate_contributors_and_commits()
        return result

api.add_resource(BranchWatcher, '/branches')
api.add_resource(LanguagesWatcher, '/languages')
api.add_resource(CommitsWatcher, '/commits')

if __name__ == '__main__':
     app.run(port='5005', debug=True)
