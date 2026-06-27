import pyttsx3
engine = pyttsx3.init()

TEXT = "你好，今天又是美好的一天。风和日丽，万里晴空! very good!"
OUTPUT_FILE = "test.wav"

engine.save_to_file(TEXT , OUTPUT_FILE)
engine.runAndWait()