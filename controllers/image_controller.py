import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request, jsonify, Blueprint
from werkzeug.utils import secure_filename
from services.s3_operations import S3Operations
from models.InMemoryFileObject import InMemoryFileObject
from controllers.image_controller_helper import is_allowed_file


image_controller = Blueprint('image_controller', __name__)

@image_controller.route('/upload-profile-pic', methods=['POST'])
def upload_file():
    uploaded_file = request.files['profile_image']
    user_id = request.form['user_id']

    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    if not is_allowed_file(uploaded_file):
        return jsonify({'error': 'Invalid file type'}), 400
    
    file_obj = InMemoryFileObject(uploaded_file)

    url = S3Operations(user_id=user_id).upload_file(file_obj)

    return jsonify({'profile_image_url': url})


@image_controller.route('/edit-profile-pic', methods=['POST'])
def edit_file():
    uploaded_file = request.files['profile_image']
    user_id = request.form['user_id']

    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    if not is_allowed_file(uploaded_file):
        return jsonify({'error': 'Invalid file type'}), 400
    
    file_obj = InMemoryFileObject(uploaded_file)

    
    url = S3Operations(user_id=user_id).edit_file(file_obj)

    return jsonify({'profile_image_url': url})


@image_controller.route('/delete-profile-pic', methods=['POST'])
def delete_file():
    user_id = request.form['user_id']
    S3Operations(user_id=user_id).delete_file()

    return jsonify({'message': 'Profile image deleted successfully'})

