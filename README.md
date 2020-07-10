# okra_py
Okra API wrapper in Python

===============================

[![Build Status](https://travis-ci.org/Uchencho/okra_py.svg?branch=master)](https://travis-ci.org/Uchencho/okra_py)


## Installation

**_To install from source, clone this repo:_**

    $ git clone https://github.com/Uchencho/okra_py.git
    
**_Change directory into the okra_py folder_**

    $ cd okra_py/
    
**_Install the module_**

    $ python setup.py install


Documentation
-------------

Please see https://docs.okra.ng/ for the most up-to-date documentation for the OKRA API.


## Implementation

### Retrieve Auth Example
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
    
    

### Balance Class Example
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
