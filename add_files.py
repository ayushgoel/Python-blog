import os
import sys

fl = sys.argv[1]

os.system('git add {0}'.format(fl))
os.system('git commit -m "added answer {0}"'.format(fl[:fl.find('.')]))
os.system('git push -u origin master')