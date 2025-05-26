
import requests

host = 'http://localhost:8080/ToolGateTheft/'

LOCATION="Haridwar"


def checkWithServerChallan(vehicle):
    final_url  = host + 'get-challan-status.jsp'    
    request_data = {'get_status':"temp",
                         'vehicle':vehicle,
                         'location':LOCATION
                         }
    print(request_data)
    reuquest_result = requests.post(final_url, request_data)
    print(reuquest_result.text)
    return reuquest_result
    

def checkWithServer(vehicle):
    final_url  = host + 'get-toll-status.jsp'    
    request_data = {'get_status':"temp",
                         'vehicle':vehicle,
                         'location':LOCATION
                         }
    print(request_data)
    reuquest_result = requests.post(final_url, request_data)
    print(reuquest_result.text)
    return reuquest_result



checkWithServer("UP14AB1234")