import os
from pathlib import Path
import json

with open("vars.json", "w+") as varsfile:
    saved_vars = json.load(varsfile)

    print("saved vars:", saved_vars)

    if not saved_vars:
        data = {"auth_token": "asfioha.135t8ugjaedher937c4n9qhwrluhqowchr.ioyu1398rqoyfugsv"}
    print("[!] Vars file is empty generating new token")

    json.dump(data,varsfile)
