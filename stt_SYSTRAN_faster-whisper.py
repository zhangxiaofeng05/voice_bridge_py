from faster_whisper import WhisperModel
import torch

model_name = "turbo"
device = "cpu"

# or run on CPU with INT8
model = WhisperModel(model_name, device=device, compute_type="int8")

segments, info = model.transcribe("test.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))