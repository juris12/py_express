from src.routes import Routes
def test_routes():
    def home_route_get():
        ...
    route = Routes('/')
    route.get(home_route_get)
    assert route._methods['GET'] == home_route_get
    assert route._methods['POST'] == None
    assert route._path == '/'    