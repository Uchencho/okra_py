# okra_py
Okra API wrapper in Python

===============================

[![Build Status](https://travis-ci.org/Uchencho/okra_py.svg?branch=master)](https://travis-ci.org/Uchencho/okra_py)


## Installation

To install from source, clone this repo:

    $ git clone https://github.com/Uchencho/okra_py.git


Documentation
-------------

Please see https://docs.okra.ng/ for the most up-to-date documentation for the OKRA API.


## Implementation

### Retrieve Auth Example
* **retrieve_auth**: Retrieves Bank details
  ```python
    # Import the Okra Auth class
    from okra_py.auth import Okra_Auth
    
    # Initialize with a token from okra
    ok_mod = Okra_Auth(my_okra_token)
    
    resp = ok_mod.retrieve_auth()
    
    print(resp.status_code, resp.json())
