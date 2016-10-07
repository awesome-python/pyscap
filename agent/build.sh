#!/bin/bash

pyinstaller -d -y --noupx --hidden-import='message.PingMessage' --hidden-import='message.FactsRequestMessage' --hidden-import='message.RunProcessMessage' agent.py
