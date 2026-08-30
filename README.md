# MPEdit Server Setup

This repository contains the server components required to run MPEdit.

## Prerequisites

Before starting the servers, ensure that the required ports are accessible to clients that need to connect to them.

The following ports are used:

|   Port | Component        |
| -----: | ---------------- |
| `7575` | Dedicated server |
| `8000` | Signaling server |
| `8001` | Web server       |

You can either use the included `upnp.py` script to configure port forwarding automatically or manually forward ports `8000`, `8001`, and `7575` to the machine running the servers.

> **Note:** If you are configuring port forwarding manually, make sure you identify the correct local IPv4 address of the server machine (for example, using `ipconfig` on Windows). Your router's configuration may vary.

> **Security note:** Do not expose these services to the public internet unless you have configured appropriate authentication, access controls, and network security.

## Dedicated Server

Start the dedicated server with:

```bash
python server.py
```

The dedicated server listens on port `7575`.

## Signaling Server

Start the signaling server with:

```bash
python signaling.py
```

The signaling server listens on port `8000`.

## Web Server

Start the web server with:

```bash
python web.py
```

The web server listens on port `8001`.

## Running All Components

For a complete MPEdit setup, run all three components:

```text
server.py      → 7575
signaling.py   → 8000
web.py         → 8001
```

Make sure the required ports are reachable from clients before attempting to connect.

## Hardware Recommendations

For a basic session with all three components running on the same machine, we recommend at least:

* AMD Ryzen 3 1200 or equivalent
* Intel Core i3-10100F or equivalent
* 8 GB of RAM

For improved performance and larger or more demanding sessions, we recommend:

* AMD Ryzen 5 3600 or equivalent
* Intel Core i5-12400F or equivalent
* 16 GB of RAM

A wired Ethernet connection is also recommended, as Wi-Fi connections can sometimes be less stable depending on the network environment.
