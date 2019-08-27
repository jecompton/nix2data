import json
import locale
import subprocess

enc = locale.getdefaultlocale()[1]
group_data = subprocess.check_output(['groups']).strip().split()
groups = [str.decode(encoding=enc, errors='strict') for str in group_data]
print(json.dumps(groups))
