import subprocess
import os
subprocess.run("pip install --only-binary :all: -r requirements.txt" if os.name == "nt" else "pip3 install --only-binary :all: -r requirements.txt", shell=True)