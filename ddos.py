from subprocess import PIPE
import subprocess
import time

while True:
    main = subprocess.run(["./executable"], stdout=PIPE)
    time.sleep(1.0)