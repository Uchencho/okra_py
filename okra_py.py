class Okra_Auth():
    """
    Okra offers a path for a customer to successfully verify their bank. 
    The customer enters their credentials and are authenticated immediately.
    
    https://docs.okra.ng/products/auth
    
    """
    import requests
    
    def __init__(self, inp_dict):
        self.api_token = inp_dict['api_token']
        self.base_url = inp_dict['base_url']
        
        
    def retrieve_auth(self):
        """
        Retrieve Bank details
        """
        url = self.base_url + "products/auths"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        resp = requests.post(url, headers = headers)
        return resp.text
    
    
    def getbyID(self, idx, page=1, limit=1):
        """
        fetch authentication info using the id of the authentication record.
        
        Args : "idx" (string): "5rggfdfghjkl4567"
        """
        url = self.base_url + "auth/getById"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"id": idx, "page": page, "limit":limit}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text
    
    
    def getbyOptions(self, first_name, last_name, page=1, limit=1):
        """
        fetch authentication info using the options metadata you provided when setting up the widget.
        
        Args : "first_name" (string): "Uchencho",
               "last_name" (string): "Nwa Alozie"
        """
        url = self.base_url + "auth/byOptions"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"page": page, "limit":limit, 
                "options":{"first_name": first_name, "last_name": last_name}}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text
    
    
    def getbyCustomer(self, customer_id, page=1, limit=1):
        """
        fetch authentication info using the customer id.
        
        Args : "customer_id" (string): "5rggfdfghjkl4567",
        """
        url = self.base_url + "auth/getByCustomer"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"page": page, "limit":limit, "customer":customer_id}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text
    
    
    def getbyDate(self, from_, to_, page=1, limit=1):
        """
        fetch authentication info using a date range.
        
        Args : "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self.base_url + "auth/getByDate"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text
    
    
    def getbyBank(self, bank_id, page=1, limit=1):
        """
        fetch authentication info using the bank id.
        
        Args : "bank_id" (string): "5rggfdfghjkl4567",
        """
        url = self.base_url + "auth/getByBank"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"page": page, "limit":limit, "bank":bank_id}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text
    
    
    def getbyCustomerDate(self, customer_id, from_, to_, page=1, limit=1):
        """
        fetch authentication for a customer using a date range and customer id.
        
        Args : "customer":"5rggfdfghjkl4567",
                "to_" (string): "2020-4-02",
                "from_" (string): "2020-01-01"
        """
        url = self.base_url + "auth/getByDateCustomer"
        headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_token}'
          }
        data_ = {"page": page, "limit":limit, "to":to_, "from":from_, "customer":customer_id}
        resp = requests.post(url, headers = headers, json=data_)
        return resp.text