from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from predict import predict
from auth import (token_required, register_user, login_user, get_current_user,
                  get_user_analyses, save_user_analysis, get_user_stats, get_user_notifications)
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Configure CORS
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://127.0.0.1:5000", "http://localhost:5000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "X-User-ID"]
    }
})

# ======================
# AUTHENTICATION ROUTES
# ======================

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """Register a new user"""
    return register_user()

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user"""
    return login_user()

@app.route('/api/auth/me', methods=['GET'])
@token_required
def get_me():
    """Get current user info"""
    return get_current_user()

# ======================
# USER ROUTES
# ======================

@app.route('/api/user/analyses', methods=['GET'])
@token_required
def get_analyses():
    """Get user's analysis history"""
    return get_user_analyses()

@app.route('/api/user/analysis', methods=['POST'])
@token_required
def save_analysis():
    """Save analysis for user"""
    return save_user_analysis()

@app.route('/api/user/stats', methods=['GET'])
@token_required
def get_stats():
    """Get user's statistics"""
    return get_user_stats()

@app.route('/api/user/notifications', methods=['GET'])
@token_required
def get_notifications():
    """Get user's notifications"""
    return get_user_notifications()

# ======================
# PREDICTION ROUTES
# ======================

@app.route('/test', methods=['GET'])
def test_route():
    """Simple test route to verify Flask app is working"""
    return jsonify({'message': 'Flask app is working!', 'status': 'ok'})

@app.route('/predict', methods=['POST'])
def predict_route():
    """Handle image prediction requests"""
    print("=" * 50)
    print("PREDICT ROUTE CALLED!")
    print("=" * 50)
    try:
        print(f"Request received: {request.method}")
        print(f"Files in request: {list(request.files.keys())}")
        
        # Check if file is in request
        if 'image' not in request.files:
            print("Error: No 'image' file in request")
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        print(f"File received: {file.filename}, size: {file.content_length}")
        
        # Check if file is selected
        if file.filename == '':
            print("Error: Empty filename")
            return jsonify({'error': 'No file selected'}), 400
        
        # Get user ID from request
        user_id = getattr(request, 'current_user', None)
        if user_id:
            user_id = user_id._id
        
        print("Calling predict function...")
        # Get prediction
        result = predict(file)
        print(f"Prediction result: {result}")
        
        # Add user info to result
        if user_id:
            result['userId'] = user_id
        
        return jsonify(result)
        
    except Exception as e:
        import traceback
        print(f"Error in prediction: {e}")
        print(f"Full traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/predict_mock', methods=['POST'])
def predict_mock_route():
    """Mock prediction route for testing"""
    print("=" * 50)
    print("MOCK PREDICT ROUTE CALLED!")
    print("=" * 50)
    try:
        print(f"Request received: {request.method}")
        print(f"Files in request: {list(request.files.keys())}")
        
        # Check if file is in request
        if 'image' not in request.files:
            print("Error: No 'image' file in request")
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        print(f"File received: {file.filename}, size: {file.content_length}")
        
        # Return mock result
        result = {
            "classification": "normal",
            "confidence": 85.5,
            "normal_prob": 85.5,
            "suspicious_prob": 10.2,
            "cancer_prob": 4.3,
            "explanation": "Mock prediction for testing purposes.",
            "next_steps": [
                "Continue regular dental checkups",
                "Maintain good oral hygiene",
                "Monitor any changes"
            ]
        }
        
        print(f"Mock prediction result: {result}")
        return jsonify(result)
        
    except Exception as e:
        import traceback
        print(f"Error in mock prediction: {e}")
        print(f"Full traceback: {traceback.format_exc()}")
        return jsonify({'error': 'Internal server error'}), 500

# ======================
# FRONTEND ROUTES
# ======================

@app.route('/')
def index():
    """Serve the main frontend"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('../frontend', filename)

# ======================
# ERROR HANDLERS
# ======================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(401)
def unauthorized(error):
    """Handle 401 errors"""
    return jsonify({'error': 'Unauthorized'}), 401

@app.before_request
def log_request_info():
    print(f"=== Incoming Request ===")
    print(f"Method: {request.method}")
    print(f"Path: {request.path}")
    print(f"Headers: {dict(request.headers)}")
    print(f"========================")

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('NODE_ENV', 'development') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)