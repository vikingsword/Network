# !usr/bin/env python
# -*- coding:utf-8 _*-
import ChatTTS
from IPython.display import Audio

chat = ChatTTS.Chat()
chat.load_models()

texts = ["123",]

wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)