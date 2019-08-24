## env2json.py - lists environment variables produced by the `env` coreutil as
#    json format

import os
import json

env_data = os.environ.copy()
# Break path out into a list
env_data['PATH'] = env_data['PATH'].split(':')


print(json.dumps(env_data))
