import requests
from PIL import Image
import io

def test_mock_endpoint():
    try:
        # Create a simple test image
        print("Creating test image...")
        img = Image.new('RGB', (224, 224), color='green')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Prepare the file for upload
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("Sending POST request to /predict_mock...")
        response = requests.post('http://localhost:5000/predict_mock', files=files)
        
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print("SUCCESS! Mock prediction completed.")
            result = response.json()
            print(f"Classification: {result['classification']}")
            print(f"Confidence: {result['confidence']}%")
        else:
            print(f"ERROR: Got status code {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_mock_endpoint()
