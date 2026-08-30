# MPEdit Server Setup

This repository contains the server components required to run MPEdit.

## Prerequisites

Before starting the servers, ensure that the required ports are accessible to the clients that need to connect to them.

The following ports are used:

|   Port | Component        |
| -----: | ---------------- |
| `7575` | Dedicated server |
| `8000` | Signaling server |
| `8001` | Web server       |

You can either use the included `upnp.py` script to configure port forwarding automatically, (dont remember to run ipconfig or it wont work, i used port 43 on local ipv4) or manually forward ports `8000`, `8001`, and `7575` to the machine running the servers.

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

Make sure the required ports are reachable from the clients before attempting to connect.


### Recommendations

For the machine running all 3, we recommend a machine that has a ryzen 3 1200 or superior or an intel i3 10100f at a minimum with 8gb ram for a basic session. 

Although, we reccomend a ryzen 5 3600 or a intel i5 12400f or superior as a recommendation with 16gb ram. this also comes with ethernet connection, as wifi can sometimes be unstable.