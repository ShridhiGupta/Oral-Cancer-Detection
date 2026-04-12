import requests
import os

# Test the predict endpoint with a simple image
def test_predict_endpoint():
    url = "http://localhost:5000/predict"
    
    # Create a simple test image file
    test_image_path = "test_image.txt"
    with open(test_image_path, "w") as f:
        f.write("fake image content for testing")
    
    try:
        with open(test_image_path, "rb") as f:
            files = {"image": f}
            print(f"Sending POST request to {url}")
            response = requests.post(url, files=files)
            
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print("SUCCESS: API endpoint is working")
        else:
            print(f"ERROR: Got status code {response.status_code}")
            
    except Exception as e:
        print(f"Error making request: {e}")
    finally:
        # Clean up test file
        if os.path.exists(test_image_path):
            os.remove(test_image_path)

if __name__ == "__main__":
    test_predict_endpoint()
