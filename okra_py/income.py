from .base import Initializer

class OkraIncome(Initializer):
    """
    allows you to retrieve information pertaining to a Record’s income. 
    In addition to the annual income, detailed information will be provided for each contributing income stream (or job).
    
    docs link: https://docs.okra.ng/products/income
    
    Initialize with token and base_url(e.g 'https://api.okra.ng/sandbox/v1/')

    Each of the underlying methods return the full response object
    """

    def getIncome(self):
        """
        Retrieve income record

        Returns: Response object
        """
        url = self._base_url + "products/income/get"
        return self._requests.post(url, headers = self._headers)

    def getbyID(self, idx, page=1, limit=20):
        """
        retrieve information pertaining to a Record’s income using the id.
        
        Args : "idx" (string)
        """
        url = self._base_url + "income/getById"
        data_ = {"id": idx, "page": page, "limit":limit}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomer(self, customer_id, page=1, limit=20):
        """
        retrieve information pertaining to a Record’s income using the customer id.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "income/getByCustomer"
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def processIncome(self, customer_id):
        """
        process the income of particular customer using the customer's id.
        
        Args : "customer_id" (string)
        """
        url = self._base_url + "products/income/process"
        data_ = {"customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)

    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=20):
        """
        retrieve information pertaining to a Record’s income using the customer id and date range.
        
        Args : "customer" (string):"5rggfdfghjkl4567",
                "to_" (string): "2020-04-02",
                "from_" (string): "2020-01-01"
        """
        url = self._base_url + "income/getByCustomerDate"
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer":customer_id}
        return self._requests.post(url, headers = self._headers, json=data_)