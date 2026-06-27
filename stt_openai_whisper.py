import whisper
import torch

# print(torch.cuda.is_available())   # NVIDIA
# print(torch.backends.mps.is_available())  # Apple Silicon

# print(torch.__version__)
# print(torch.backends.mps.is_available())
# print(torch.backends.mps.is_built())

model_name = "turbo"
device = "mps" if torch.backends.mps.is_available() else "cpu"

# device="cpu"

model = whisper.load_model(
  model_name,
  device=device
)
# print(model.device)
result = model.transcribe("test.mp3")
print(result["text"])