#!/usr/bin/env python3

"""Simple example to generate audio with preset voice using async/await"""

# https://github.com/rany2/edge-tts
# edge-tts --list-voices

import asyncio

import edge_tts

# TEXT = "Hello World!"
# VOICE = "en-GB-SoniaNeural"

TEXT = "你好，今天又是美好的一天。风和日丽，万里晴空!"
VOICE = "zh-CN-XiaoxiaoNeural"

OUTPUT_FILE = "test.mp3"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(amain())