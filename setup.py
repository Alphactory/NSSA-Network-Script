import subprocess
import os
subprocess.run("pip install -r requirements.txt" if os.name == "nt" else "pip3 install -r requirements.txt")