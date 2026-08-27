import subprocess
from pathlib import Path

ROOT = Path(r"C:\MPEdit\servers\signaling")

print("starting MPEdit signaling server...")
print("directory:", ROOT)
print("port: 8000")
print()

subprocess.run([
    "deno",
    "run",
    "--allow-all",
    "--unstable-kv",
    "worker.js"
], cwd=ROOT)

input("\npress Enter to close...")