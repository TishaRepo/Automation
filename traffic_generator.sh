#!/bin/bash

#Do vagrant reload
vagrant reload ran_ue_nw
# Run the Vagrant command to start VNC server
vagrant ssh ran_ue_nw -c 'sudo pkill vnc* & sleep 1'

vagrant ssh ran_ue_nw -c 'nohup vncserver & sleep 2'

# Open VNC viewer
(vncviewer 127.0.0.1:5911 -passwd ./shared/pass.txt &)

# Execute the final_script within the Vagrant environment using Python3
vagrant ssh ran_ue_nw -c 'python3 /home/vagrant/shared/traffic_generator_guest.py > /home/vagrant/shared/traffic_generator.log 2>&1'


