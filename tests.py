#
#  test.py
#  Created by Renato Jensen Filho on 26/07/19.
#  Copyright © 2019 IBM. All rights reserved.
#

import json
from os import getenv
from datetime import datetime
import requests
import sys

wksp_id = getenv("TARGET_WORKSPACE_ID", "")
apikey = getenv("API_KEY", "")
user = "apikey"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def ts():
  return '{:%Y.%m.%d-%H.%M.%S}'.format(datetime.now())

#initialization
def init():
  if wksp_id == "" or apikey == "":
    print(ts() + " - ERROR: Initialization error")
    sys.exit(1)

def send_message():
  params = (
    ('version', '2019-02-28'),
  )
  print(ts() + " - Running test call")
  data = {"input": {"text":  "" }, "context": {}}
  data = json.dumps(data)
  try:
    r = requests.post('https://gateway.watsonplatform.net/assistant/api/v1/workspaces/' + wksp_id + '/message', params=params, headers=headers, data=data, auth=(user, apikey))
  except:
    print(ts() + " - ERROR: Request failed.")
    sys.exit(2)
  if r.status_code != 200:
    print(ts() + " - ERROR: Request returned code: " + str(r.status_code))
    sys.exit(3)
  
###

init()
send_message()

print(ts() + " - Test sucessful!")
