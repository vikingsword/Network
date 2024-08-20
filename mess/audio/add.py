# !usr/bin/env python
# -*- coding:utf-8 _*-

from pydub import AudioSegment

# 加载两段音频
audio1 = AudioSegment.from_file("Bonfire.mp3")
audio2 = AudioSegment.from_file("Bonfire.mp3")
audio3 = AudioSegment.from_file("Bonfire.mp3")
audio4 = AudioSegment.from_file("Bonfire.mp3")

# 将 audio2 添加到 audio1 后面
combined = audio1 + audio2 + audio3 + audio4

# 保存合并后的音频
combined.export("combined_audio2.mp3", format="mp3")
