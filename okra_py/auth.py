from .errors import MissingTokenError, RequestLibraryError
from .base import Initializer

class Okra_Auth(Initializer):
    """
    Okra offers a path for a customer to successfully verify their bank. 
    The customer enters their credentials and are authenticated immediately.
    
    https://docs.okra.ng/products/auth

    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')
    """

     
    def retrieve_auth(self):
        
        """
        Retrieve Bank details
        """
        url = self._base_url + "products/auths"
        return self._requests.post(url, headers = self._headers)
    
    
    def getbyID(self, idx, page=1, limit=20):
        
        """
        fetch authentication info using the id of the authentication record.
        
        Args : "idx" (string): "5rggfdfghjkl4567"
        """
        url = self._base_url + "auth/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyOptions(self, first_name, last_name, page=1, limit=20):
        """
        fetch authentication info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self._base_url + "auth/byOptions"
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyCustomer(self, customer_id, page=1, limit=20, **kwargs):
        """
        fetch authentication info using the customer id.
        
        Args : "customer_id" (string): "5rggfdfghjkl4567",
        """
        url = self._base_url + "auth/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyDate(self, from_, to_, page=1, limit=20):
        """
        fetch authentication info using a date range.
        
        Args : "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "auth/getByDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyBank(self, bank_id, page=1, limit=20):
        """
        fetch authentication info using the bank id.
        
        Args : "bank_id" (string): "5rggfdfghjkl4567",
        """
        url = self._base_url + "auth/getByBank"
        data_ = {"page": page, "limit":limit, "bank":bank_id}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=20):
        """
        fetch authentication for a customer using a date range and customer id.
        
        Args : "customer":"5rggfdfghjkl4567",
                "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "auth/getByDateCustomer"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)