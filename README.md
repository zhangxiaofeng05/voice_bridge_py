## voice_bridge_py
A simple Python library for bidirectional conversion between text and speech (TTS &amp; STT).

Text-to-speech uses https://github.com/rany2/edge-tts.

speech-to-Text uses https://github.com/openai/whisper.

`uv` dependency management

## init
env
```bash
uv init
uv venv
source .venv/bin/activate
```

## freeze
```bash
uv pip freeze > requirements.txt
```

## sync
```bash
uv sync
```

## tts
### https://github.com/rany2/edge-tts
dependencies
```bash
uv pip install edge-tts
```
run tts
```bash
uv run tts_rany2_edge-tts.py
```

### https://github.com/nateshmbhat/pyttsx3
dependencies
```bash
uv pip install pyttsx3
```
run
```bash
uv run tts_nateshmbhat_pyttsx3.py
```
Convert WAV format to MP3
```bash
ffmpeg -i test.wav test.mp3
```

## stt
### https://github.com/openai/whisper
dependencies
```bash
uv pip install openai-whisper
```
run
```bash
uv run stt_openai_whisper.py
```
The directory for downloaded models on Mac is `~/.cache/whisper/large-v3-turbo.pt`

### https://github.com/SYSTRAN/faster-whisper (Deprecated)
The Mac can only use the CPU.

dependencies
```bash
uv pip install faster-whisper
```
run
```bash
uv run stt_SYSTRAN_faster-whisper.py
```
The directory for downloaded models on Mac is `~/.cache/huggingface/hub`
