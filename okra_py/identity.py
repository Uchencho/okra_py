from .base import Initializer

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

    def getbyID(self, idx, page=1, limit=20):
        """
        retrieve various account holder information on file using the id.
        
        Args : "idx" (string)
        """
        url = self._base_url + "identity/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyOptions(self, first_name, last_name, page=1, limit=20):
        """
        fetch identity info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self._base_url + "identity/byOptions"
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomer(self, customer_id, page=1, limit=20):
        """
        retrieve various account holder information on file using the customer id.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "identity/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyDate(self, from_, to_, page=1, limit=20):
        """
        etrieve various account holder information on file using date range.
        
        Args : "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "identity/getByDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=20):
        """
        fetch account holder information on file using date range and customer id.
        
        Args : "customer" (string):"5rggfdfghjkl4567",
                "to_" (string): "2020-04-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "identity/getByCustomerDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)