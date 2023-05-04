# What is this
This is a script to move mouse cursor automatically
# How to use
1. Put main.py to rpi
2. Put service file to `/etc/systemd/system/` and set its owner root and permission 755
3. `systemctl start mousemover` and `systemctl enable mousemover`