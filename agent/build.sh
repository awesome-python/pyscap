#!/bin/bash
#python -m pip install --upgrade pip
# this isn't a true requirement(s.txt) because pytest is only used for testing and pyinstaller is only used for packaging, not runtime
#pip install pytest pyinstaller
pyinstaller -d -y --noupx --hidden-import='message.PingMessage' --hidden-import='message.FactsRequestMessage' --hidden-import='message.RunProcessMessage' agent.py
