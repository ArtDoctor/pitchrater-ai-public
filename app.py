from flask import Flask, flash, jsonify, request, redirect, url_for, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from backend.main_pipelines import get_feedback_for_presentation
from werkzeug.utils import secure_filename
import os
from io import BytesIO
from datetime import datetime
import shutil


ALLOWED_EXTENSIONS = {'pptx', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Flask app and endpoints
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.secret_key = "super secret key"
CORS(app) #comment this on deployment
api = Api(app)


@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


@app.route("/flask/test", methods = ['GET'])
def hello():
    return jsonify({"hello": "hello"})


@app.route('/flask/upload', methods=['POST'])
def upload_file():
    """Handles the upload of a file."""
    d = {}
    try:
        file = request.files['file_from_react']
        filename = file.filename
        if allowed_file(filename):
            print(f"Uploading file {filename}")
            now = datetime.now()
            dt_string = now.strftime("calls_folder/%d-%m-%Y-%H-%M-%S")
            if not os.path.exists(dt_string):
                os.makedirs(dt_string)
            
                full_path = os.path.join(os.path.abspath(dt_string), 'presentation.pptx')
                file.save(full_path)
                
                result = get_feedback_for_presentation(full_path, dt_string)

                d['result'] = result
            else:
                raise Exception("Same folder exists already")

            d['status'] = 1
        else:
            d['result'] = 'Wrong file extension. Please use pptx/pdf.'
            d['status'] = 1


    except Exception as e:
        print(f"Couldn't upload file. Error: {e}")
        d['status'] = 0

    return jsonify(d)
