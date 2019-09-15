from app import app
from flask import jsonify

@app.route('/', methods=['GET'])
@app.route('/api/v1', methods=['GET'])
def home():
  return jsonify({ 'message': 'Welcome to Questioner API v1', 'success': True  })

