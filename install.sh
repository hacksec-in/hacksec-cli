sudo apt-get install git python3 python3-pip -y

if [ -d ~/hacksec-cli ] 
then
    rm -rf ~/hacksec-cli
fi
git clone https://github.com/ScRiPt1337/hacksec-cli ~/hacksec-cli
pip install -r  ~/hacksec-cli/requirements.txt
sudo chmod 777 /usr/bin/
sudo echo "python3 ~/hacksec-cli/hacksec_cli/app.py" > /usr/bin/hacksec
sudo chmod +x /usr/bin/hacksec
echo "hacksec-cli successfully installed type hacksec"