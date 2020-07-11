from .base import Initializer

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

        Returns: Response object
        """
        url = self._base_url + "products/balances"
        return self._requests.post(url, headers = self._headers)
    
    
    def getbyID(self, idx, page=1, limit=20):
        """
        fetch balance info using the id of the balance.
        
        Args : "idx" (string)
        """
        url = self._base_url + "balance/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyOptions(self, first_name, last_name, page=1, limit=20):
        """
        fetch balance info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self._base_url + "balance/byOptions"
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        return self._requests.post(url, headers = self._headers, json=data_)
    
    
    def getbyCustomer(self, customer_id, page=1, limit=20):
        """
        fetch balance info using the customer id.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "balance/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    
    def getbyAccount(self, account_id, page=1, limit=20):
        """
        fetch balance info using the account id.
        
        Args : "account_id" (string)
        """
        url = self._base_url + "balance/getByAccount"
        data_ = {"page": page, "limit":limit, "account":account_id}
        return self._requests.post(url, headers = self._headers, json=data_)


    def getbyType(self, type_, amount, page=1, limit=20):
        """
        fetch balance info using type of balance.
        
        Args : type_ (string) eg ledger_balance, available_balance
               value (string) eg 4000
        """
        url = self._base_url + "balance/getByType"
        data_ = {"page": page, "limit":limit, "type":type_, "amount":amount}
        return self._requests.post(url, headers = self._headers, json=data_)
        

    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=20):
        """
        fetch balance info of a customer using date range and customer id
        
        Args : "customer" (string):"5rggfdfghjkl4567",
                "to_" (string): "2020-04-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "balance/getByCustomerDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)


    def getRealTimeBalance(self, account_id, record_id, currency):
        """
        fetch the real-time BALANCE at anytime without heavy calculation of the transactions on each of an Record's accounts.
        
        Args : "account_id" (string),
                "record_id" (string),
                "currency" (string),
        """
        url = self._base_url + "products/balance/periodic"
        data_ = {"currency":currency, "record_id":record_id, "account_id":account_id}
        return self._requests.post(url, headers = self._headers, json=data_)
    