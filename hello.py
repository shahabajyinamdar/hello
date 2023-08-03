import json
from flask_cors import CORS, cross_origin
from flask_restx import Api, Resource, fields
from flask import request, Flask
from datetime import date

# Start of appilcation
app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])
# Create the Flask-RESTx API
api = Api(
    app,
    version="1.0",
    title="NPS API",
    description="A Swagger UI collection of NPS Journey API(s)",
)

# Define the namespace
ns = api.namespace("api", description="NPS APIs")


def input_check(input_value):
    match input_value:
        case None:
            raise ValueError("None / Null value")
        case "":
            raise ValueError("Empty String")
        case "string":
            raise ValueError("Default Value not accepted")
        case "0":
            raise ValueError("Default Integer Value")
        case _:
            return input_value


@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        return json.dumps({"message": "ok"})
@cross_origin()

@ns.route("/name")
@ns.doc(responses={400: "Bad Request", 200: "success", 500: "Client Error"})
class generate_RID(Resource):
    @ns.expect(ns.model("name", {"name": fields.String}, strict=True), validate=True)
    def post(self):
        response = request.json
        try:
            name = response["name"]

            return json.dumps({'name':name})
        except:
            return "Error Encountered"
    def get(self):
            return json.dumps({'msg':'Error Method call is GET'})
        


# region HelloWorld
# endregion


if __name__ == "__main__":
    app.run(debug=True)
