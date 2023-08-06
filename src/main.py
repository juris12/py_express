import socket
import re
from .request import Request
from .response import Response
from .routes import Routes


class Server:
    """Initializes class instance"""

    def __init__(self) -> None:
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = None
        self._port = None
        self._router_list = []
        self._queue = None
        self._is_running = False

    def listen(self, ip, port, queue=5):
        """Starts server

        Parameters:

        ip: str
            ip address
        port: int
            port you are using
        queue: int
            number of alowed clients in queue befor cutting of new clients
        """
        if self._is_running:
            print("Server is alredy running")
        else:
            self._is_running = True
            self._host = ip
            self._port = port
            self._queue = queue
            self._server_socket.bind((self._host, self._port))
            self._server_socket.listen(self._queue)
            print(f"Server running on PORT: {port}")
            self._running_client()

    def route(self, path: str, func):
        """Adds route to server"""
        self._router_list.append(func(path))

    def _running_client(self):
        """ Starts server
        
        """
        for _ in range(2):
            # while True:
            try:
                client_socket, _ = self._server_socket.accept()
                msg = client_socket.recv(1024).decode("utf-8")
                
                req = Request(msg)      

                for r in self._router_list:
                    absolute_path = re.search(r"^([\/\w,\/]*)(?:\/:(\w*))?$", r._path)
                    params = absolute_path.group(2)
                    path = absolute_path.group(1)
                    req._add_params_and_path(msg, params)


                    if req.path == path:
                        print("----------------------------------------")
                        print(req.method, req.path, req.params)
                        print("----------------------------------------")

                        if r._methods[req.method] != None:
                            res = Response(client_socket)
                            r._methods[req.method](res, req)
                        else:
                            print(
                                f"Method {req.method} is not defined for route {req.path}"
                            )

                client_socket.shutdown(socket.SHUT_WR)
            except KeyboardInterrupt:
                print("keybord interupt...")
            except Exception as exc:
                print('Error: ')
                print(exc)
                client_socket.shutdown(socket.SHUT_WR)

    def stop_server(self):
        print("Server closed")
        if self._is_running:
            self._is_running = False
            self._server_socket.close()

