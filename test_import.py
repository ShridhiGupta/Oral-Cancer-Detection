try:
    print("Testing imports...")
    from predict import predict
    print("predict module imported successfully!")
    
    print("Testing model import...")
    from model import OralModel
    print("model imported successfully!")
    
    print("Testing torch...")
    import torch
    print("torch imported successfully!")
    
    print("Testing torchvision...")
    import torchvision
    print("torchvision imported successfully!")
    
    print("Testing PIL...")
    from PIL import Image
    print("PIL imported successfully!")
    
    print("All imports successful!")
    
except Exception as e:
    print(f"Import error: {e}")
    import traceback
    traceback.print_exc()
