import miniupnpc

u = miniupnpc.UPnP()
u.discoverdelay = 200

print("discovering router...")
count = u.discover()
print(f"found {count} device(s)")

if count == 0:
    raise RuntimeError("No UPnP devices found")

u.selectigd()

print("router:", u.getfriendlyname())
print("local IP:", u.lanaddr)

ports = [8000, 8001, 7575]

for port in ports:
    try:
        u.deleteportmapping(port, "TCP")
        print(f"removed old {port} mapping")
    except Exception:
        print(f"no old {port} mapping found")

    success = u.addportmapping(
        port,
        "TCP",
        u.lanaddr,
        port,
        f"MPEdit Backend {port}",
        ""
    )

    print(f"{port}: {'SUCCESS' if success else 'FAILED'}")
