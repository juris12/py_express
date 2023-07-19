import json

class Response:
    """Response objekt

    header: sets a list of headers

    status: sets satus code

    mesage: sets regular text message

    send: sends response to client
    """

    def __init__(self, client_socket):
        self._headers = []
        self._status_code = 500
        self._mesage = ""
        self._client_socket = client_socket

    def headers(self, headers):
        self._headers = headers

    def status(self, headers):
        self._status_code = headers

    def json(self, db):
        self._mesage = json.dumps(
            [
                {
                    "name": x.name,
                    "pwd_hash": x.pwd_hash.decode("utf-8"),
                    "status": x.status,
                    "ip": x.ip,
                }
                for x in db
            ]
        )

    def mesage(self, mesage):
        self._mesage = mesage

    def html(self, path):
        with open(path) as f:
            self._mesage = f.read()

    def send(self):
        data = f"HTTP/1.1 {self._status_code}\r\n"
        data += f'{"; ".join(self._headers)}\r\n'
        data += "\r\n"
        data += self._mesage
        self._client_socket.sendall(data.encode())

    def send_html(self, path):
        try:
            with open(path) as f:
                self._mesage = f.read()
                self.send()
        except FileNotFoundError:
            data = f"HTTP/1.1 404\r\n"
            data += "\r\n"
            data += f"file: {path} not found!"
            self._client_socket.sendall(data.encode())

    def send_img(self, path):
        try:
            with open("files/favicon.png", "rb") as f:
                img = f.read()

                # response = (
                # "HTTP/1.1 200 OK\r\n"
                # "Content-Type: image/png\r\n"
                # f"Content-Length: {format(len(img))}\r\n\r\n"
                # f'{str(img)}'
                # )
                data = f"HTTP/1.1 200\r\n"
                data += "\r\n"
                data += f"img: {path} send!"
                self._client_socket.sendall(data.encode())
        except FileNotFoundError:
            data = f"HTTP/1.1 404\r\n"
            data += "\r\n"
            data += f"img: {path} not found!"
            self._client_socket.sendall(data.encode())