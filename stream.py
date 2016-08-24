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
    i = pyscreenshot.grab(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    i.save("screenshot.png")
    time.sleep(0.1)
