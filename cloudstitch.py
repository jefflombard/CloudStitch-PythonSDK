import urllib.request
import requests
import json


domain = "api.cloudstitch.com"

def load_worksheet(user,app,worksheet):
    return Worksheet(user,app,worksheet)

def load_worksheet_data(domain,user,app,worksheet):
    # Setup
    # Set API Request path
    path = "https://{domain}/{user}/{app}/{worksheet}".format(domain=domain,user=user,app=app,worksheet=worksheet)
    
    # Transform
    response = urllib.request.urlopen(path).read()
    jsonString = response.decode("utf-8")
        
    # Output
    return json.loads(jsonString)

def add_row(domain,user,app,worksheet,data):
    # Setup
    path = "https://{domain}/{user}/{app}/{worksheet}".format(domain=domain,user=user,app=app,worksheet=worksheet)
    request = requests.post(path,data=data)
     
    # Output
    if request.status_code == 200:
        return True
    else:
        return False

class Worksheet(object):
    def __init__(self,user,app,worksheet):
        self.data = load_worksheet_data(domain,user,app,worksheet)
        self.user = user
        self.app = app
        self.worksheet = worksheet
    
    def add_entry(self,**kwargs):
        response = add_row(domain,self.user,self.app,self.worksheet,kwargs)
        
        # If success, update self.data
        if response == True:
            # Reload Data
            self.data = load_worksheet_data(domain,self.user,self.app,self.worksheet)
            return self.data
        else:
            return False
        
    # update entry method