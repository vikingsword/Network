# !usr/bin/env python
# -*- coding:utf-8 _*-
from pywinauto.application import Application

app = Application(backend='uia').start("notepad.exe")
