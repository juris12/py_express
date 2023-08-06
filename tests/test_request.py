from src.request import Request

test_msg = 'GET / HTTP/1.1\r\nContent-Type: application/json\r\n\r\n{"name":"jangfbdddis","pwd_hash":"Aaf12afasf"}\r\n'

def test_req_method():
    req = Request(test_msg)
    assert req.method == 'GET'

