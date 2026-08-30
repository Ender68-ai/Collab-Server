import miniupnpc

u = miniupnpc.UPnP()
u.discoverdelay = 200

print("discovering router...")
count = u.discover()
print(f"found {count} device(s)")

u.selectigd()

print("router:", u.getfriendlyname())
print("local IP:", u.lanaddr)

try:
    u.deleteportmapping(8000, "TCP")
    print("removed old 8000 mapping")
except:
    print("no old mapping found")

success = u.addportmapping(
    8000,
    "TCP",
    u.lanaddr,
    8000,
    "MPEdit Backend",
    ""
)

print("mapping:", "SUCCESS" if success else "FAILED")