import base64
print(base64.b64decode(
    'ZGVmIHRyaWUoKToKICAgIHJldHVybi'
    'BkZWZhdWx0ZGljdCh0cmllKQo='.encode()).decode())

import re

# == (.start(), .end())
print(re.search(r'123', '458971985719285712324953928572').span())

ninjas = 'ninjatreenooinjaforniggaestninjavoicenwvi9ew9ninjana'

print('Следва ли стринга този патърн?',
      re.match(r'.*ninja$', ninjas) is not None)

print('Намери всички срещания:',
      re.findall(r'n.*?a', ninjas))