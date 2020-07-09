from .auth import Initializer

class OkraIdentify(Initializer):
    """
    allows you to retrieve various account holder information on file with the bank, including names, emails, phone numbers, and addresses.
    
    docs link: https://docs.okra.ng/products/identity
    
    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')

    Each of the underlying methods return the full response object
    """

    def getIdentity(self):
        """
        Retrieve transactions

        Returns: Response object
        """
        url = self._base_url + "products/identities"
        return self._requests.post(url, headers = self._headers)