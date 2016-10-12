#!/bin/bash

#python -m pip install --upgrade pip

# this isn't a true requirement(s.txt) because pytest is only used for testing and pyinstaller is only used for packaging, not runtime

#pip install pytest

#pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip

# replace '#!c:\program files (x86)\python35-32\python.exe' with
# '#!"c:\program files (x86)\python35-32\python.exe"' in all the *.py files in
# C:\Program Files (x86)\Python35-32\Scripts
pyinstaller -d -y --noupx --hidden-import='message.PingMessage' --hidden-import='message.FactsRequestMessage' --hidden-import='message.RunProcessMessage' agent.py
