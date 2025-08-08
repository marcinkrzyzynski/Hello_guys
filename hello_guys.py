from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.MoviesApiApi()
api_key = '[add user key]' # str |


krtry:
    api_response = api_instance.a_pi_top250_movies_api_key_get(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApiApi->a_pi_top250_movies_api_key_get: %s\n"% e)



    #dodaje komentarz