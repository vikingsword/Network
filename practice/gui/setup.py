# !usr/bin/env python
# -*- coding:utf-8 _*-
from cx_Freeze import setup, Executable

setup(
    name="test gui",
    version="1.0",
    description="test gui script",
    executables=[Executable("test1.py", base="Win32GUI", target_name='test_gui.exe')]
)
