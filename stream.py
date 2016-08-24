import pyscreenshot
import time
import sys

if len(sys.argv) < 5:
  while True:
    i = pyscreenshot.grab()
    i.save("screenshot.png")
    time.sleep(0.1)
else:
  while True:
    i = pyscreenshot.grab(bbox =(
      int(sys.argv[1]),
      int(sys.argv[2]),
      int(sys.argv[3]),
      int(sys.argv[4]))
    )
    i.save("screenshot.png")
    time.sleep(0.1)
