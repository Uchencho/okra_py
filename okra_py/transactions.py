from .auth import Initializer

class OkraTransaction(Initializer):
    """
    allows developers to receive customer-authorized transaction data for current, savings, and domiciliary Accounts.
    
    docs link: https://docs.okra.ng/products/transactions
    
    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')
    """

    def getTransactions(self):
        """
        Retrieve transactions

        Returns: Response object
        """
        url = self._base_url + "products/transactions"
        return self._requests.post(url, headers = self._headers)
