import re
import json

class Request:
    """ Request object
        
    """
    def __init__(self, msg):  
        bodyparse = ""

        body = msg.split("\r\n\r\n")

        if len(body) >= 2 and body[1] != "":
            for i in body[1].split("\n"):
                bodyparse += i.replace("\r", "")

            bodyparse = json.loads(bodyparse)
        else:
            bodyparse = None

        self._body = bodyparse
        self._mathod = msg.split("\n")[0].split(" ")[0]


    def _add_params_and_path(self,msg, params):
        """ adds parameters and path to request object
        msg: request data that is recived from client

        params: url parameter that is added to route by user for example: "route/:parameter"

        """
        absolute_path = re.search(
            r"^(\/[\w,\/]*)?(?:\/([\w,\.]*))$", msg.split("\n")[0].split(" ")[1]
        )

        number_of_grops_found = 2 if absolute_path.group(1) else 1
        if params and number_of_grops_found == 2:
            self._params = absolute_path.group(2)
            self._path = absolute_path.group(1)
        else:
            self._path = f"/{absolute_path.group(2)}"
            self._params = None

    @property
    def params(self):
        return self._params

    @property
    def body(self):
        return self._body

    @property
    def method(self):
        return self._mathod

    @property
    def path(self):
        return self._path


