import torch
import os
from torchvision import transforms
from PIL import Image
from model import OralModel

print("Loading oral cancer detection model...")
model = OralModel()
print("Model created, loading weights...")
model.load_state_dict(torch.load(os.path.join(os.path.dirname(__file__), "model.pth"), map_location="cpu"))
print("Model weights loaded successfully!")
model.eval()
print("Model set to eval mode!")
print("Model initialization complete.")

classes = ["normal", "suspicious", "cancer"]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image):
    try:
        print(f"Processing image: {image.filename if hasattr(image, 'filename') else 'unknown'}")
        
        # Convert PIL Image if needed
        if hasattr(image, 'save'):
            pil_image = image
        else:
            pil_image = Image.open(image)
        
        print("Transforming image...")
        image_tensor = transform(pil_image).unsqueeze(0)
        print(f"Image tensor shape: {image_tensor.shape}")

        print("Running model inference...")
        with torch.no_grad():
            outputs = model(image_tensor)
            probs = torch.softmax(outputs, dim=1)[0]

        confidence, pred = torch.max(probs, 0)
        print(f"Prediction: {classes[pred.item()]}, Confidence: {confidence.item()*100:.2f}%")

        return {
            "classification": classes[pred.item()],
            "confidence": float(confidence.item()*100),
            "normal_prob": float(probs[0].item()*100),
            "suspicious_prob": float(probs[1].item()*100),
            "cancer_prob": float(probs[2].item()*100),
            "explanation": "Prediction from trained CNN model.",
            "next_steps": [
                "Consult a doctor",
                "Do clinical tests",
                "Monitor symptoms"
            ]
        }
    except Exception as e:
        import traceback
        print(f"Error in predict function: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        raise e