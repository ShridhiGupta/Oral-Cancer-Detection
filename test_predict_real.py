import urllib.request
import json
from PIL import Image
import io

def test_predict_with_real_image():
    try:
        # Create a simple test image
        print("Creating test image...")
        img = Image.new('RGB', (224, 224), color='red')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        
        # Create multipart form data manually
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        body = (
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="image"; filename="test.jpg"\r\n'
            f'Content-Type: image/jpeg\r\n\r\n'
        ).encode('utf-8')
        body += img_bytes.getvalue()
        body += f'\r\n--{boundary}--\r\n'.encode('utf-8')
        
        # Make the request
        print("Sending POST request to /predict...")
        req = urllib.request.Request(
            'http://localhost:5000/predict',
            data=body,
            headers={
                'Content-Type': f'multipart/form-data; boundary={boundary}',
                'Content-Length': str(len(body))
            }
        )
        
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        print(f"Predict response: {result}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_predict_with_real_image()
