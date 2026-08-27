import miniupnpc

u = miniupnpc.UPnP()
u.discoverdelay = 3000

print("devices:", u.discover())
print("gateway:", u.selectigd())
print("external:", u.externalipaddress())

for port in [7575, 8000, 8001]:
    try:
        ok = u.addportmapping(
            port,
            "TCP",
            "192.168.1.43",
            port,
            f"MPEdit {port}",
            "",
            86400
        )
        print(f"{port}: {ok}")
    except Exception as e:
        print(f"{port}: ERROR - {e}")