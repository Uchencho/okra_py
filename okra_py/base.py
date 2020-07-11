from .errors import RequestLibraryError, MissingTokenError

class Initializer():

    def __init__(self, token=None, base_url='https://api.okra.ng/sandbox/v1/', prod_url=None):
        
        """
        Import requests on initialization
        Set the headers based on api token
        Set needed attributes
        """
        try:
            import requests
        except ModuleNotFoundError:
            raise RequestLibraryError("Please install request module")

        if token is None:
            raise MissingTokenError("Token is necessary to initialize this class")
        
        self._api_token = token
        self._base_url = base_url if prod_url is None else prod_url
        self._headers = {'Content-Type': 'application/json',
                          'Authorization' : 'Bearer ' + self._api_token}
        self._requests = requests