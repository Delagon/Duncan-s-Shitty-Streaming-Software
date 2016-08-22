import pyscreenshot
import time

while True:
  i = pyscreenshot.grab()
  i.save("screenshot.png")
  time.sleep(0.1)
