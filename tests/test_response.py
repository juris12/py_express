from src.response import Response

def test_response():
    def home_route_get(res: Response, req, next=None):
        res.status(200)
        res.headers(["Content-Type: text/html", "charset=utf-8"])
        res.mesage(f"Server is online")

    res = Response('127.0.0.1')
    home_route_get(res, None)
    assert res._status_code == 200
    assert res._headers == ["Content-Type: text/html", "charset=utf-8"]
    assert res._mesage == "Server is online"