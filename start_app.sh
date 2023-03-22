#!/bin/bash

# Aktiviere die virtuelle Umgebung
source env_092/bin/activate

# Starte den Webserver
uvicorn backend.main:app --reload &

# Warte einen Moment, damit der Server vollständig gestartet wird
sleep 1

# Öffne ein neues Tab und wechsle in das Verzeichnis des Frontends
osascript -e 'tell application "Terminal" to activate' -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' -e 'tell application "Terminal" to do script "cd /Users/konstantinoskakoulis/dev/floretta/flo-app/frontend/ && npm run serve" in selected tab of the front window'