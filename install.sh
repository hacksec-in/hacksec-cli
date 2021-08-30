sudo apt-get install git python3 python3-pip -y
git clone https://github.com/ScRiPt1337/hacksec-cli ~/hacksec-cli
pip install -r  ~/hacksec-cli/requirements.txt
sudo echo "python3 ~/hacksec-cli/hacksec_cli/app.py" > /usr/bin/hacksec