
from flask import Flask, request, jsonify
from flask_cors import CORS
import yaml
import os

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    jenkinsfile = data.get("jenkinsfile", "")

    # Simple mock conversion logic
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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # fallback to 10000
    app.run(host="0.0.0.0", port=port)
