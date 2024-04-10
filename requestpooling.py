

import requests

from requests.adapters import HTTPAdapter, Retry

session = requests.Session()

retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504, 429 ])

# setting status_forcelist=[429] would cause requests to retry requests that encounter a 429 (Too Many Requests) status code, indicating rate limiting, even though it is not a server error.
# 500: Internal Server Error
# 502: Bad Gateway
# 503: Service Unavailable
# 504: Gateway Timeout
# 429: Too Many Requests


# {backoff factor} * (2 ** ({number of previous retries})) seconds
# 0.1 * (2 ** (0)) = 0.1
# 0.1 * (2 ** (1)) = 0.2
# 0.1 * (2 ** (2)) = 0.4
# 0.1 * (2 ** (3)) = 0.8
# 0.1 * (2 ** (4)) = 1.6
# 0.1 * (2 ** (5)) = 3.2
# The delay increases exponentially with each retry, up to a maximum of 5 seconds.


session.mount('http://', HTTPAdapter(max_retries=retries))

session.get('http://httpstat.us/500')



# documentation at https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#module-urllib3.util.retry
# class urllib3.util.Retry(total=10, connect=None, read=None, redirect=None, status=None, other=None, allowed_methods=frozenset({'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE'}), status_forcelist=None, backoff_factor=0, backoff_max=120, raise_on_redirect=True, raise_on_status=True, history=None, respect_retry_after_header=True, remove_headers_on_redirect=frozenset({'Authorization', 'Cookie'}), backoff_jitter=0.0)


import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Define a session with a persistent connection pool
session = requests.Session()

# Configure retries and backoff for the connection pool
retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Make a request using the session
response = session.get('https://example.com')

# Process the response
if response.status_code == 200:
    print('Request successful:', response.text)
else:
    print('Request failed:', response.status_code)
