# py_express
Py_express Is a simple http server library that try’s to mimic functionality of express.js only using python web sockets.

# Quick Start

1. Define your port number and your ip.
```
PORT = 5000
IP = "127.0.0.1"
```
2. Import sys, os, Server, Response, Request, Routes
```
import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, ".."))
from src import Server, Response, Request, Routes
```
3. Create server instance and start the server
```
#create server instance
server = Server()

# start server
server.listen(IP, PORT, 5)
```
4. Create route function and add it to server
```
# defines route function
def home_route(path):
    route = Routes(path)
    return route

# add route to server
server.route("/", home_route)
```
5. Create function for a method 
```
# defines function for get method
def home_route_get(res: Response, req: Request, next=None):
    # sets statuscode 
    res.status(200)
    # sets headers
    res.headers(["Content-Type: text/html", "charset=utf-8"])
    # sets message
    res.mesage(f"Server is online")
    # sends response
    res.send()
```
6. Adds that method to router
```
def home_route(path):
    route = Routes(path)
    # adds function to route
    route.get(home_route_get)
    return route

```

# Suggested file structure
/src
    main.py
    /routes
        route1.py
        route2.py
        ...





