from sp_toaster.run import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})