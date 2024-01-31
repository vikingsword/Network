import time

from rich.progress import track

for i in track(range(10), description='process',
               complete_style='blue', finished_style='green'):
    time.sleep(1)