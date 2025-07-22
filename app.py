from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/convert": {"origins": "*"}})  # Allow all origins (or specify GitHub pages URL)

@app.route("/convert", methods=["POST", "OPTIONS"])
def convert():
    if request.method == "OPTIONS":
        return '', 204  # Respond OK to preflight
    data = request.get_json()
    jenkinsfile = data.get("jenkinsFile", "")

    output = {
        "stages": ["build", "test", "deploy"],
        "build_job": {
            "stage": "build",
            "script": ["echo Building project..."]
        },
        "test_job": {
            "stage": "test",
            "script": ["echo Running tests..."]
        },
        "deploy_job": {
            "stage": "deploy",
            "script": ["echo Deploying..."]
        }
    }

    return yaml.dump(output)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
