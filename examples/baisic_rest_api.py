PORT = 5000
IP = "127.0.0.1"
import sys
import os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(parent_dir, ".."))
from src import Server, Response, Request, Routes

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

# start server
server.listen(IP, PORT, 5)
