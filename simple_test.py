import urllib.request
import json

def test_flask_app():
    try:
        # Test the simple test route
        print("Testing /test route...")
        response = urllib.request.urlopen('http://localhost:5000/test')
        data = response.read().decode('utf-8')
        print(f"Test route response: {data}")
        
        # Test the main page
        print("\nTesting / route...")
        response = urllib.request.urlopen('http://localhost:5000/')
        data = response.read().decode('utf-8')
        print(f"Main page response length: {len(data)} characters")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_flask_app()
