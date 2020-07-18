from .base import Initializer

class OkraTransaction(Initializer):
    """
    allows developers to receive customer-authorized transaction data for current, savings, and domiciliary Accounts.
    
    docs link: https://docs.okra.ng/products/transactions
    
    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')

    Each of the underlying methods return the full response object
    """

    def getTransactions(self):
        """
        Retrieve transactions

        Returns: Response object
        """
        url = self._base_url + "products/transactions"
        return self._requests.post(url, headers = self._headers)

    def getbyID(self, idx, page=1, limit=20):
        """
        fetch transaction info using the id of the transaction.
        
        Args : "idx" (string)
        """
        url = self._base_url + "transaction/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyOptions(self, first_name, last_name, page=1, limit=20):
        """
        fetch transactions info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self._base_url + "transaction/byOptions"
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomer(self, customer_id, page=1, limit=20):
        """
        fetch transaction info using the customer id.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "transaction/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyAccount(self, account_id, page=1, limit=20):
        """
        fetch transaction info using the account id.
        
        Args : "account_id" (string)
        """
        url = self._base_url + "transaction/getByAccount"
        data_ = {"page": page, "limit":limit, "account":account_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyDate(self, from_, to_, page=1, limit=20):
        """
        fetch transaction info using a date range.
        
        Args : "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "transaction/getByDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyBank(self, bank_id, page=1, limit=20):
        """
        fetch transaction info using the bank id.
        
        Args : "bank_id" (string): "5rggfdfghjkl4567",
        """
        url = self._base_url + "transaction/getByBank"
        data_ = {"page": page, "limit":limit, "bank":bank_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyType(self, type_, amount, page=1, limit=20):
        """
        fetch transaction info using type of balance.
        
        Args : type_ (string) eg ledger_balance, available_balance
               value (string) eg 4000
        """
        url = self._base_url + "transaction/getByType"
        data_ = {"page": page, "limit":limit, "type":type_, "amount":amount}
        return self._requests.post(url, headers = self._headers, json=data_)

    def SpendingPattern(self, customer_id):
        """
        fetch spending pattern of a customer.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "products/transactions/spending-pattern"
        data_ = {"customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=20):
        """
        fetch transaction info of a customer using date range and customer id
        
        Args : "customer" (string):"5rggfdfghjkl4567",
                "to_" (string): "2020-04-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "transaction/getByCustomerDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer_id":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getRealTimeBalance(self, account_id, record_id, currency):
        """
        fetch the real-time TRANSACTION at anytime on each of an Record's accounts.
        
        Args : "account_id" (string),
                "record_id" (string),
                "currency" (string),
        """
        url = self._base_url + "products/transactions/periodic"
        data_ = {"currency":currency, "record_id":record_id, "account_id":account_id}
        return self._requests.post(url, headers = self._headers, json=data_)
