#dedupe.py
import hashlib as hash
import argparse

#Tries to import win10toast if installed, if not no notifications show.
try:
  import win10toast
  notify = True
except ImportError:
  noNotify = False
  
#Checks whether or not it was run from the CLI
if sys.argv:
  commandLine = True
else:
  commandline = False
