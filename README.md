# py_express
Py_express Is a simple http server library that try’s to mimic functionality of express.js only using python web sockets.

Note: Only baisic functionality is implimented(sending text messages and html files)

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
# Full example
main.py/server.py
```
PORT = 5000
IP = "127.0.0.1"
import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, ".."))
from src import Server, Response, Request, Routes
from routes.profil_route import profil_route
from routes.login_route import login_route

#create server instance

server = Server()

def home_route_get(res: Response, req: Request, next=None):
    res.status(200)
    res.headers(["Content-Type: text/html", "charset=utf-8"])
    res.mesage(f"Server is online")
    res.send()


def home_route(path):
    route = Routes(path)
    route.get(home_route_get)
    return route

# add routes to server
server.route("/", home_route)
server.route("/login", login_route)
server.route("/profil/:id", profil_route)

# start server
server.listen(IP, PORT, 5)
```
login_route.py
```
from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import bcrypt

def is_not_pwd_valid(profil, pwd):
    if profil == None:
        return True
    if bcrypt.checkpw(pwd.encode("utf-8"), profil.pwd_hash):
        return False
    return True


def login_route_post(res: Response, req: Request, next=None):
    """
    checks if user existe ad validates pwd
    """
    try:
        db = Db()
        profil: Profile = db.get(req.body["name"])

        if is_not_pwd_valid(profil, req.body["pwd_hash"]):
            res.status(400)
            res.headers(["Content-Type: application/json"])
            res.mesage(f'"message":"Name or pwd is incorect!"')
        else:
            res.status(200)
            res.headers(["Content-Type: application/json"])
            res.json([profil])
    except KeyError:
        res.status(400)
        res.headers(["Content-Type: application/json"])
        res.mesage(f"No name or pwd!")
    res.send()


def login_route(path):
    route = Routes(path)
    route.post(login_route_post)
    return route
```
porfil_route.py
```
from lib.py_express.routes import Routes
from lib.py_express.server import Response
from lib.py_express.server import Request
from db import Profile
from db import Db
import json


def profil_route_get(res: Response, req: Request, next=None):
    db = Db()
    res.status(200)
    res.headers(["Content-Type: application/json"])
    # res.json([x for x in db.get() if x.status])
    res.json(db.get())
    res.send()


def profil_route_post(res: Response, req: Request, next=None):
    db = Db()
    res.status(200)
    res.headers(["Content-Type: application/json"])
    user = [x for x in db.get() if x.name == req.params]

    if len(user) == 1:
        db.change_status(user[0].name)
        res.mesage(
            f'"mesage":"Status cnaged for user {user[0].name} to {user[0].status}"'
        )
    else:
        res.mesage('"mesage":"no user found"')
    res.send()


def profil_route(path):
    route = Routes(path)
    route.post(profil_route_post)
    route.get(profil_route_get)
    return route

```

# Suggested file structure
```
/src
    main.py
    /routes
        route1.py
        route2.py
        ...
```





