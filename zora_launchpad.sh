#!/bin/bash

echo "🚀 Zora Launchpad initializing..."

# Activate your virtual environment
source ~/Zora-TwitterBot/venv/bin/activate

# Open each module in a new Terminal tab
osascript <<EOF
tell application "Terminal"
    activate
    do script "cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_terminal.py"
    delay 1
    do script "cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_control.py" in front window
    delay 1
    do script "cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_autopilot.py" in front window
    delay 1
    do script "cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_composer.py" in front window
    delay 1
    do script "cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_scheduler.py" in front window
end tell
EOF

echo "🌌 All Zora modules launched into hyperspace."