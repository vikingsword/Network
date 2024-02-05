# !usr/bin/env python
# -*- coding:utf-8 _*-
from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("test1.py")]
)
