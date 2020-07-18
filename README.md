# okra_py
[Okra](https://okra.ng/) API wrapper in Python

<img src="https://pbs.twimg.com/profile_images/1199677745262989314/_D2jAMbu_400x400.jpg" alt="drawing" width="200"/> 

===============================

[![Build Status](https://travis-ci.org/Uchencho/okra_py.svg?branch=master)](https://travis-ci.org/Uchencho/okra_py)

## Installation

**_To install with pip_**

    $ pip install okra_py

**_To install from source, clone this repo:_**

    $ git clone https://github.com/Uchencho/okra_py.git
    
**_Change directory into the okra\_py folder_**

    $ cd okra_py/
    
**_Install the module_**

    $ python setup.py install


Documentation
-------------

Please see https://docs.okra.ng/ for the most up-to-date documentation for the OKRA API.


Implementation
-------------

### Sandbox/Development
By default, the class is instantiated using sandbox(developement) endpoint. To use in production, simply pass the url as an argument to 
prod_url when instantiating the class.

### Okra Auth Class
The okra auth class provides seven methods which corresponds to the okra auth product https://docs.okra.ng/products/auth. Some of the methods are shown below:
* **retrieve_auth**: retrieve the bank account and routing numbers associated with a Record's current, savings, and domiciliary accounts,
  ```python
    # Import the Okra Auth class
    from okra_py.auth import Okra_Auth
    
    # Initialize with a token from okra
    ok_mod = Okra_Auth(my_okra_token)
    
    resp = ok_mod.retrieve_auth()
    
    print(resp.status_code, resp.json())
    
* **getbyID**: fetch authentication info using the id.
  ```python
    
    the_id = "5rggfdfghjkl4567"
    resp_by_id = ok_mod.getbyID(idx=the_id)
    
    print(resp_by_id.status_code, resp_by_id.json())
    
* **getbyCustomer**: fetch authentication info using the customer id.
  ```python
    
    customer_id = "5rggfdfghjkl4567"
    resp_by_cus_id = ok_mod.getbyCustomer(customer_id=customer_id)
    
    print(resp_by_cus_id.status_code, resp_by_cus_id.json())
    
* **getbyBank**: fetch authentication info using the bank id.
  ```python
    
    bank_id = "5rggfdfghjkl4567"
    resp_by_bank_id = ok_mod.getbyBank(bank_id=bank_id)
    
    print(resp_by_bank_id.status_code, resp_by_bank_id.json())
    
    

### Balance Class Example
The okra balance class provides eight methods which corresponds to the okra balance product https://docs.okra.ng/products/balance. Some of the methods are shown below:
* **retrieve_balance**: this returns the real-time balance for each of a Record's account
  ```python
    # Import the Okra Balance class
    from okra_py.balance import Okra_Balance
    
    # Initialize with a token from okra
    ok_bal = Okra_Balance(my_okra_token)
    
    bal_resp = ok_bal.retrieve_balance()
    
    print(bal_resp.status_code, bal_resp.json())
    
* **getbyID**: fetch balance info using the id of the balance.
  ```python
    
    the_id = "5rggfdfghjkl4567"
    bal_by_id = ok_bal.getbyID(idx=the_id)
    
    print(bal_by_id.status_code, bal_by_id.json())
    
* **getbyAccount**: fetch balance info using the account id.
  ```python
    
    account_id = "5rggfdfghjkl4567"
    resp_by_account_id = ok_bal.getbyAccount(account_id=account_id)
    
    print(resp_by_account_id.status_code, resp_by_account_id.json())
    
    
    
### Production

### Retrieve Auth Production Example
* **retrieve_auth**: retrieve the bank account and routing numbers associated with a Record's current, savings, and domiciliary accounts,
  ```python
    # Import the Okra Auth class
    from okra_py.auth import Okra_Auth
    
    # Initialize with a token from okra
    prod_okr_mod = Okra_Auth(my_okra_token, prod_url='https://api.okra.ng')
    
    prod_resp = prod_okr_mod.retrieve_auth()
    
    print(prod_resp.status_code, prod_resp.json())
    
* **getbyID**: fetch authentication info using the id.
  ```python
    
    the_id = "5rggfdfghjkl4567"
    prod_resp_by_id = prod_okr_mod.getbyID(idx=the_id)
    
    print(prod_resp_by_id.status_code, prod_resp_by_id.json())
