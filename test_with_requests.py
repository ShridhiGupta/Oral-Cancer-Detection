import requests
from PIL import Image
import io

def test_with_requests_library():
    try:
        # Create a simple test image
        print("Creating test image...")
        img = Image.new('RGB', (224, 224), color='blue')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Prepare the file for upload
        files = {'image': ('test.jpg', img_bytes, 'image/jpeg')}
        
        print("Sending POST request to /predict...")
        response = requests.post('http://localhost:5000/predict', files=files)
        
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print("SUCCESS! Analysis completed.")
        else:
            print(f"ERROR: Got status code {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_with_requests_library()
