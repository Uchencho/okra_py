from auth import Initializer

class Okra_Balance(Initializer):
    
    """
    returns the real-time balance for each of a record's accounts. 
    It can be used for existing Records that were added via any of Okra’s other products
    
    https://docs.okra.ng/products/balance
    
    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')
    """    
    
    def retrieve_balance(self):
        
        """
        Retrieve Bank balance

        Returns: Json Response
        """
        url = self._base_url + "products/balances"
        resp = self._requests.post(url, headers = self._headers)
        return resp.json()
    
    
    def getbyID(self, idx, page=1, limit=20):
        
        """
        
        fetch balance info using the id of the balance.
        
        Args : "idx" (string)
        
        """
        url = self._base_url + "balance/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        resp = self._requests.post(url, headers = self._headers, json=data_)
        return resp.json()
    
    
    def getbyOptions(self, first_name, last_name, page=1, limit=20):
        """
        fetch balance info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self._base_url + "balance/byOptions"
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        resp = self._requests.post(url, headers = self._headers, json=data_)
        return resp.json()
    
    
    def getbyCustomer(self, customer_id, page=1, limit=20):
        """
        
        fetch balance info using the customer id.
        
        Args : "customer_id" (string)
        
        """
        url = self._base_url + "balance/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        resp = self._requests.post(url, headers = self._headers, json=data_)
        return resp.json()