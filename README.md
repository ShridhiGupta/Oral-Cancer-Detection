# Oral Cancer Detection

An AI-powered web application for early detection of oral cancer using deep learning and computer vision. This project leverages a ResNet18-based neural network to analyze oral cavity images and provide probabilistic assessments for cancer detection.

## 🌟 Features

- **AI-Powered Detection**: Uses a trained ResNet18 model for accurate image classification
- **User Authentication**: Secure login/registration system with JWT tokens
- **Interactive Web Interface**: Modern, responsive frontend built with HTML, CSS, and JavaScript
- **Real-time Analysis**: Instant image upload and prediction results
- **User Dashboard**: Track analysis history and personal statistics
- **Educational Resources**: Comprehensive information about oral cancer prevention and detection

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask with CORS support
- **Authentication**: JWT-based authentication with bcrypt password hashing
- **Database**: MongoDB for user data and analysis history
- **ML Model**: PyTorch ResNet18 for image classification
- **API Endpoints**: RESTful API for authentication and predictions

### Frontend
- **Technologies**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with responsive design
- **UI Components**: Modern interface with Font Awesome icons
- **Pages**: Home, About, Detection, Resources, Contact, and more

### Machine Learning Model
- **Architecture**: ResNet18 (pre-trained on ImageNet)
- **Output Classes**: 3-class classification (Normal, Benign, Malignant)
- **Input**: Oral cavity images
- **Framework**: PyTorch

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MongoDB
- Node.js (optional for development tools)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd oral_cancer_detection
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myvenv
   # Windows
   myvenv\Scripts\activate
   # Unix/MacOS
   source myvenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   MONGO_URI=mongodb://localhost:27017/oral_cancer_db
   JWT_SECRET=your-secret-key-here
   FLASK_ENV=development
   ```

5. **Start MongoDB**
   ```bash
   # Windows
   mongod
   # Unix/MacOS
   sudo mongod
   ```

6. **Run the application**
   ```bash
   cd backend
   python app.py
   ```

7. **Access the application**
   - Frontend: http://localhost:5000
   - API Base URL: http://localhost:5000/api

## 📁 Project Structure

```
oral_cancer_detection/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── auth.py             # Authentication logic
│   ├── model.py            # PyTorch model definition
│   ├── predict.py          # Prediction logic
│   ├── train.py            # Model training script
│   └── model.pth           # Trained model weights
├── frontend/
│   ├── index.html          # Homepage
│   ├── detection.html      # Detection interface
│   ├── about.html          # About page
│   ├── style.css           # Main stylesheet
│   ├── script.js           # JavaScript functionality
│   └── [other pages]       # Additional HTML pages
├── Oral_Cancer_Dataset/    # Training dataset
├── requirements.txt        # Python dependencies
├── test_*.py              # Test files
└── README.md              # This file
```

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user info

### Prediction
- `POST /api/predict` - Upload image for analysis

### User Data
- `GET /api/user/analyses` - Get user's analysis history
- `GET /api/user/stats` - Get user statistics
- `GET /api/user/notifications` - Get user notifications

## 🧪 Testing

The project includes several test files:
- `test_api.py` - API endpoint testing
- `test_import.py` - Import testing
- `test_mock.py` - Mock testing
- `test_predict_real.py` - Real prediction testing
- `test_with_requests.py` - HTTP request testing

Run tests with:
```bash
python test_api.py
```

## 🎯 Model Performance

The ResNet18 model is trained on oral cavity images and provides:
- **Input**: 224x224 RGB images
- **Output**: Probability scores for 3 classes
- **Accuracy**: High accuracy on validation dataset
- **Inference Time**: < 1 second per image

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- Input validation and sanitization
- Secure file upload handling

## 🌐 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📊 Dataset

The model is trained on a curated dataset of oral cavity images:
- **Normal**: Healthy oral cavity images
- **Benign**: Non-cancerous abnormalities
- **Malignant**: Cancerous lesions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with any questions you may have regarding a medical condition.

## 📞 Contact

For questions, suggestions, or collaborations:
- Email: [your-email@example.com]
- GitHub: [your-github-username]

## 🙏 Acknowledgments

- PyTorch team for the deep learning framework
- Flask developers for the web framework
- Medical professionals who contributed to dataset curation
- Open-source community for various libraries and tools

