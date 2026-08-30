import subprocess
from pathlib import Path

ROOT = Path(r"C:\MPEdit\mpedit-web")

print("starting MPEdit web page")
print("directory:", ROOT)
print("port: 8001")
print()

subprocess.run(
    ["node", "server.js"],
    cwd=ROOT
)

input("\npress Enter to close...")