import subprocess
from pathlib import Path

ROOT = Path(r"C:\MPEdit\servers\dedicated")

print("starting MPEdit debug dedicated server...")
print("directory:", ROOT)
print("port: 7575")
print()

subprocess.run(
    ["npm", "start"],
    cwd=ROOT
)

input("\npress Enter to close...")