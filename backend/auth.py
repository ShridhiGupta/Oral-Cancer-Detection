from functools import wraps
from flask import request, jsonify, current_app
import jwt
from datetime import datetime, timedelta

# Simple mock user database for demo purposes
USERS = {}

def generate_token(user_id):
    """Generate JWT token for user"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, current_app.config.get('SECRET_KEY', 'secret-key'), algorithm='HS256')

def token_required(f):
    """Decorator to require JWT token"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]  # Bearer <token>
            except IndexError:
                return jsonify({'error': 'Invalid token format'}), 401
        
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        
        try:
            data = jwt.decode(token, current_app.config.get('SECRET_KEY', 'secret-key'), algorithms=['HS256'])
            current_user_id = data['user_id']
            
            # Mock user object
            class MockUser:
                def __init__(self, user_id):
                    self._id = user_id
                    
            request.current_user = MockUser(current_user_id)
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token is invalid'}), 401
            
        return f(*args, **kwargs)
    
    return decorated

def register_user():
    """Register a new user"""
    try:
        data = request.get_json()
        
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
        
        email = data['email']
        
        if email in USERS:
            return jsonify({'error': 'User already exists'}), 400
        
        # Simple mock user registration
        user_id = len(USERS) + 1
        USERS[email] = {
            'id': user_id,
            'email': email,
            'password': data['password']  # In production, hash this
        }
        
        token = generate_token(user_id)
        
        return jsonify({
            'message': 'User registered successfully',
            'token': token,
            'user': {
                'id': user_id,
                'email': email
            }
        }), 201
        
    except Exception as e:
        return jsonify({'error': 'Registration failed'}), 500

def login_user():
    """Login user"""
    try:
        data = request.get_json()
        
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
        
        email = data['email']
        password = data['password']
        
        if email not in USERS or USERS[email]['password'] != password:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        user = USERS[email]
        token = generate_token(user['id'])
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email']
            }
        })
        
    except Exception as e:
        return jsonify({'error': 'Login failed'}), 500

def get_current_user():
    """Get current user info"""
    try:
        user = getattr(request, 'current_user', None)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'id': user._id,
            'email': f'user{user._id}@example.com'  # Mock email
        })
        
    except Exception as e:
        return jsonify({'error': 'Failed to get user info'}), 500

def get_user_analyses():
    """Get user's analysis history"""
    return jsonify({
        'analyses': [],
        'total': 0
    })

def save_user_analysis():
    """Save analysis for user"""
    return jsonify({
        'message': 'Analysis saved successfully'
    })

def get_user_stats():
    """Get user's statistics"""
    return jsonify({
        'total_analyses': 0,
        'last_analysis': None
    })

def get_user_notifications():
    """Get user's notifications"""
    return jsonify({
        'notifications': []
    })
