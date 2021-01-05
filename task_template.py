#
# Purpose: Running some code triggered by a ServiceNow Catalogue Task and log the result there
# Author: fjonas
#
# Parameter: TaskID (sy_id of record in sc_task table)
#


#Need to install requests package for python
import requests
import sys 

# Parameter
TaskID = sys.argv[1]

# Variables
url = ''
work_notes = ''
work_state = 'Closed Complete'

# Constants
user = 'jenkins'
pwd = 'jenkins'
# Set proper headers
headers = {"Content-Type":"application/xml","Accept":"application/xml"}


# Set the request parameters
url = 'https://dev82746.service-now.com/api/now/table/sc_task/'+TaskID

# Running step 1
work_notes = work_notes + 'Running step 1\n'



#Collecting data
request_data = '<request><entry><work_notes>' + work_notes + '</work_notes><state>' + work_state + '</state></entry></request>'

# Do the HTTP request
response = requests.put(url, auth=(user, pwd), headers=headers, data="<request><entry><work_notes>Work done</work_notes><state>Closed Complete</state></entry></request>")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()

# Decode the XML response into a dictionary and use the data
print(response.content)
