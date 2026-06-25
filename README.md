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

### tts
https://github.com/rany2/edge-tts

dependencies
```bash
uv pip install edge-tts
```

run tts
```bash
uv run edge_tts_main.py
```

### stt
https://github.com/openai/whisper

dependencies
```bash
uv pip install openai-whisper
```

run stt
```bash
uv run openai_whisper_main.py
```
The directory for downloaded models on Mac is `~/.cache/whisper/large-v3-turbo.pt`

## freeze
```bash
uv pip freeze > requirements.txt
```

## sync
```bash
uv sync
```
