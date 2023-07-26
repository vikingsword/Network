import os
import sys

print(sys.version_info.major)
filename = os.path.abspath(__file__)
print(filename)
dir_name = os.path.dirname(filename)
print(dir_name)