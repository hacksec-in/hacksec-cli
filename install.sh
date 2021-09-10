#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
apt-get install git python3 python3-pip -y

if [ -d /usr/share/hacksec-cli ] 
then
    rm -rf /usr/share/hacksec-cli
fi
git clone https://github.com/ScRiPt1337/hacksec-cli /usr/share/hacksec-cli
pip install -r  /usr/share/hacksec-cli/requirements.txt
sudo echo "python3 /usr/share/hacksec-cli/hacksec_cli/app.py" > /bin/hacksec
sudo chmod +x /bin/hacksec
echo "hacksec-cli successfully installed type hacksec"
