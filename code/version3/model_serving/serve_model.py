# Ensure FastAPI and PyTorch are installed: pip install fastapi torch
from fastapi import FastAPI
import torch
import torch.nn as nn

# Define the model class
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(28 * 28, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        return self.fc(x)

# Load the model
model = SimpleNN()
model.load_state_dict(torch.load("mnist_model.pth"))
model.eval()

# Initialize FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(data: list):
    tensor_data = torch.tensor(data, dtype=torch.float32)
    with torch.no_grad():
        predictions = model(tensor_data)
    return {"predictions": predictions.tolist()}