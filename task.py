#Need to install requests package for python
import requests
import sys 

TaskID = sys.argv[1]

# Set the request parameters
url = 'https://dev82746.service-now.com/api/now/table/sc_task/'+TaskID

print(url)

# Eg. User name="username", Password="password" for this code sample.
user = 'jenkins'
pwd = 'jenkins'

# Set proper headers
headers = {"Content-Type":"application/xml","Accept":"application/xml"}

# Do the HTTP request
response = requests.put(url, auth=(user, pwd), headers=headers, data="<request><entry><work_notes>Work done</work_notes><state>Closed Complete</state></entry></request>")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()

# Decode the XML response into a dictionary and use the data
print(response.content)
